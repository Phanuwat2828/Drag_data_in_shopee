


def Methode_Tax():
    while True :
        print("""
            ==========================================
            [I] Income Tax
            [E] Exit
            ==========================================
            """)
        Type = str(input("ป้อนสถาณะ : "))
        if Type == 'E':
            return
        
        Salary = float(input("\bป้อนเงินเดือน : "))
        money_help_add  = float(input("\bป้อนเงินลดหย่อนภาษีเพิ่มเติม : "))
        money_use = 100000; #ค่าใช้จ่าย
        money_help = 60000; #ลดหย่อนภาษี
        if Salary>=100000 :
            money_sumation = float(Salary*12)-money_use-money_help-money_help_add;
        else:
            money_sumation = float(Salary*12);
        Total_Money = 0; 
        Tax = 0;
        Tax_percent = 0;
        if money_sumation > 5000000:
            Tax_percent = 35;
        elif money_sumation > 2000000:
            Tax_percent = 30;
        elif money_sumation > 1000000:
            Tax_percent = 25;
        elif money_sumation > 750000:
            Tax_percent = 20;
        elif money_sumation > 500000:
            Tax_percent = 15;
        elif money_sumation > 300000:
            Tax_percent = 10;
        elif money_sumation > 150000:
            Tax_percent = 5;
        else:
            Tax_percent = 0;
        Total_Money = money_sumation*(Tax_percent/100);
        print("เงินสุทธิ : ",money_sumation," Bath");
        print("เงินภาษีสุทธิที่ต้องจ่าย : ",Total_Money," Bath");
        print("เงินเหลือสุทธิ : ",money_sumation-Total_Money," Bath");
        
Methode_Tax();