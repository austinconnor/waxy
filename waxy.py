import sys
import math

#TICK DATA LINE FORMAT
#DD/MM/YYYY HR:MI:SE.MS  ASK   BID   
#XX.XX.XXXX XX:XX:XX.XXX,X.{X},X.{X}
# {} indicates closure (one or more digits)


def main():
    f = open(sys.argv[1])
    timeframe = int(sys.argv[2])

    count = 0
    if(f is None):
        exit(1)
    
    for line in f:
        if not line[0].isdigit():
            continue
        else:
            count += 1
            line = line[:-2]
            d = processLine(line)



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

    print("DAY:\t" + str(data["DAY"]))
    print("MONTH:\t" + str(data["MONTH"]))
    print("YEAR:\t" + str(data["YEAR"]))
    print("HOUR:\t" + str(data["HOUR"]))
    print("MINUTE:\t" + str(data["MINUTE"]))
    print("SECOND:\t" + str(data["SECOND"]))
    print("ASK:\t" + str(data["ASK"]))
    print("BID:\t" + str(data["BID"]))
    print("PRICE:\t" + str(data["PRICE"]))
    
    print("")
    
    return data

if __name__ == "__main__":
    main()