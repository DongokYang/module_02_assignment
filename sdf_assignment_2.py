"""
Description: this file is created to practice basic python grammars and PEP8 standards
Author: Dongok Yang
Date: 2023.09.18
Usage:
"""

#SIMPLE DATA TYPES
# the codes below shows what types of data types exists and how to use it
name = "Dongok"
print(f"value:{name} type: {type(name)}")

have_Manitoba_drivers_license = False
print(f"value:{have_Manitoba_drivers_license} type: {type(have_Manitoba_drivers_license)}")

this_year = 2023
print(f"this year:{this_year} type: {type(this_year)}")

this_year +=1 
print(f"next year:{this_year} type: {type(this_year)}")

#CALCULATIONS
# the codes below shows how to use calculation with python
CANADA_GST_RATE = 0.05
MANITOBA_PST_RATE = 0.07
vehicle_price = 22503.03
price_inclue_tax = vehicle_price + vehicle_price *(CANADA_GST_RATE + MANITOBA_PST_RATE)
print(f"pre-tax value: ${vehicle_price:.2f} PST: {vehicle_price*MANITOBA_PST_RATE:.2f} GST: {vehicle_price*CANADA_GST_RATE:.2f} total: ${price_inclue_tax:.2f}")

#LISTS
# the codes below shows how to use LIst with python
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
# the codes below shows how to use tuples with python
provinces = ('Manitoba','Ontario','Quebec','Alberta')
print(provinces)
print(type(provinces))

#DICTIONARIES
# the codes below shows how to use dictionaries with python
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
# the codes below shows how to use sets with python
even_numbers = set(range(2,21,2))
print(even_numbers)
print(type(even_numbers))
five_numbers = set(range(5,21,5))
print(five_numbers)
unionset = even_numbers.union(five_numbers)
print(unionset)
intersection_set = even_numbers.intersection(five_numbers)
print(intersection_set)
difference_set = even_numbers.difference(five_numbers)
print(difference_set)
difference_set2 = five_numbers.difference(even_numbers)
print(difference_set2)
