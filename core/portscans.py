import asyncio

async def check_port(host, port):
    try:
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(host, port),
            timeout=1
        )

        writer.close()
        await writer.wait_closed()

        return port

    except:
        return None

async def scan_ports(host, ports):
    tasks = [check_port(host, port) for port in ports]

    results = await asyncio.gather(*tasks)

    return [port for port in results if port]