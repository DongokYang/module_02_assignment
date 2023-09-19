"""
Description:
Author: Dongok Yang
Date: 2023.09.18
Usage:
"""

#SIMPLE DATA TYPES
name = "Dongok"
print(f"value:{name} type: {type(name)}")

have_Manitoba_drivers_license = False
print(f"value:{have_Manitoba_drivers_license} type: {type(have_Manitoba_drivers_license)}")

this_year = 2023
print(f"this year:{this_year} type: {type(this_year)}")

this_year +=1 
print(f"next year:{this_year} type: {type(this_year)}")

#CALCULATIONS
CANADA_GST_RATE = 0.05
MANITOBA_PST_RATE = 0.07
vehicle_price = 22503.03
price_inclue_tax = vehicle_price + vehicle_price *(CANADA_GST_RATE + MANITOBA_PST_RATE)
print(f"pre-tax value: ${vehicle_price:.2f} PST: {vehicle_price*MANITOBA_PST_RATE:.2f} GST: {vehicle_price*CANADA_GST_RATE:.2f} total: ${price_inclue_tax:.2f}")

#LISTS
number_list = [1,2,3,4,5,6,7,8,9,10]
print(type(number_list))
print(number_list)
number_list[5:5] = ["Dongok"]
print(number_list)
number_list.remove(9)
print(number_list)
second_list = ['A','B','C']
third_list = number_list + second_list
print(third_list)

#TUPLES
provinces = ('Manitoba','Ontario','Quebec','Alberta')
print(provinces)
<<<<<<< HEAD
print(type(provinces))
=======
print(type(provinces))
#DICTIONARIES
canada_currency = {'nickel': 0.05, 'dime': 0.10, 'quarter': 0.25}
print(canada_currency)
print(type(canada_currency))
canada_currency['nickel'] = 5
canada_currency['dime'] = 10
canada_currency['quarter'] = 25
print(canada_currency)
canada_currency['loonie'] = 100
canada_currency['toonie'] = 200
print(canada_currency)
#SETS

evennumbers = set(range(2,21,2))
print(evennumbers)
print(type(evennumbers))
fivenumbers = set(range(5,21,5))
print(fivenumbers)
unionset = evennumbers.union(fivenumbers)
print(unionset)
intersectionset = evennumbers.intersection(fivenumbers)
print(intersectionset)
differenceset = evennumbers.difference(fivenumbers)
print(differenceset)
differenceset2 = fivenumbers.difference(evennumbers)
print(differenceset2)
>>>>>>> cfc85c15eb2e68e42a4f10e9e869a6ec53325b89
