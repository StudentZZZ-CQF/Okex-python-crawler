import requests
url = 'https://www.okex.com/api/spot/v3/instruments/BTC-USDT/candles?granularity=300&start=2021-05-20T16:00:00.000Z&end=2021-07-20T16:00:00.000Z'
response = requests.get(url)
response.json()
XBTCUSDT=response.json()

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
#bolling
middle = dfY['close'].rolling(30).mean()
std = dfY['close'].rolling(30).std()
Upperband=middle+std
Lowerband=middle-std
dfY['middle']=middle
dfY['Upperband']=Upperband
dfY['Loweband']=Lowerband
NDF=dfY.dropna()
NDF.index = range(1,len(NDF) + 1)
#Profit and Loss
def status(DF):
    DFstatus=[]
    Sell=NDF['close']>NDF['Upperband']
    buy=NDF['close']<NDF['Loweband']
    for i in range(len(DF)):
        if Sell[i]==True:
            DFstatus.append(1)
        elif buy[i]==True:
            DFstatus.append(-1)
        else:
            DFstatus.append(0)   
    DF['BorSell']=DFstatus

def AmountandPL(DF):
    Amount=[]
    PL=[0]
    Amount.append(DF['BorSell'][0])
    for i in range(1,len(DF)):
        if DF['BorSell'][i]==1 and sum(Amount[:i])>=0:
            Amount.append(1)
            PL.append(0)
        elif DF['BorSell'][i]==1 and sum(Amount[:i])<=0:
            Amount.append(-sum(Amount[:i]))
            PL.append(1)
        elif DF['BorSell'][i]==-1 and sum(Amount[:i])<=0:
            Amount.append(-1)
            PL.append(0)
        elif DF['BorSell'][i]==-1 and sum(Amount[:i])>=0:
            Amount.append(-sum(Amount[:i]))
            PL.append(1)
        else:
            Amount.append(0)
            PL.append(0)
    DF['Amount']=Amount
    DF['PL']=PL

def PandL(DF):
    PandL=[]
    for i in range(len(DF)):
        Price=NDF['close']*NDF['Amount']
        PandL.append(sum(Price[:i+1]))
    DF['PandL']=PandL

status(NDF)
AmountandPL(NDF)
PandL(NDF)
import matplotlib.pyplot as plt
PandL=NDF['PL']*NDF['PandL']
for i in range(len(PandL)-1):
    if PandL[i]!=0 and PandL[i+1]==0:
        PandL[i+1]=PandL[i]
plt.plot(PandL)