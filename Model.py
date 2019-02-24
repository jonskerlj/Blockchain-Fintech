import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#plt.plot([1,2,3,4])
#plt.ylabel('some numbers')
#plt.show()
price = []


#importing data
df = pd.read_csv('datas/BTC_USD Bitfinex Historical Data (1).csv')
for n in range(len(df['Price'])):
    #removing the colon
    if "," in df['Price'][n]:
        b = df['Price'][n]
        b = b.replace(",", "")

    else:
        b = df['Price'][n]

    price.append(b)

#Raw price
price = [float(i) for i in price]
price.reverse()

#12 day moving average
N = 12
cumsum, moving_aves = [0], []

for i, x in enumerate(price, 1):
    cumsum.append(cumsum[i-1] + x)
    if i>=N:
        moving_ave = (cumsum[i] - cumsum[i-N])/N
        #can do stuff with moving_ave here
        moving_aves.append(moving_ave)

#First derivative
#dev1 = np.empty(shape=1, dtype=float)
dev1 = []
for n in range(len(moving_aves)):
    if n == 0:
        dev1.append(0)
    else:
        dev1.append(moving_aves[n] - moving_aves[n-1])


#second moving average(of 1st derivative)
cumsum2, moving_aves2 = [0], []
N = 12
for i, x in enumerate(dev1, 1):
    cumsum2.append(cumsum2[i-1] + x)
    if i>=N:
        moving_ave2 = (cumsum2[i] - cumsum2[i-N])/N
        #can do stuff with moving_ave here
        moving_aves2.append(moving_ave2)

#2nd derivative
dev2 = []
for n in range(len(moving_aves2)):
    if n == 0:
        dev2.append(0)
    else:
        dev2.append(moving_aves2[n] - moving_aves2[n-1])

#3rd moving average:
cumsum3, moving_aves3 = [0], []
N = 12
for i, x in enumerate(dev2, 1):
    cumsum3.append(cumsum3[i-1] + x)
    if i>=N:
        moving_ave3 = (cumsum3[i] - cumsum3[i-N])/N
        #can do stuff with moving_ave here
        moving_aves3.append(moving_ave3)

InvArr = []
a = 0;
#starts on the 36th day
#getting the buy and sell array
for n in range(len(moving_aves3)):
    if moving_aves2[n]>0 and moving_aves3[n]>0:
            a = 'Buy'
    if moving_aves2[n]<0 and moving_aves3[n]<0:
            a = 'Sell'
    if moving_aves2[n]>0 and moving_aves3[n]<0:
            a = 'Sell'
    if moving_aves2[n]<0 and moving_aves3[n]>0:
            a = 'Buy'
    if moving_aves2[n]==0 or moving_aves3[n]==0:
        a = 0;

    Buying = 'Buy'
    Selling = 'Sell'
    if n==0:
        InvArr.append(a)
        k = n
    elif InvArr[k]==a:
        InvArr.append(0)
    elif InvArr[k] != a:
        InvArr.append(a)
        k=n

#
Money=100000;

for n in range(len(moving_aves3)):
    if InvArr[n]=='Buy':
        Money = Money - price[n+36]
    elif InvArr[n]=='Sell':
        Money = Money + price[n+36]


print('Data used: BTC_USD Bitfinex Historical Data (1).csv')
print("Invest Array:")
print(InvArr)
print('Money at the start:', 100000)
print('Money in the end:', round(Money))

print('Increase:', round(((round(Money)/100000)-1)*100), '%.')
