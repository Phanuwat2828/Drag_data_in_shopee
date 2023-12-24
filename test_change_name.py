

import requests
from bs4 import BeautifulSoup

url = 'https://shopee.co.th/%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%87%E0%B8%B2%E0%B8%A1%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B9%83%E0%B8%8A%E0%B9%89%E0%B8%AA%E0%B9%88%E0%B8%A7%E0%B8%99%E0%B8%95%E0%B8%B1%E0%B8%A7-cat.11044959?page=0';
# ส่งคำขอและดึง HTML content
page = requests.get(url)
# สร้าง BeautifulSoup object
soup = BeautifulSoup(page.text,'html')

# ดึงลิงก์ (href) จาก <a> tag ที่อยู่ในตำแหน่งที่คุณต้องการ
# target_link = soup.find_all('div',class_ = 'shopee-category-list__body')
soup.find_all('div', class_ = 'shopee-category-list__body');
print(soup)