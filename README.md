# waxy
Converts market tick data into candlestick data of any time frame<br>

Tick data format:
- DD.MM.YYYY HH:MM:SS.MSS,BID,ASK
- Data is followed by Ask and Bid Volume, however these values are not used

# Usage
`python waxy.py <filename.csv> <timeframe (in minutes)`
