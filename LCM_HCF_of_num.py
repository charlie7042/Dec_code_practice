num1=int(input("Enter first num :"))
num2=int(input("Enter second num :"))

# LCM 
i=0
if num1>num2:
    max=num1
elif num2>num1:
    max=num2
else:
    print("wrong number typed")

while True:
    i+=1
    lcm=max*i
    if lcm%num1==0 and lcm%num2==0:
        lcm=max*i
        print(f"LCM of numbers {num1} , {num2} is ({lcm}) ")
        break
# HCF
if num1>num2:
    min=num2
elif num2>num1:
    min=num1
else:
    print("wrong number typed")
a=0
while True:
    hcf=min-a
    a+=1
    if num1%hcf==0 and num2%hcf==0:
        print(f"HCF of numbers {num1} , {num2} is ({hcf}) ")
        break