import aiohttp

# Function for fetching and returning the JSON fetched
# Parameter: string
# Returns a string
async def fetch_data(url):

    cookies = {
        "csrftoken": "lTbf1ZbSWu0rgnrZTLkhHJsu2uQDmL7pYcX7nFit3qf9IWgT7vLql8ZQrmyMX4Lh",
        "amp_a5727e": "KcbP7TltBFrUk5VCkpIrsM...1iod12dvl.1iod1735c.6.6.c",
        "amp_a5727e_simcompanies.com": "KcbP7TltBFrUk5VCkpIrsM...1iod124eq.1iod17347.0.0.0",
        "last-exchange-resource-0": "1",
        "last-exchange-resource-1": "1",
        "sessionid": ".eJx1kdFP2zAQxv8Xv66N7uxzbOeNDsQQgkmAyspL5LgOLSlJFScd2cT_PjcUVbDtxZbuu_t9n8-_We5CW3ZN5WuWsfv1w3y3qK5eFpff5xfDTcpv4TQNV2cFfsNfDUBaNTP6iosHgavz2Wx3U9O9v6ZdOzT0dP2DTVhu-26V98G3-XoZkQSaUMuPSmFdNNzL240dfBuSvZacxGN2kD70r2xYxWbhuVJgyQktyRRalLJwVEqHYEpRgEdOUCrLyyI1yokSkciaJS-lLJZcR-ib3xiNayME0YS55nlr62EsEufGpHgs5q23m-dRgwkbI3UhZuHA5RT0FPgd6EzojFRCmkDAF4AM4Oi1sfVjbx99HIpLnrCNDV2k_mzaimWoJCEXRmECB8m6bt3UefAh7O_KD3_bmUxggopjerR7HxghrqmDd3233vl34OG9bzCaIkzR3MVhaTKiRChSWn7OHvqwjb_h91_1r_L_d8F15IkD7_UPBaG4jQ:1ui7mz:GIwX2bPKOKY-FdmbN4TwE1e9v6TSEBcHqMuHmR0d4Y4"}

    headers = {
        "User-Agent": "Mozilla/5.0"  # Mimic a real browser request
    }

    async with aiohttp.ClientSession(cookies=cookies, headers=headers) as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                print(f"Failed to fetch data. Status Code: {response.status}")
                print(await response.text())  # Debugging output