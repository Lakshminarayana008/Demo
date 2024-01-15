string = input("Enter your string of at least 6 characters:")
print("Your string:", string)
strList = []
strList[:0] = string
print("String as list:", strList)
strList.pop(-2)
strList.pop(3)
print("String with 5th character removed:", strList)
strList.reverse()
print("Reversed list:",strList)


newStr = ""
for i in strList:
    newStr = newStr+i
print("Resulting string:",newStr)