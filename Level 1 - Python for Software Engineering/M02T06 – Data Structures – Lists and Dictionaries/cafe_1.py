menu_item = ["Applepie",
             "Coffee",
             "Tea",
             "Milktart"]

stock_item = {"Applepie" : 3,
              "Coffee" : 2,
              "Tea" : 5,
              "Milktart" : 6}

price_item = {"Applepie" : 5.99,
              "Coffee" : 3.25,
              "Tea" : 10,
              "Milktart" : 4.50}


total_stock = 0

for item , value in stock_item.items():
    item_value = (stock_item[item] * price_item[item])
    total_stock += item_value
    
print(total_stock)