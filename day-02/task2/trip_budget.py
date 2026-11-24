CATEGORIES = {
    "f": "Food",
    "t": "Transport",
    "s": "Stationery",
    "a": "Accommodation"
}


def read_transactions():
    totals = {
        "Food": 0,
        "Transport": 0,
        "Stationery": 0,
        "Accommodation": 0
    }

    rejected = 0

    code = input("Category (f/t/s/a) or x to finish: ").lower()

    while code != "x":
        if code in CATEGORIES:
            amount = input("Amount in rand: ")

            if amount.isdigit() and 0 < int(amount) <= 5000:
                name = CATEGORIES[code]
                totals[name] = totals[name] + int(amount)

            else:
                print("Rejected: amount must be a whole number between R1 and R5000.")
                rejected = rejected + 1

        else:
            print("Rejected: unknown category.")
            rejected = rejected + 1

        code = input("Category (f/t/s/a) or x to finish: ").lower()

    return totals, rejected


def print_totals(totals, rejected):
    grand = 0

    print()
    print("===== TRIP BUDGET =====")

    for name in totals:
        print(f"{name:<12}R{totals[name]:>6}")
        grand = grand + totals[name]

    print("-" * 20)
    print(f"{'Total':<12}R{grand:>6}")
    print(f"Rejected entries: {rejected}")


totals, rejected = read_transactions()
print_totals(totals, rejected)