import random

# Data for fast food locations
fastf_locs = [
    ("Birdy Bytes \n Ratings: 4.7 / 5", -36.91540360714608, 174.87203796632136),
    ("Burger Fuel \n Ratings: 4.5 / 5", -36.9107909781057, 174.87174736090853),
    ("Subway \n Ratings: 3.8 / 5", -36.91268903482884, 174.87155663683762),
    ("Mcdonalds \n Ratings: 3.3 / 5", -36.89963910924124, 174.90058447864246),
    ("Mighty Hotdog \n Ratings: 4.4 / 5", -36.9123325342632, 174.87065238555024),
    ("Ok Chiken \n Ratings: 4.5 / 5", -36.91225777477972, 174.87061862899873),
    ("Pakuranga Pizza \n Ratings: 4.5 / 5", -36.9153257155152, 174.88970536578574),
    ("Noodle Canteen \n Ratings: 3.8", -36.912581675641114, 174.87078515794573),
    ("KFC \n Ratings: 2.9 / 5", -36.9003865591953, 174.89939711340074),
    ("Porterhouse Grill \n Ratings: 4.3 / 5", -36.912464364020884, 174.8723767088602)
]

# Creating a dictionary with restaurant names as keys and coordinates (latitude, longitude) as values
fastf_dict = {name: (lat, lon) for name, lat, lon in fastf_locs}

# Print the first 4 restaurants (original order)
first_four = list(fastf_dict.items())[:4]
print("First print (original order):")
for name, coords in first_four:
    print(f"Restaurant: {name}\nCoordinates: {coords}\n")

# Shuffle the dictionary items
shuffled_items = list(fastf_dict.items())  # Convert dictionary items to a list
random.shuffle(shuffled_items)  # Shuffle the list

# Print the shuffled list (first 4 restaurants)
print("Shuffled order:")
for name, coords in shuffled_items[:4]:  # Printing only 4 
    print(f"Restaurant: {name}\nCoordinates: {coords}\n")
