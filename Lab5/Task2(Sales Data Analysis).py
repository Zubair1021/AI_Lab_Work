import pandas as pd
import numpy as np
import random as rand
import matplotlib.pyplot as plt

Product_Name = ['Prod1','Prod2','Prod3','Prod4','Prod5','Prod6','Prod7','Prod8','Prod9','Prod10']
Product = []
Price = []
Date_Purchase = []
Quantity = []

for i in range(1, 501):
    Price.append(rand.randint(10, 1000))
    Quantity.append(rand.randint(1, 20))
    Product.append(Product_Name[rand.randint(0, 9)])
    
    d = np.datetime64('2024-10-02')
    number = np.random.randint(0, 365)
    d += number
    Date_Purchase.append(d)


Data = {
    "Product Name": Product,
    "Price": Price,
    "Quantity": Quantity,
    "Date of Purchase": Date_Purchase        
}

data_frame = pd.DataFrame(Data,index=np.arange(1,501))

#print(data_frame)



Price_Array = np.array(data_frame["Price"])
Quantity_Array = np.array(data_frame["Quantity"])

total_sales = Price_Array*Quantity_Array
print("Total Sales of First Ten Products",total_sales[:10])

data_frame["Total Sales"] = data_frame["Price"] * data_frame["Quantity"]
print("Products having Sales more 100$ \n",data_frame[data_frame["Total Sales"]>100])


print(data_frame.groupby("Product Name").sum(True)["Quantity"])


plt.title("Relation b/w Price and Quantity of products sold")
plt.scatter(data_frame["Price"], data_frame["Quantity"])
plt.xlabel("Price")
plt.ylabel("Quantity")
plt.show()


plt.title("Distribution of total sales values")
plt.hist(data_frame["Total Sales"], bins=10, rwidth=0.9)
plt.xlabel("Sale")
plt.ylabel("Quantity")
plt.show()
