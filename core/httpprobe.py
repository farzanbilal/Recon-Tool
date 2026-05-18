import httpx

async def probe_http(host):
    protocols = ["https://", "http://"]

    for proto in protocols:
        url = proto + host

        try:
            async with httpx.AsyncClient(follow_redirects=True, timeout=10) as client:
                response = await client.get(url)

                return {
                    "url": str(response.url),
                    "status": response.status_code,
                    "title": extract_title(response.text),
                    "server": response.headers.get("server"),
                    "headers": dict(response.headers)
                }

        except:
            pass

    return None


def extract_title(html):
    try:
        start = html.lower().find("<title>")
        end = html.lower().find("</title>")

        if start != -1 and end != -1:
            return html[start + 7:end].strip()

    except:
        pass

    return "No Title"