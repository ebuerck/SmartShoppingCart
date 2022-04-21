print("Scanner Ready")
item_count = 0
scode = ""
scan_mesg = "Scanned Barcode is: "
while(1):
	scode = str(input("Scan your code: "))
	print(scan_mesg + scode)
	item_count += 1




