import httpx
from bs4 import BeautifulSoup

async def extract_js_files(url):
    js_files = []

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url)

            soup = BeautifulSoup(response.text, "html.parser")

            scripts = soup.find_all("script")

            for script in scripts:
                src = script.get("src")

                if src:
                    js_files.append(src)

    except:
        pass

    return js_files