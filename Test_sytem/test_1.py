
# male (66.5+(13.75*wight))+(5*height)-(6.78*age)
# female (665+(9.56*wight))+(1.85*height)-(4.68*age);

sex =(input("Enter sex : "));
age = int(input("Enter Age : "));
weight = int(input("Enter Weight : "));
height = int(input("Enter Height : "));
factor = float(input("Enter Factor : "));
# น้อย Bmr 1.2 1-3weekBmr*1.375 3-5week bmr*1.55 6-7weekbmr*1.725 ใช้แรงมากbmr*1.9
if(sex =='m'):
    Tdee = ((66.5+(13.75*weight))+(5*height)-(6.78*age))*factor;
elif(sex=='F'):
    Tdee = ((665+(9.56*weight))+(1.85*height)-(4.68*age))*factor;

print(Tdee);

# 2618 

# 785 30% 654 25% 523 20% 656 25%


