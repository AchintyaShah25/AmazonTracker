from bs4 import BeautifulSoup
import requests
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
accepted_language = "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7"
header = {
      "User-Agent": user_agent,
      "Accepted-Language": accepted_language
}
# URL = "https://www.amazon.in/Promotion-Buggati-Openable-Musical-Flashing/dp/B08KDPR3S8/ref=sr_1_2?keywords=buggati+cars&qid=1677416118&sprefix=bugg%2Caps%2C207&sr=8-2"
URL = "https://www.amazon.in/dp/B0BT58F8WM/ref=sspa_dk_detail_4?psc=1&pd_rd_i=B0BT58F8WM&pd_rd_w=7Jtxy&content-id=amzn1.sym.b3dfef88-30a1-490c-be36-e990ef384667&pf_rd_p=b3dfef88-30a1-490c-be36-e990ef384667&pf_rd_r=0MRW7XDTWH9MZE8AR6K8&pd_rd_wg=dnn8p&pd_rd_r=60a9bc97-37e7-417b-9692-b12ae09c913c&s=toys&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw"
response = requests.get(URL, headers=header)
response = response.text
soup = BeautifulSoup(response, "html.parser")
price = soup.find(name="span", class_="a-price-whole").getText()
price = price.replace(",","")
price = price.replace(".","")
price = int(price)
set_price = int(input("Enter Your Set Price:\n"))
if price<=set_price:
      print("Cop ASAP!!!!!")