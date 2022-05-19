from cmath import nan
from tkinter import Y

def orderList():
    totalOrder=[]
    customerMenu = [
        {"type":"dessert","name":"cake","price":int(7)},
        {"type":"drink","name":"smoothie","price":int(8)},
        {"type":"dessert","name":"icecream","price":int(5)},
        {"type":"salad","name":"caeser","price":int(12)},
        {"type":"drink","name":"lemonade","price":int(5)},
        {"type":"burger","name":"beef","price":int(15)},
        {"type":"dessert","name":"fudge","price":int(5)}
    ]
    selection1=str(input("Enter meal type:"))
    if selection1=="cancel":
        orderList()
    print([row['name'] for row in customerMenu if row['type']==selection1])
    selection2=str(input("Select a meal:"))
    if selection2=="cancel":
        orderList()
    for row in customerMenu:
        if selection2==row["name"] and selection1==row["type"]:
            print(f"Order found || Type: {row['type']} || Name: {row['name']} || Price: {row['price']}")
            orderItem=row
    confirmation=str(input("Confirm order: [y/n] "))
    if confirmation=="y":
            print("Order successful!")
            totalOrder.append(orderItem)
            for item in totalOrder:
                print(item)
    if confirmation=="n":
            print("Order discarded.")
            orderList()
orderList()
