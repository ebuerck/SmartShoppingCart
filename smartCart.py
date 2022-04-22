import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('ItemData.xlsx')

priceList = df['Price'].tolist()
barcodeList = df['Barcode #'].tolist()
descriptionList = df['Description'].tolist()
# print(df)
# print(df.columns.tolist())
# print(barcodeList)
# print(descriptionList)
i = 0
totalPrice = 0
scode = ""

while scode != 55555:
    scode = int(input("Scan your item:"))
    i = 0
    for x in barcodeList:
        if x == scode:
            totalPrice += priceList[i]
        i += 1
print(totalPrice)
