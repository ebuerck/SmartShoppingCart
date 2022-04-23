import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('ItemData.xlsx')

priceList = df['Price'].tolist()
barcodeList = df['Barcode #'].tolist()
descriptionList = df['Description'].tolist()
File_object = open("Receipt.txt", "w")
File_object.write("Smart Shopping Cart\n")
File_object.write("--------------------\n")
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
            File_object.write(str(descriptionList[i]) + "          " + str(priceList[i]) + "\n")
            totalPrice += priceList[i]
        i += 1
print("Thank you for shopping!\n")
File_object.write("--------------------\n")
File_object.write("Total Price:          " + str(totalPrice) + "\n")
File_object.write("Thank you for shopping!")
