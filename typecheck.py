costum=input("whats your id? : ")
list1={"id":"94","name":"agrin","department":"Dinning"}
for value in list1.keys():
    if value==int(costum):
        print(list1.values())
        break
   