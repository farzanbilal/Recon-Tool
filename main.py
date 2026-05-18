import asyncio
import json
from rich.console import Console

from core.subdomains import enumerate_subdomains
from core.portscans import scan_ports
from core.httpprobe import probe_http
from core.headers import analyze_headers
from core.jsfinder import extract_js_files
from core.screenshots import capture_screenshot
from core.report import save_report

console = Console()

COMMON_PORTS = [
    21,22,25,53,80,110,111,135,
    139,143,443,445,993,995,
    1723,3306,3389,5900,8080,8443
]

async def process_host(host):
    result = {}

    console.print(f"[cyan][*] Scanning {host}[/cyan]")

    ports = await scan_ports(host, COMMON_PORTS)
    result["open_ports"] = ports

    http_data = await probe_http(host)
    result["http"] = http_data

    if http_data:
        headers = analyze_headers(http_data.get("headers", {}))
        result["security_headers"] = headers

        js_files = await extract_js_files(http_data.get("url"))
        result["js_files"] = js_files

        await capture_screenshot(http_data.get("url"), host)

    return result

async def main(domain):
    final_report = {}

    console.print(f"[green][+] Enumerating subdomains for {domain}[/green]")

    subdomains = await enumerate_subdomains(domain)

    final_report["subdomains"] = {}

    tasks = []

    for sub in subdomains:
        tasks.append(process_host(sub))

    results = await asyncio.gather(*tasks)

    for sub, res in zip(subdomains, results):
        final_report["subdomains"][sub] = res

    save_report(domain, final_report)

    console.print("[bold green][+] Scan completed[/bold green]")

if __name__ == "__main__":
    domain = input("Enter target domain: ")
    asyncio.run(main(domain))