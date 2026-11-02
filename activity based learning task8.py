
m=float(input("material cost:"))
l=float(input("labour cost:"))
w=float(input("wastage cost:"))
mc=float(input("machine cost:"))
s=float(input("selling price:"))
t=float(input("profit target:"))

cost = m + l + w + mc
profit = s - cost

print("Total Cost:", cost)
print("Profit:", profit)
print("Result:", "Achieved" if profit >= t else "Not Achieved")