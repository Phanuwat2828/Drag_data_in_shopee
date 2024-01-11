import requests as req

# ไอดีสินค้าลูปแต่ละครั้ง ให้ไนท์ใช้ด้วย แต่ละครั้งที่ทำการอ่าน excel ทำการกำหนด id ให้และส่ง api มาบันทึกเลย
id_items_Byshopee = [
    {
        "id":"SHOP01",
        "about":"ความงามและของใช้ส่วนตัว"
    },
    {
        "id":"SHOP02",
        "about":"เสื้อฟ้าแฟชั่นผู้ชาย"
    },
    {
        "id":"SHOP03",
        "about":"กระเป๋า"
    },
    {
        "id":"SHOP04",
        "about":"รองเท้าผู้หญิง"
    },
    {
        "id":"SHOP05",
        "about":"นาฬิกาและแว่นตา"
    },
    {
        "id":"SHOP06",
        "about":"สื่อบันเทิงภายในบ้าน"
    },
    {
        "id":"SHOP07",
        "about":"เครื่องใช้ไฟฟ้าภายในบ้าน"
    },
    {
        "id":"SHOP08",
        "about":"กล้องและอุปกรณ์ภ่ายภาพ"
    },
    {
        "id":"SHOP09",
        "about":"ของเล่นเด็กสินค้าของแม่"
    },
    {
        "id":"SHOP10",
        "about":"กลุ่มผลิตภัณฑ์เพื่อสุขภาพ"
    },
    {
        "id":"SHOP11",
        "about":"เสื้อผ้าแฟชั่นผู้หญิง"
    },
    {
        "id":"SHOP12",
        "about":"รองเท้าผู้ชาย"
    },
    {
        "id":"SHOP13",
        "about":"เครื่องประดับ"
    },
    {
        "id":"SHOP14",
        "about":"เครื่องใช้ในบ้าน พวกที่นอน ตู้เสื้อผ้า"
    },
    {
        "id":"SHOP15",
        "about":"มือถือและอุปกรณ์เสริม"
    },
    {
        "id":"SHOP16",
        "about":"คอมพิวเตอร์และแล็ปท็อป"
    },
    {
        "id":"SHOP17",
        "about":"อาหารและเครื่องดื่ม"
    },
    {
        "id":"SHOP18",
        "about":"กีฬาและกิตกรรมกลางแจ้ง"
    },
    {
        "id":"SHOP19",
        "about":"เกมและอุกรณ์เสริม"
    },
    {
        "id":"SHOP20",
        "about":"อื่นๆ ยังไม่ได้กำหนด"
    },
]

url = ""
header = {
    "Content-Type":"application/x-www-form-urlencoded",
}
data = {
    "id":"F0001",
    "data":{
        "product":[],
        "price_product_2":[],
        "price_product_1":[],
        "image_product_1":[],
        "discount":[],
        "image_product_2":[],
        "data_product":[],
        "price_before":[],
        "Emoji":[],
        "sold":[],
        "place":[],
        "Recommended_shops":[]
    }
}
res = req.post("https://google.com/",data=data,headers=header)
print(res.status_code)

