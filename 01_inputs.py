
######################## INPUTS
import re

print("Hello,! Welcome to Find and Dine!")

def valid_gps_format(coord):
    pattern = r'^[-]?[0-9]{1,2}\.[0-9]+,\s*[-]?[0-9]{1,3}\.[0-9]+$'
    return re.match(pattern, coord) is not None

while True:
    user_loc = input("Please input your location through coordinates (latitude, longitude)")

    if valid_gps_format(user_loc):
        break
    else:
        print("Sorry, there's something wrong. Please try again")
