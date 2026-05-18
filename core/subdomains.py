import httpx
import json

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

async def enumerate_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"

    subdomains = set()

    try:
        async with httpx.AsyncClient(
            timeout=30,
            headers=HEADERS,
            verify=False
        ) as client:

            response = await client.get(url)

            print(f"[DEBUG] Status Code: {response.status_code}")

            if response.status_code != 200:
                return []

            try:
                data = response.json()

            except:
                print("[DEBUG] JSON Parsing Failed")
                print(response.text[:500])
                return []

            for item in data:

                name_value = item.get("name_value")

                if not name_value:
                    continue

                for sub in name_value.split("\n"):

                    sub = sub.strip().lower()

                    if "*" in sub:
                        continue

                    if domain in sub:
                        subdomains.add(sub)

    except Exception as e:
        print(f"[ERROR] {e}")

    return sorted(list(subdomains))