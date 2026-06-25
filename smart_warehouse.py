class SmartWarehouse:
    """
    A warehouse that enforces stock limits and automatically removes items when stock reaches zero.
    """

    def __init__(self, max_stock):
        self.max_stock = max_stock
        self.items = {}

    def __getitem__(self, item):
        if item not in self.items:
            raise KeyError(f"{item} not found in the warehouse")
        return self.items[item]

    def __setitem__(self, item, amount):
        if amount > self.max_stock:
            raise ValueError(
                f"Cannot exceed max stock limit of {self.max_stock} for {item}"
            )

        if amount == 0:
            if item in self.items:
                del self[item]
        else:
            self.items[item] = amount

    def __delitem__(self, item):
        if item not in self.items:
            raise KeyError(f"{item} not found in the warehouse")
        del self.items[item]

    def __contains__(self, item):
        return item in self.items


warehouse = SmartWarehouse(max_stock=100)

warehouse["laptops"] = 50
print(warehouse["laptops"])  # 50

warehouse["laptops"] += 40
print(warehouse["laptops"])  # 90

print("laptops" in warehouse)  # True

warehouse["laptops"] -= 90
print("laptops" in warehouse)  # False

try:
    warehouse["phones"] += 10
except KeyError as error:
    print(error)

try:
    warehouse["phones"] = 110
except ValueError as error:
    print(error)

warehouse["phones"] = 10
print(warehouse["phones"])  # 10

del warehouse["phones"]

try:
    warehouse["phones"] += 10
except KeyError as error:
    print(error)

try:
    del warehouse["phones"]
except KeyError as error:
    print(error)
