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
        "sessionid": ".eJxtkF9PwjAUxb9LX4Xl9h9t9yYaEyBqMBjC09KVDgjdhuuGDuN3twyQkPjSJvfc8zun_UaJ8VVWl1tboBhN5u8md8OKbsatHPv2S78t3p_d03o48pNmz3OzcFNM_OxjNHUj9zp-UXM9eZjl08PjoSZD1EOJbup10nhbJZtlQDKQDEt-q6TahMCjvHO6tZWPjlp0H47hWbrZX2u_DsvUEiFAM0MlZyqVNOOpYRk3GFRGU7CYMMiEJlk6UMLQDGPGtFqSjPN0SWSAnvK6akQqShnrIVPmO1203ZARotQAX4dJZbXLOw16qKtU-9CFAOF9UH0gM0xjIDElESgQgt8BxADXLKeLVaNXNpjCJ_eQ074O1M-y2qIYCz6QWOIBj-AsaVNvyiLx1vvjvbXtf3GMR1xyIvBf3MXQQUxZeGuaerO3F-D5vScY62PoYzULZq5ixiIqmJCX7j-_saui7w:1utQer:TIMY2XS_rXL8x9LScIhXnQB4wYmJqGQGGj7aDi8Gydk"}

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