import sys
import math

#TICK DATA LINE FORMAT
#DD/MM/YYYY HR:MI:SE.MS  ASK   BID   
#XX.XX.XXXX XX:XX:XX.XXX,X.{X},X.{X}
# {} indicates closure (one or more digits)

#d is a dictionary that contains information for each tick
# has 9 key:value pairs,
# in order, they are: DAY, MONTH, YEAR, HOUR, MINUTE, SECOND, ASK, BID, PRICE
# the PRICE field is the average of the ASK and BID price and will be used in candlestick calculations

# Candlestick data:
# OPEN,CLOSE,HIGH,LOW

def main():
    f = open(sys.argv[1])
    timeframe = int(sys.argv[2])

    prices = []
    totalmins = 0
    currentmin = 0

    count = 0
    if(f is None):
        exit(1)
    
    for line in f:
        if not line[0].isdigit():
            continue
        else:
            line = line[:-2]
            d = processLine(line)
            if(count == 0):
                currentmin = d["MINUTE"]
            elif(currentmin != d["MINUTE"]):
                if(d["MINUTE"] < currentmin):
                    totalmins += (60 - currentmin) + d["MINUTE"]
                else:
                    totalmins += d["MINUTE"] - currentmin
                currentmin = d["MINUTE"]
            
                if(totalmins % timeframe == 0 and totalmins is not 0):
    
                    makeCandle(prices)
                    prices = []
                else:
                    prices.append(d["PRICE"])
            
            count += 1




def processLine(line):
    data = {}
    data.update({"DAY":int(line[0:2])})    
    data.update({"MONTH":int(line[3:5])})     
    data.update({"YEAR":int(line[6:10])})     
    line = line[11:]            
    data.update({"HOUR":int(line[0:2])})
    data.update({"MINUTE":int(line[3:5])})
    data.update({"SECOND":int(line[6:8])})

    line = line[13:]
    i = line.find(',')
    ask = line[0:i]
    line = line[i+1:]
    i = line.find(',')
    bid = line[0:i]

    ask = ask[0:7]
    bid = bid[0:7]

    data.update({"ASK":float(ask)})
    data.update({"BID":float(bid)})
    data.update({"PRICE":(data["ASK"] + data["BID"]) / 2})
    
    return data

def makeCandle(prices):
    openPrice = prices[0]
    closePrice = prices[-1]
    highPrice = max(prices)
    lowPrice = min(prices)
    filename = sys.argv[1][:-4] + "_" + sys.argv[2] + ".csv"

    f = open(filename, "a+")

    f.write(str(openPrice) + "," + str(closePrice) + "," + str(highPrice) + "," + str(lowPrice) + "\n")
    f.close()



if __name__ == "__main__":
    main()