# waxy
Converts market tick data into candlestick data of any time frame<br>

- Input format: DD.MM.YYYY HH:MM:SS.MSS,BID,ASK
- Tick data taken from [Dukascopy](https://www.dukascopy.com/swiss/english/marketwatch/historical/) is in this format
- Dukascopy also includes the ask and bid volume, this program does not use those values, as they are not necessary to construct candlesticks
- I have included 1 day of sample tick data `EURUSD_TICKS.csv` for testing purposes
- output filename = input filename + "_<TIMEFRAME>"

# Usage
`python waxy.py <filename.csv> <timeframe (in minutes)>`
