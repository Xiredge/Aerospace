# A dictionary of products and their equivalent emoji number in game
product_list = {
    "Power": 1, "Water": 2, "Apples": 3, "Oranges": 4, "Grapes": 5, "Grain": 6,
    "Steak": 7, "Sausages": 8, "Eggs": 9, "Crude oil": 10, "Petrol": 11, "Diesel": 12,
    "Transport": 13, "Minerals": 14, "Bauxite": 15, "Silicon": 16, "Chemicals": 17,
    "Aluminium": 18, "Plastic": 19, "Processors": 20, "Electronic components": 21, "Batteries": 22,
    "Displays": 23, "Smart phones": 24, "Tablets": 25, "Laptops": 26, "Monitors": 27,
    "Televisions": 28, "Plant research": 29, "Energy research": 30, "Mining research": 31,
    "Electronics research": 32, "Breeding research": 33, "Chemistry research": 34, "Software": 35,
    "Cotton": 40, "Fabric": 41, "Iron ore": 42, "Steel": 43, "Sand": 44, "Glass": 45,
    "Leather": 46, "On-board computer": 47, "Electric motor": 48, "Luxury car interior": 49,
    "Basic interior": 50, "Car body": 51, "Combustion engine": 52, "Economy e-car": 53,
    "Luxury e-car": 54, "Economy car": 55, "Luxury car": 56, "Truck": 57, "Automotive research": 58,
    "Fashion research": 59, "Underwear": 60, "Gloves": 61, "Dress": 62, "Stiletto Heel": 63,
    "Handbags": 64, "Sneakers": 65, "Seeds": 66, "Xmas crackers": 67, "Gold ore": 68,
    "Golden bars": 69, "Luxury watch": 70, "Necklace": 71, "Sugarcane": 72, "Ethanol": 73,
    "Methane": 74, "Carbon fibers": 75, "Carbon composite": 76, "Fuselage": 77, "Wing": 78,
    "High grade e-comps": 79, "Flight computer": 80, "Cockpit": 81, "Attitude control": 82,
    "Rocket fuel": 83, "Propellant tank": 84, "Solid fuel booster": 85, "Rocket engine": 86,
    "Heat shield": 87, "Ion drive": 88, "Jet engine": 89, "Sub-orbital nd stage": 90,
    "Sub-orbital rocket": 91, "Orbital booster": 92, "Starship": 93, "BFR": 94, "Jumbo jet": 95,
    "Luxury jet": 96, "Single engine plane": 97, "Quadcopter": 98, "Satellite": 99,
    "Aerospace research": 100, "Reinforced concrete": 101, "Bricks": 102, "Cement": 103,
    "Clay": 104, "Limestone": 105, "Wood": 106, "Steel beams": 107, "Planks": 108, "Windows": 109,
    "Tools": 110, "Construction units": 111, "Bulldozer": 112, "Materials research": 113,
    "Robots": 114, "Cows": 115, "Pigs": 116, "Milk": 117, "Coffee beans": 118, "Coffee powder": 119,
    "Vegetables": 120, "Bread": 121, "Cheese": 122, "Apple pie": 123, "Orange juice": 124,
    "Apple cider": 125, "Ginger beer": 126, "Frozen pizza": 127, "Pasta": 128, "Hamburger": 129,
    "Lasagna": 130, "Meat balls": 131, "Cocktails": 132, "Flour": 133, "Butter": 134,
    "Sugar": 135, "Cocoa": 136, "Dough": 137, "Sauce": 138, "Fodder": 139, "Chocolate": 140,
    "Vegetable oil": 141, "Salad": 142, "Samosa": 143, "Recipes": 145
}

# A function that returns the emoji number
# Parameter: string
# Returns a string
def get_emoji(kind):
    if kind in product_list:
        emoji = ":re-" +  str(product_list[kind])  + ":"
        return emoji

if __name__ == "__main__":
    emojis = get_emoji("Electric motor")
    print(emojis)