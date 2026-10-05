from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from bs4 import BeautifulSoup

app = FastAPI()

# อนุญาตให้ HTML เรียกใช้งาน API ได้ (แก้เรื่อง CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/data")
def get_scraped_data():
    # 1. ดึง HTML จากเว็บเป้าหมาย
    url = "https://example.com"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    # 2. สกัดข้อมูลด้วย BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # ตัวอย่าง: ดึงชื่อหัวข้อทั้งหมด
    results = []
    for item in soup.select('h2'):
        results.append({"title": item.text.strip()})
        
    # 3. ส่งข้อมูลกลับไปเป็น JSON
    return {"data": results}