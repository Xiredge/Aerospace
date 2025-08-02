from django.http import HttpResponse
import asyncio
from .get_json import fetch_data
from .data_storage import *

def homepage(request):
    data = asyncio.run(fetch_data("https://www.simcompanies.com/api/v2/companies/buildings/38184904/sales-orders/"))
    store_data(data, "json.json")
    info = read_data("json.json")
    return HttpResponse(info)