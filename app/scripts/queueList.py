def queueList():
    totalOrder = [
        {"type":"dessert","name":"cake","price":int(7)},
        {"type":"burger","name":"beef","price":int(15)},
        {"type":"drink","name":"lemonade","price":int(5)}
    ]
    queueList = [
        {"primaryOrder"},
        {"secondaryOrder"},
        {"tertiaryOrder"}
    ]
    queueList.extend(totalOrder)
    print(queueList)
    selection1 = input("Would you like to remove an order? y/n")
    if selection1 == "n":
        queueList()
    if selection1 == "y":
        print("Alrightie")
    selection2 = input("Select order to remove")
    if selection2 == "1":
        totalOrder.pop(1)
        print(queueList)
    elif selection2 == "2":
        totalOrder.pop(2)
        print(queueList)
    elif selection2 == "3":
        totalOrder.pop(3)
        print(queueList)
    elif selection2 =="Latest":
        totalOrder.pop(-1)
        print(queueList)
queueList()