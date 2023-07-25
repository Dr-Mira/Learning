def final_deposit_amount(*interest, amount=1000):
    total = amount
    for i in interest:
        total = total * ((int(i) / 100) + 1)
    return round(total, 2)
