import os
import json
from urllib.request import urlopen
os.system('clear')

CONVERT_TO = {
    'volume': {
            'tsp': 48,
            'tbsp': 16,
            'c': 1,
            'q': .25,
            'p': .5,
            'gal': .0625,
            'oz': 8
        },
    'mass': {
            'g': 453.59,
            'oz': 16,
            'lb': 1,
            'kg': 0.45359
        }
}

CONVERT_FROM = {
    'volume': {
            'tsp': .015625,
            'tbsp': .0625,
            'c': 1,
            'q': 4, 
            'p': 2, 
            'gal': 16,
            'oz': .125
        },
    'mass': {
            'g': .0022046,
            'oz': .0625,
            'lb': 1,
            'kg': 2.2406
        }
}

#Temparature Conversion
def temp():
    print("""\n 1: Celsius to Fahrenheit
                2. Celsius to Kelvin
                3. Fahrenheit to Celsius
                4. Fahrenheit to Kelvin
                5. Kelvin to Celsius
                6. Kelvin to Fahrenheit""")
    option = int(input("Enter conversion type: "))
    if option == 1:
        degree = int(input("Enter temperature to convert: "))
        result = (degree * 1.8) + 32
        unit = 'F'
    elif option == 2:
        degree = int(input("Enter temperature to convert: "))
        result = degree + 273.15
        unit = 'K'
    elif option == 3:
        degree = int(input("Enter temperature to convert: "))
        result = (degree - 32) / 1.8
        unit = 'C'
    elif option == 4:
        degree = int(input("Enter temperature to convert: "))
        result = ((degree - 32) / 1.8) + 273.15
        unit = 'K'
    elif option == 5:
        degree = int(input("Enter temperature to convert: "))
        result = degree - 273.15
        unit = 'C'
    elif option == 6:
        degree = int(input("Enter temperature to convert: "))
        result = ((degree - 273.15) * 1.8) + 32
        unit = 'F'
    else:
        print("Invalid selection")
        temp()
    print("Value: " + str(result) + ' ' + unit)

#Mass and Volume Conversion
def convert(conversion):
    conversion_units = ','.join(CONVERT_FROM[conversion].keys())
    amount = float(input("Enter conversion amount:"))
    source_unit = input("Enter source unit (%s):" % conversion_units)
    to_unit = input("Enter unit to convert to (%s):" % conversion_units)
    print("%s %s's equals %f %s's" % (amount, source_unit, 
            amount * \
            CONVERT_FROM[conversion][source_unit] * \
            CONVERT_TO[conversion][to_unit],
            to_unit))

#Currency Conversion
def currency():
    amount = str(input("Enter amount to convert: "))
    from_currency = str(input("Enter your source currency (3 digit code): "))
    to_currency = str(input("Enter the currence you would like to convert to (3 digit code): "))
    request = urlopen('http://rate-exchange.appspot.com/currency?from=' + from_currency + '&to=' + to_currency + '&q=' + amount)
    response = json.loads(request.read())
    print("%s %s is equal to %f %s" % (amount, from_currency, float(response['v']), to_currency))

#Main Part
print(""" 1: Temperature
          2: Volume
          3: Mass
          4: Currency""")

given_input = int(input("Enter conversion type: "))

if given_input == 1:
    temp()
elif given_input == 2:
    convert('volume')
elif given_input == 3:
    convert('mass')
elif given_input == 4:
    currency()
else:
    print("Invalid selection!! Please Select Properly")






