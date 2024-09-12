purchase_amount =int(input("Enter the purchase amount: $"))
if purchase_amount >= 100:
    Discount=(purchase_amount*10)/100
else:
    Discount=(purchase_amount*5)/100
print(f"The discount amount is: $ {Discount:}")
print("Net pay : $",purchase_amount-Discount )
