# NCV Level 4 | Day 1 Foundations | example: final
# Type it in Thonny, run it, then change one thing.
# Marks analyser: final version (Day 1)
# Step 2: capture marks
marks = []
text = input("Enter a mark (0-100) or x to finish: ")
while text != "x":
    if text.isdigit() and int(text) <= 100:
        marks.append(int(text))
    else:
        print("Invalid mark ignored.")
    text = input("Enter a mark (0-100) or x to finish: ")

if len(marks) == 0:
    print("No marks captured.")
else:
    # Step 3: total and average
    total = 0
    for m in marks:
        total = total + m
    average = total / len(marks)

    # Step 4: highest and lowest
    highest = marks[0]
    lowest = marks[0]
    for m in marks:
        if m > highest:
            highest = m
        if m < lowest:
            lowest = m

    # Step 5: count learners per rating band
    bands = {"Outstanding": 0, "Highly competent": 0,
             "Competent": 0, "Not yet competent": 0,
             "Not achieved": 0}
    for m in marks:
        if m >= 80:
            bands["Outstanding"] = bands["Outstanding"] + 1
        elif m >= 70:
            bands["Highly competent"] = bands["Highly competent"] + 1
        elif m >= 50:
            bands["Competent"] = bands["Competent"] + 1
        elif m >= 40:
            bands["Not yet competent"] = bands["Not yet competent"] + 1
        else:
            bands["Not achieved"] = bands["Not achieved"] + 1

    # Step 6: formatted report
    print()
    print("===== CLASS MARKS REPORT =====")
    print(f"Learners : {len(marks)}")
    print(f"Average  : {average:.1f}")
    print(f"Highest  : {highest}")
    print(f"Lowest   : {lowest}")
    print("-" * 30)
    for name in bands:
        count = bands[name]
        print(f"{name:<18}{count:>3}")
    low = bands["Not yet competent"] + bands["Not achieved"]
    percent = (len(marks) - low) / len(marks) * 100
    print("-" * 30)
    print(f"Competent or better: {percent:.0f}%")
