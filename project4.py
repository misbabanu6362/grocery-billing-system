products={
    "rice":50,
    "oil":140,
    "biscuit":20,
    "brush":30,
    "paste":70,
    "milk":30,
    "ghee":500,
    "water":10
}
total=0
cart=[]
while True:
    print("1.add item")
    print ("2.print bill")
    choice=int(input("Enter your choice(1-2) "))
    if choice==1:
        key=input("Enter product name ").lowe()
        value=products.get(key)
        print(value)
        if value==None:
            print("Item not in stock")
            continue
        quantity=int(input("Enter quantity "))
        product_total=value*quantity
        total=total+product_total
        cart.append(f"{key}*{quantity}={product_total}")
        #print(total)
    elif choice==2:
        break
    else :
        print("Invalid choice")        
 
print("=====FINAL BILL=====")
for item in cart:    
    print(item)
print("total bill = ",total)
discount=10
if total>=500:
    with_discount=(discount/100)*total
    print("discount 10% =",with_discount)
    new_bill=total-with_discount
    print("final bill = ",new_bill)
    print("Thank you")
else:
    print("Thank you")    
