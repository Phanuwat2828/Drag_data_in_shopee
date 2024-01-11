const puppeteer = require('puppeteer');

(async () => {
  // เปิดบราวเซอร์
  const browser = await puppeteer.launch();

  // เปิดหน้าใหม่
  const page = await browser.newPage();

  // ไปที่ URL ของเว็บที่ต้องการดึงข้อมูล
  await page.goto('https://shopee.co.th/%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%94%E0%B8%B1%E0%B8%9A-cat.11044954?page=');

  // รอให้หน้าเว็บโหลดเสร็จสมบูรณ์
  await page.waitForSelector('body');

  // ดึงข้อมูลจากหน้าเว็บ
  const data = await page.evaluate(() => {
    // ใส่โค้ด JavaScript เพื่อดึงข้อมูล
    // ตัวอย่าง: ดึงข้อมูลจาก element ที่มี id เป็น "exampleElement"
    return document.getElementById('div').innerText;
  });

  // แสดงผลลัพธ์
  console.log('Data:', data);
  

  // ปิดบราวเซอร์
  await browser.close();
})();