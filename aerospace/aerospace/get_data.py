from product_type import product_type

def get_data(products, data):
    # A list that processes the data variable and extract the necessary data we need
    # Stores it inside a list as a dictionary
    # Sample JSON: {'id': 25428075, 'datetime': '2024-10-17T10:06:40.030368+00:00', 'searchCost': 39235,
    # 'resources': [{'amount': 3, 'price': 94142, 'kind': 96}, {'amount': 4, 'price': 42872, 'kind': 97}], 'qualityBonus': 2.273160085131345, 'speedBonus': 0},...}
    extracted_data = [
        {
            "id": item["id"],
            "searchCost": item["searchCost"],
            "kind": resource["kind"],
            "amount": resource["amount"],
            "price": resource["price"],
            "qualityBonus": round(item["qualityBonus"], 2) # ✅ Get from item, then rounds the number to nearest thousandth
        }
        for item in data if "resources" in item  # ✅ Ensure "resources" key exists
        for resource in item["resources"]  # ✅ Extract each resource
    ]
    # print(extracted_data)
    id_copy = extracted_data[0]["id"]

    total_net_income = 0
    total_gross_profit = 0

    for item in extracted_data:

        if id_copy == item["id"]:
            print(f"\nID: {item['id']}")
        else:
            print(f'_____________________________________')
            print(f"ID: {item['id']}")

        print("Kind: {:<25}\n\tAmount: {:>3}\n\tPrice: {:>3}\n\tQuality Bonus: {:>3}".format(
                product_type(item["kind"]),
                item["amount"],
                item["price"],
                item["qualityBonus"]))

        discount_rate = 0.15
        purchased_price = int(item["price"] - (item["price"] * discount_rate))

        print(f"Recommended Purchase Price: {purchased_price}")
        purchased_quality = 4
        print(f"Product Quality: {purchased_quality}")
        total_terms = item["price"] * item["amount"]
        print(f"Total Terms: {total_terms}")
        revenue = int(total_terms + (total_terms * ((item["qualityBonus"] / 100) * purchased_quality)))
        print(f"Revenue: {revenue}")
        gross_profit = revenue - (purchased_price * item["amount"])
        print(f"Gross Profit: {gross_profit}")
        net_income = gross_profit - item["searchCost"]
        print(f"Net Income: {net_income}")

        total_gross_profit += gross_profit
        total_net_income += net_income

        id_copy = item["id"]

        # Stores the product type
        product = product_type(item["kind"])

        # Checks if the product exists in the product dictionary, else create and initialize its corresponding data
        if product in products:
            products[product]["amount"] += item["amount"] # Adds the amount per product type
            products[product]["price"] += int(item["price"] * item["amount"]) # Gets the sum of price
            products[product]["totalPrice"] = products[product]["price"]  # Multiply the amount and price to get the total price per product type
            products[product]["qualityBonus"] += item["qualityBonus"]
            products[product]["typeCount"] += 1
        else:
            products[product] = {"amount": item["amount"], "price": (item["price"] * item["amount"]), "totalPrice" : item["price"], "qualityBonus" : item["qualityBonus"], "typeCount" : 1}
    # return products
    print(f"\nTotal Gross Profit: {total_gross_profit}")
    print(f"Total Net Income: {total_net_income}")

if __name__ == "__main__":
    print(product_type(100))