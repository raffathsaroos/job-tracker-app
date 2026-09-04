fruits = [
    {
        "name"   : "apple",
        "country": "canada",
        "taste"  : "sweet",
        "price"  : 120000
    },
    { 
        "name"   : "orange ",
        "country": "England",
        "taste"  : "sour",
        "price"  : 110000
    }
]

print("=== JOB APPLICATION TRACKER ===")


for index, fruit in enumerate(fruits, start = 1):
    print(f"\nJob #{index}:")
    print(f"  fruit   : {fruit['name']}")
    print(f"  Role    : {fruit['country']}")
    print(f"  Status  : {fruit['taste']}")
    print(f"  Price   : ${fruit['price']}")

print("\n===============================")