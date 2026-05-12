city_name = input("Enter the city name: ")

Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

if city_name in Australia:
    print("{} is in Australia".format(city_name))
elif city_name in UAE:
    print("{} is in UAE".format(city_name))
elif city_name in India:
    print("{} is in India".format(city_name))

# Enter the city name: Sydney
# Sydney is in Australia

first_city = input("Enter the first city : ")
second_city = input("Enter the second city : ")

if first_city in Australia and second_city in Australia:
    print("Both Cities are in Australia")
elif first_city in UAE and second_city in UAE:
    print("Both Cities are in UAE")
elif first_city in India and second_city in India:
    print("Both Cities are in India")
else:
    print("They don't belong to the same country")

# Enter the first city : Sydney
# Enter the second city : Dubai
# They don't belong to the same country
