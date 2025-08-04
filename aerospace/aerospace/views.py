from django.http import HttpResponse
from django.shortcuts import render
import asyncio
from .get_json import fetch_data
from .data_storage import *
from .get_summary import get_summary
from .get_data import get_data
from .data_storage import *
from .read_chat import read_chat

def homepage(request):
    data = asyncio.run(fetch_data("https://www.simcompanies.com/api/v2/companies/buildings/38184904/sales-orders/"))
    data += asyncio.run(fetch_data("https://www.simcompanies.com/api/v2/companies/buildings/38321052/sales-orders/"))
    data += asyncio.run(fetch_data("https://www.simcompanies.com/api/v2/companies/buildings/38315475/sales-orders/"))

    store_data(data, "json.json")
    info = read_data("json.json")
    sales_data = get_data(info)
    
    total_gross_income = 0
    total_net_income = 0
    total_SEP = 0
    total_JUM = 0
    total_SOR = 0
    total_BFR = 0
    total_LUX = 0
    total_SAT = 0

    for item in sales_data:
        if "net_income" and "gross_profit" in item:
            total_net_income += item["net_income"]
            total_gross_income += item["gross_profit"]
        if "kind" in item:
            if "Single engine plane" == item["kind"]:
                total_SEP += item["amount"]
            elif "Jumbo jet" == item["kind"]:
                total_JUM += item["amount"]
            elif "Sub-orbital rocket" == item["kind"]:
                total_SOR += item["amount"]
            elif "BFR" == item["kind"]:
                total_BFR += item["amount"]
            elif "Luxury jet" == item["kind"]:
                total_LUX += item["amount"]
            elif "Satellite" == item["kind"]:
                total_SAT += item["amount"]
 
    #get_summary(products)
    return render(request, "home.html", {
        "products": sales_data, 
        "total_net_income": total_net_income,
        "total_gross_income": total_gross_income,
        "total_SEP": total_SEP,
        "total_JUM": total_JUM,
        "total_SOR": total_SOR,
        "total_BFR": total_BFR,
        "total_LUX": total_LUX,
        "total_SAT": total_SAT,
        })