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
print(f"pre-tax value: {vehicle_price} PST: {vehicle_price*MANITOBA_PST_RATE} GST: {vehicle_price*CANADA_GST_RATE} total: {price_inclue_tax}")

#LISTS

#TUPLES

#DICTIONARIES

#SETS

