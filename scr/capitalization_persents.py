def compound(amount, year_perсent, month_count):
    month_percent = year_perсent / 12
    for i in range(month_count):
        inc = amount / 100 * month_percent
        amount += inc
    return amount


def compound_efficient(amount, year_perсent, month_count):
    month_perсent = year_perсent / 12
    return amount * (1 + month_perсent / 100) ** month_count


print(compound(100000, 10, 12))
print(compound_efficient(100000, 10, 12))