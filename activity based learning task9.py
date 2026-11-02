
r= float(input("exchange rate:"))
f=float(input("fee (%): "))
b= float(input("budget: "))

e={}
for i in range(3):
    c=input("category:")
    a= float(input("amount:"))
    e[c]=a*r*(1+f/100)

    total=sum(e.values())

    print("Total:", total)
    print("largest:", max(e, key=e.get))
    print("status:","within budget" if total<=b else "over budget")