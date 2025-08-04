from .product_type import product_type
from .data_storage import read_data

def get_data(data):
    # A list that processes the data variable and extract the necessary data we need
    # Stores it inside a list as a dictionary
    # Sample JSON: {'id': 25428075, 'datetime': '2024-10-17T10:06:40.030368+00:00', 'searchCost': 39235,
    # 'resources': [{'amount': 3, 'price': 94142, 'kind': 96}, {'amount': 4, 'price': 42872, 'kind': 97}], 'qualityBonus': 2.273160085131345, 'speedBonus': 0},...}
    extracted_data = []
   
    #total = 0
    for item in data:
        if "resources" in item:
            for resource in item["resources"]:
                sell_price = resource["price"]
                amount = resource["amount"]
                quality = item["qualityBonus"]
                purchased_price = int(sell_price - (sell_price * 0.15))
                total_terms = sell_price * amount
                revenue = total_terms + (total_terms * ((quality / 100) * 4))
                gross_profit = revenue - (purchased_price * resource["amount"])
                net_income = gross_profit - item["searchCost"]
                #total += net_income
 
                extracted_data.append({
                    "id": item["id"],
                    "searchCost": item["searchCost"],
                    "kind": product_type(resource["kind"]),
                    "amount": amount,
                    "sell_price": sell_price,
                    "qualityBonus": round(quality, 2),
                    "purchased_price": purchased_price,
                    "total_terms": total_terms,
                    "revenue": int(revenue),
                    "gross_profit": round(gross_profit),
                    "net_income": round(net_income),
                })

    #extracted_data.append({"total_net_income": total})

    return extracted_data

if __name__ == "__main__":
    print(product_type(100))