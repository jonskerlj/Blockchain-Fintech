import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#plt.plot([1,2,3,4])
#plt.ylabel('some numbers')
#plt.show()
price = []

df = pd.read_csv('BTC_USD Bitfinex Historical Data (1).csv')
for n in range(len(df['Price'])):
    if "," in df['Price'][n]:
        b = df['Price'][n]
        b = b.replace(",", "")

    else:
        b = df['Price'][n]

    price.append(b)

#Raw price
price = [float(i) for i in price]

#First derivative
#dev1 = np.empty(shape=1, dtype=float)
dev1 = []
for n in range(len(price)):
    if n == 0:
        dev1.append(0)
    else:
        dev1.append(price[n] - price[n-1])


dev2 = []
for n in range(len(dev1)):
    if n == 0:
        dev2.append(0)
    elif n==1:
        dev2.append(0)
    else:
        dev2.append(dev1[n] - dev1[n-1])
dev1 = [float(i) for i in dev1]
dev2 = [float(i) for i in dev2]
for n in range(len(dev2)):
    if abs(dev1(n))<0.5 and abs(dev2)>100:
        print('Selling points')
        print(n)


print(price)
plt.figure(1)
plt.plot(price)
plt.ylabel('Price')
plt.show()


print(dev1)
plt.figure(2)
plt.plot(dev1, 'bo')
plt.ylabel('First derivative')
plt.show()
