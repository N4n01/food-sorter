RESTAURANTS = [
    ("Mango Rice", 4.2, 25),
    ("Pad Thai House", 4.8, 40),
    ("Chicken Rice", 4.6, 15),
    ("Som Tam Corner", 4.6, 25),
    ("Boat Noodles", 4.8, 30)
]

def by_rating(r):
    return (-r[1], r[2])

def by_time(r):
    return (r[2], -r[1])

opt = input("Sort by (rating/time): ").lower()

if opt == "rating":
    restaurants_sorted = sorted(RESTAURANTS, key=by_rating)
elif opt == "time":
    restaurants_sorted = sorted(RESTAURANTS, key=by_time)
else:
    print("Unknown option")
    restaurants_sorted = []

for i in range(len(restaurants_sorted)):
    r = restaurants_sorted[i]
    print(f"{i + 1}. {r[0]}, {r[1]} stars, {r[2]} min")