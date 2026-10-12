"""
Loyalty Points

A coffee shop awards points on every purchase. This program takes a
day's purchases and works out where everybody stands at closing time.
"""

BRONZE_THRESHOLD = 100
SILVER_THRESHOLD = 200
GOLD_THRESHOLD = 250
people_in_silver = 0
people_in_bronze = 0
people_in_gold = 0
people_in_standard = 0

points = {
    "alice": 120,
    "bob": 40,
    "siobhan": 195,
    "gold_man": 250
}

purchases = [
    ("alice", 30),
    ("chen", 15),
    ("bob", 60),
    ("alice", 10),
    ("siobhan", 12)
]


def award_points(points, purchases):
    for name, amount in purchases:
        if amount >= 50:
         points[name] = points.get(name, 0) + (amount * 2)
        else:
         points[name] = points.get(name, 0) + amount  


def tier(total):
    global people_in_silver, people_in_bronze, people_in_standard, people_in_gold
    if total >= GOLD_THRESHOLD:
        people_in_gold += 1
        return "Gold"
    elif total >= SILVER_THRESHOLD:
        people_in_silver += 1
        return "Silver"
    elif total >= BRONZE_THRESHOLD:
        people_in_bronze += 1
        return "Bronze"
    else:
        people_in_standard += 1
        return "Standard"


print(f"Customers at open: {len(points)}")

award_points(points, purchases)

print(f"Customers at close: {len(points)}")
print("End of day standings:")
for name, total in points.items():
    print(f"  {name}: {total} points, {tier(total)}")

print(f" {people_in_gold} in gold teir, {people_in_silver} in silver tier, {people_in_bronze} in bronze tier, {people_in_standard} in standard tier.")

