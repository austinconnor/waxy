# waxy
Converts Forex market tick data into candlestick data of any time frame<br>

- Input format: `DD.MM.YYYY HH:MM:SS.MSS,BID,ASK`
- Tick data taken from [Dukascopy](https://www.dukascopy.com/swiss/english/marketwatch/historical/) is in this format
- Dukascopy also includes the ask and bid volume, this program does not use those values, as they are not necessary to construct candlesticks
- I have included 1 day of sample tick data `EURUSD_TICKS.csv` for testing purposes
- output filename = `input filename + "_TIMEFRAME"`
- Candlestick data is given as `OPEN,HIGH,LOW,CLOSE`

# Usage
`python waxy.py <filename.csv> <timeframe (in minutes)>`

# Example
`python waxy.py EURUSD_TICKS.csv 60`

`cat EURUSD_TICKS_60.csv`

```
open,high,low,close
1.3245,1.326075,1.324375,1.324975
1.325275,1.3267,1.32485,1.32515
1.324975,1.3266,1.324825,1.32505
1.325175,1.325675,1.325,1.325375
1.32528,1.326575,1.32495,1.326575
1.3266,1.3276,1.326525,1.32725
1.32715,1.329975,1.32695,1.328825
1.329725,1.330175,1.326775,1.32775
1.328125,1.328325,1.3229,1.3258
1.326325,1.327,1.324575,1.32545
1.325675,1.3327,1.325525,1.33145
1.330025,1.330025,1.327425,1.328675
1.328475,1.329725,1.3253,1.32595
1.32615,1.327825,1.32405,1.327275
1.3261,1.327375,1.3244,1.32575
1.3256,1.32765,1.3256,1.326875
1.326225,1.32735,1.32575,1.326175
1.326025,1.327075,1.325875,1.325875
1.32635,1.327375,1.326175,1.326775
1.326725,1.327125,1.32565,1.3266

```
