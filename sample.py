def calculate_total(items):
    total = 0
    for i in range(len(items)):
        total=total+items[i]
    return total

print(calculate_total([10,20,30]))
