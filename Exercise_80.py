try:
    today_temperature = float(input("Enter today's temperature in Celsius: "))
    yesterday_temperature = float(input("Enter yesterday's temperature in Celsius: "))
    
    if today_temperature > yesterday_temperature:
        print("Today is warmer than yesterday.")
    elif today_temperature < yesterday_temperature:
        print("Today is colder than yesterday.")
    else:
        print("Today has the same temperature as yesterday.")
except ValueError:
    print("Please enter valid numerical values for temperatures.")