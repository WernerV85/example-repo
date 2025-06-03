menu_item = ["Apple pie",
             "Coffee",
             "Tea",
             "Milk tart"]

stock_item = {"Apple pie" : 3,
              "Coffee" : 2,
              "Tea" : 5,
              "Milk tart" : 6}

price_item = {"Apple pie" : 5.99,
              "Coffee" : 3.25,
              "Tea" : 10,
              "Milk tart" : 4.50}


total_stock = 0

for item , value in stock_item.items():
    item_value = (stock_item[item] * price_item[item])
    total_stock += item_value
    
print(total_stock)