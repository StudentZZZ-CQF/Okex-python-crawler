import requests
url = 'https://www.okex.com/api/spot/v3/instruments/BTC-USDT/candles?granularity=300&start=2021-05-20T16:00:00.000Z&end=2021-07-20T16:00:00.000Z'
response = requests.get(url)
response.json()
XBTCUSDT=response.json()
url = 'https://www.okex.com/api/spot/v3/instruments/LTC-USDT/candles?granularity=300&start=2021-07-19T16:00:00.000Z&end=2021-07-20T16:00:00.000Z'
response = requests.get(url)
response.json()
XLTCUSDT=response.json()
def datalist(X:list,n:int):
    Datalist=[]
    for i in range(len(X)):
        Datalist.append(X[i][n])
    return Datalist
def strtofloat(X):
    XN=[]
    for i in range(len(X)):
        XN.append(float(closel[i]))
    return XN
#BTCUSDT TO CSV
timel=datalist(XBTCUSDT,0)
openl=datalist(XBTCUSDT,1)
highl=datalist(XBTCUSDT,2)
lowl=datalist(XBTCUSDT,3)
closel=datalist(XBTCUSDT,4)
volumel=datalist(XBTCUSDT,5)
openN=strtofloat(openl)
highN=strtofloat(highl)
lowN=strtofloat(lowl)
closeN=strtofloat(closel)
volumeN=strtofloat(volumel)
dfY = pd.DataFrame(columns=['time','open','high','low','close','volume'])
dfY.time=timel
dfY.open=openN
dfY.high=highN
dfY.low=lowN
dfY.close=closeN
dfY.volume=volumeN
dfY.to_csv("BTCUSDT.csv",index=False,sep=',')
#XLTUSDT TO CSV
timel=datalist(XLTCUSDT,0)
openl=datalist(XLTCUSDT,1)
highl=datalist(XLTCUSDT,2)
lowl=datalist(XLTCUSDT,3)
closel=datalist(XLTCUSDT,4)
volumel=datalist(XLTCUSDT,5)
openN=strtofloat(openl)
highN=strtofloat(highl)
lowN=strtofloat(lowl)
closeN=strtofloat(closel)
volumeN=strtofloat(volumel)
dfY = pd.DataFrame(columns=['time','open','high','low','close','volume'])
dfY.time=timel
dfY.open=openN
dfY.high=highN
dfY.low=lowN
dfY.close=closeN
dfY.volume=volumeN
dfY.to_csv("XLTCUSDT.csv",index=False,sep=',')