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
    sales_data = get_data({}, info)
    total_gross_income = 0
    total_net_income = 0

    for item in sales_data:
        if "net_income" and "gross_profit" in item:
            total_net_income += item["net_income"]
            total_gross_income += item["gross_profit"]
 
    #get_summary(products)
    return render(request, "home.html", {
        "products": sales_data, 
        "total_net_income": total_net_income,
        "total_gross_income": total_gross_income,
        })