import re

def validate_coord(user_input):
    """Validate if the input is a valid coordinate (latitude, longitude)."""
    if user_input == "":
        return False  # Reject empty input

    # Regular expression to match coordinates in the format "latitude, longitude"
    pattern = r'^[-]?([1-8]?\d(\.\d+)?|90(\.0+)?)\s*,\s*[-]?((1[0-7][0-9]|[1-9]?\d)(\.\d+)?|180(\.0+)?)$'
    
    if not re.match(pattern, user_input):
        return False

    # Split the input into latitude and longitude
    latitude, longitude = user_input.split(',')
    
    try:
        lat_float = float(latitude.strip())
        lon_float = float(longitude.strip())

        # Check if both latitude and longitude have a decimal part
        if lat_float.is_integer() or lon_float.is_integer():
            return False

        return True
    except ValueError:
        return False

# Testing the function
test_cases = [
    "1, 1",               # Invalid
    "1.0, 1.0",           # Invalid
    "36.912, 174.870",    # Valid
    "-36.912, 174.870",   # Valid
    "90, 180",            # Invalid
    "-90.0, -180.0",      # Invalid
    "36.912, 174",        # Invalid
]

for test in test_cases:
    print(f"Input: {test}, Valid: {validate_coord(test)}")
