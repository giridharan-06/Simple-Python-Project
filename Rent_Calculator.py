#INPUT
'''
Enter the Total Rent Amount:
Enter the Total food expense:
Enter the Water Expense:
Enter the Maintance amount:
Enter the Total Electricity Unit Runned:
Enter the Electricity per Unit cost:
Enter the No.of persons in Room/flat: 
'''
#OUTPUT
'''
Total Amount to pay per person:
'''

rent=int(input("Enter the Rent Amount:"))

food_expence=int(input("Enter the Food Expence:"))

water_bill=int(input("Enter the Water expense:"))

maintance=int(input("Enter the Maintance charge:"))

electricity_unit=int(input("Enter the Total Electricity Unit:"))

unit_cost = int(input("Enter the Per unit cost:"))

persons=int(input("Enter the persons in room/flat:"))

Total=(electricity_unit*unit_cost + food_expence +water_bill+maintance+ rent)//persons

print(f'The amount each person is to pay is Rupees:{Total}')
