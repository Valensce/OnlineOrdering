# FOR item IN orderlist
#      SET price = orderItem.price
#      SET total = total + price

def calcBill():

    totalOrder = [
        {
            "type": "dessert",
            "name": "cake",
            "price": 7
        },
        {
            "type": "burger",
            "name": "beef",
            "price": 15
        },
        {
            "type": "drink",
            "name": "lemonade",
            "price": 5
        }
    ]

    total = 0

    for row in totalOrder:

        price = row["price"]
        total = total + price

    print(total)
    
calcBill()
