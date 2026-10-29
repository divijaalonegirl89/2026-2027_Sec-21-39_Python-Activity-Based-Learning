students =[
    ["Rahul", 85, 70, 80, 150000],
    ["Priya", 90, 80, 90, 100000],
    ["Arun", 75, 60, 85, 120000],
    ["Sneha", 90, 80, 95, 90000]
]
eligible = []
for s in students:
    name, marks, subject, attendance, income = s

    if marks >= 80 and subject >= 40 and attendance >= 75 and income <= 200000:
        eligible.append(s)
eligible.sort(key=lambda x: (-x[1], -x[3], x[4]))

print("Scholarship Eligible Students")

for s in eligible:
    print(s[0], s[1]) 