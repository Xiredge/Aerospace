from django.http import HttpResponse
import asyncio
from .get_json import fetch_data
from .data_storage import *
from .get_summary import get_summary
from .get_data import get_data
from .data_storage import *
from .read_chat import read_chat

def homepage(request):
    data = asyncio.run(fetch_data("https://www.simcompanies.com/api/v2/companies/buildings/38184904/sales-orders/"))
    store_data(data, "json.json")
    info = read_data("json.json")

    products = {}

    get_data(products, read_data("json.json"))
    get_summary(products)
    return HttpResponse(info)