import requests
from bs4 import BeautifulSoup

class GetProductData:
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept-Language": "en-GB,en;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Referer": "https://google.com",
            "Connection": "keep-alive",
        }

        response = self.session.get(url, headers=self.headers)

        if response.status_code != 200:
            raise Exception("Failed to fetch page")

        if "captcha" in response.text.lower():
            raise Exception("Blocked by Amazon")

        self.html_data = BeautifulSoup(response.text, "html.parser")

    def parse_price_data(self):
        try:
            price = self.html_data.select_one('.a-price .a-offscreen')
            
            return float(price.text.replace('£', '').replace(',', ''))

        except:
            return None

    def parse_item_name(self):
        title = self.html_data.select_one('#productTitle')
        return title.text.strip() if title else None


product = GetProductData("https://www.amazon.co.uk/PlayStation-PS5-Pro-5-Console/dp/B0FR94FV8J/ref=sr_1_4?_encoding=UTF8&brr=1&content-id=amzn1.sym.cc5a8121-5dd2-4b00-be77-8ccc7730d8ef&dib=eyJ2IjoiMSJ9.MyD1pCDSo5QOHiScCzOOiI0ylZAK6NBmTbtx0C-dT_0qWquwqd7TkFUe-L9hY2rdPq1set0-NjiZy_E1J_Z2OrbBtMA4ph6FmOAdQ_SSH8kIPSYKTpFB3pN2bGqZ4UCgVymp51XURSLHySJ2XfQ_HOdPZaDEfe8hTon3fbtuGrsOzfhxUCj5eFuRN2P3fwsdn28xlESVeFH0_aFXhAVqlOtStqYCuoGCsKwOk3WeF-8.MJl4e-JPQ_LdReySIuG9a_Bxp8nilu_C5BLe8Ba3QM4&dib_tag=se&pd_rd_r=685b0165-3ead-45b4-9bab-7247dddc1db6&pd_rd_w=V4sQS&pd_rd_wg=h5tjM&qid=1775768596&rd=1&s=videogames&sr=1-4")

print(product.parse_item_name())
print(product.parse_price_data())