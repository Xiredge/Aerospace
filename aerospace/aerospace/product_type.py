# A dictionary of products
product_list = {
    1: "Power", 2: "Water", 3: "Apples", 4: "Oranges", 5: "Grapes", 6: "Grain",
    7: "Steak", 8: "Sausages", 9: "Eggs", 10: "Crude oil", 11: "Petrol", 12: "Diesel",
    13: "Transport", 14: "Minerals", 15: "Bauxite", 16: "Silicon", 17: "Chemicals",
    18: "Aluminium", 19: "Plastic", 20: "Processors", 21: "Electronic components", 22: "Batteries",
    23: "Displays", 24: "Smart phones", 25: "Tablets", 26: "Laptops", 27: "Monitors",
    28: "Televisions", 29: "Plant research", 30: "Energy research", 31: "Mining research",
    32: "Electronics research", 33: "Breeding research", 34: "Chemistry research", 35: "Software",
    40: "Cotton", 41: "Fabric", 42: "Iron ore", 43: "Steel", 44: "Sand", 45: "Glass",
    46: "Leather", 47: "On-board computer", 48: "Electric motor", 49: "Luxury car interior",
    50: "Basic interior", 51: "Car body", 52: "Combustion engine", 53: "Economy e-car",
    54: "Luxury e-car", 55: "Economy car", 56: "Luxury car", 57: "Truck", 58: "Automotive research",
    59: "Fashion research", 60: "Underwear", 61: "Gloves", 62: "Dress", 63: "Stiletto Heel",
    64: "Handbags", 65: "Sneakers", 66: "Seeds", 67: "Xmas crackers", 68: "Gold ore",
    69: "Golden bars", 70: "Luxury watch", 71: "Necklace", 72: "Sugarcane", 73: "Ethanol",
    74: "Methane", 75: "Carbon fibers", 76: "Carbon composite", 77: "Fuselage", 78: "Wing",
    79: "High grade e-comps", 80: "Flight computer", 81: "Coc.kpit", 82: "Attitude control",
    83: "Rocket fuel", 84: "Propellant tank", 85: "Solid fuel booster", 86: "Rocket engine",
    87: "Heat shield", 88: "Ion drive", 89: "Jet engine", 90: "Sub-orbital nd stage",
    91: "Sub-orbital rocket", 92: "Orbital booster", 93: "Starship", 94: "BFR", 95: "Jumbo jet",
    96: "Luxury jet", 97: "Single engine plane", 98: "Quadcopter", 99: "Satellite",
    100: "Aerospace research", 101: "Reinforced concrete", 102: "Bricks", 103: "Cement",
    104: "Clay", 105: "Limestone", 106: "Wood", 107: "Steel beams", 108: "Planks", 109: "Windows",
    110: "Tools", 111: "Construction units", 112: "Bulldozer", 113: "Materials research",
    114: "Robots", 115: "Cows", 116: "Pigs", 117: "Milk", 118: "Coffee beans", 119: "Coffee powder",
    120: "Vegetables", 121: "Bread", 122: "Cheese", 123: "Apple pie", 124: "Orange juice",
    125: "Apple cider", 126: "Ginger beer", 127: "Frozen pizza", 128: "Pasta", 129: "Hamburger",
    130: "Lasagna", 131: "Meat balls", 132: "Coc.ktails", 133: "Flour", 134: "Butter",
    135: "Sugar", 136: "Cocoa", 137: "Dough", 138: "Sauce", 139: "Fodder", 140: "Chocolate",
    141: "Vegetable oil", 142: "Salad", 143: "Samosa", 145: "Recipes"
}

# A function that returns the products
# Parameter: integer
# Returns a key of the dictionary
def product_type(product_number):
    if product_number  in product_list:
        return product_list[product_number]