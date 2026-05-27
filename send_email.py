import smtplib
import product_data
from dotenv import load_dotenv
load_dotenv()
import os

TARGET_PRICE = 800
price = product_data.product.parse_price_data()
try:
    print(f"Product: {product_data.product.parse_item_name()}")
    print(f"Current price: £{price}")
    print(f"Target price: £{TARGET_PRICE}")
    if price <= TARGET_PRICE:
        with smtplib.SMTP(host="smtp.gmail.com",port=587) as con:
            con.starttls()
            msg = f'Subject:Amazon Price Bot!\n\nThis a Price drop alert!\n\nItem : {product_data.product.parse_item_name()}\n\nNew price : {product_data.product.parse_price_data()}￡\n\nBuy now: {product_data.PRODUCT_URL}'
            sender_email = os.getenv('SENDER_EMAIL')
            sender_pass = os.getenv('SENDER_EMAIL_PASS')
            receiver = os.getenv('RECEIVER_EMAIL')
            con.login(user=sender_email,password=sender_pass)
            con.sendmail(msg=msg.encode("utf-8"),from_addr=sender_email,to_addrs=receiver)
            print("Alert sent!")
    else:
        print("Price still above target. No alert sent.")
except TypeError as e:
    print("Price Unavailable, check the product page.")