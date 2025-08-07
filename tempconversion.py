temperature = float(input("enter a temperature:"))
unit = input("is this celcius or fahrenheit:")

if unit == "celcius":
    temperature = round((9*temperature)/5 + 32,2)
    unit = "fahrenheit"
    print(f"the temperature is {temperature} {unit}")
elif unit == "fahrenheit":
    temperature = round((temperature - 32)*9/5,2)
    unit = "celcius"
    print(f"the temperature is {temperature} {unit}")
else:
    print("invalid unit")