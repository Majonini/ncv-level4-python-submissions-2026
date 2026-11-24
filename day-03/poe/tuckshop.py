items = {"pie": 0, "juice": 1, "chips": 2}
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
sales = [[12, 15, 9, 14, 20],
         [8, 11, 7, 10, 16],
         [5, 6, 9, 4, 12]]
 
def item_total(sales, row):
    total = 0
    for value in sales[row]:
        total = total + value
    return total
 
def day_total(sales, col):
    total = 0
    for row in sales:
        total = total + row[col]
    return total
 
def best_day(sales):
    best = 0
    for col in range(1, len(sales[0])):
        if day_total(sales, col) > day_total(sales, best):
            best = col
    return best
 
for name in items:
    print(f"{name:<6}{item_total(sales, items[name]):>4}")
print("Best day:", days[best_day(sales)], day_total(sales, best_day(sales)))

def check(name, actual, expected):
    if actual == expected:
        print("PASS", name)
    else:
        print("FAIL", name, "expected", expected, "got", actual)
 
check("rows", len(sales), 3)
check("pie total", item_total(sales, items["pie"]), 70)
check("juice total", item_total(sales, items["juice"]), 52)
check("friday total", day_total(sales, 4), 48)
check("best day", days[best_day(sales)], "Fri")
