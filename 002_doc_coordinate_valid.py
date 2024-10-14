import re

def user_coordinates():
    # Regular expression to match coord in a valid format (Latitude, Longitude)
    pattern = r'^[-]?([1-8]?\d(\.\d+)?|90(\.0+)?)\s*,\s*[-]?((1[0-7][0-9]|[1-9]?\d)(\.\d+)?|180(\.0+)?)$'

    while True:
        user_input = input("Please enter your coordinates (latitude, longitude): ").strip()

        # Check if it matches the pattern
        if re.match(pattern, user_input):
            # Split and parse
            latitude, longitude = map(str.strip, user_input.split(','))
            try:
                lat_float = float(latitude)
                lon_float = float(longitude)

            # Check if valid range
                if -90 <= lat_float and -180 <= lon_float <= 180:
                    return lat_float,lon_float
                else:
                    print("Coordinates are out of range. Try Again")
            
            except ValueError:
                print("Invalid Coordinate. Try again")

        else:
            print("Invalid Coordinate. Try again")

# Test
latitude, longitude = user_coordinates()
print(f"Valid coordinates given: Latitude = {latitude}, Longitude = {longitude}")