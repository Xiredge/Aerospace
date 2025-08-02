from get_quality import get_quality
from get_emoji import get_emoji

def get_summary(product):
    show_summary = str(input("Show summary: (Y/N)"))

    if show_summary == "Y" or show_summary == "y":

        print(f'\n\n\n\n\n_____________________________________')
        print("\n\n\t  ***Summary  of Products***")

        # Create a string variable to store the recommended items to purchase for the user
        buying_list = ""

        for item in product:
            print(f'\n_____________________________________')
            print(f'Product: {item}')
            print(f'\tAmount: {product[item]["amount"]}')

            average_price = int(product[item]["price"] / (product[item]["amount"]))

            print(f'\tAverage Price: {average_price}')
            print(f'\tTotal Price: {product[item]["totalPrice"]}')

            # Stores how much discount the user wants, and calculates at what price the user should buy each product type
            cog_discount = 0.15
            cog = average_price - (average_price * cog_discount)

            print(f'\n\tRecommended Purchase Price: {int(round(cog, -3))}')
            print(f'\n\tAverage Quality:  {round(product[item]["qualityBonus"] / product[item]["typeCount"], 2)}')
            print(f'\tQuality Range: {get_quality(product[item]["qualityBonus"])}')

            # Adds each item to the buying_list variable
            buying_list +=  get_emoji(str(item))+ " " + str(product[item]["amount"]) + " for $" + str(int(round(cog, -3))) + "\n"

        print(f"\t---Buying---\n{buying_list}")