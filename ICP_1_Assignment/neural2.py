sen = input("Enter your sentence:")
senList = []
senList = sen.split(" ")
newList = []
i = 0
while i < len(senList):
    if senList[i] == "python":
        newList.append("pythons")
    else:
        newList.append(senList[i])
    i+=1


strSen = ""
for word in newList:
    strSen = strSen+word+" "

print(strSen)