import subprocess

def change_ip_address(interface, new_ip):
    try:
        # เปลี่ยน IP address โดยใช้ netsh command
        subprocess.run(['netsh', 'interface', 'ip', 'set', 'address', interface, 'static', new_ip])
        
        print(f"เปลี่ยน IP address ของ {interface} เป็น {new_ip} สำเร็จแล้ว")
    except Exception as e:
        print("เกิดข้อผิดพลาดในการเปลี่ยน IP address:", e)

# เรียกใช้งานฟังก์ชันเพื่อเปลี่ยน IP address
interface_name = 'Ethernet'  # ระบุชื่อ interface ที่ต้องการเปลี่ยน IP address
new_ip_address = '192.168.1.10'  # ระบุ IP address ใหม่ที่ต้องการกำหนด
change_ip_address(interface_name, new_ip_address)
