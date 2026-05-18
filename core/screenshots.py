from playwright.async_api import async_playwright
import os

async def capture_screenshot(url, host):
    os.makedirs("output/screenshots", exist_ok=True)

    filename = f"output/screenshots/{host}.png"

    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch()

            page = await browser.new_page()

            await page.goto(url, timeout=15000)

            await page.screenshot(path=filename)

            await browser.close()

    except:
        pass