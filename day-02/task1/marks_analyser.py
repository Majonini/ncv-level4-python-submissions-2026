def is_valid_mark(text):
    return text.isdigit() and int(text) <= 100
 
def read_marks():
    marks = []
    text = input("Enter a mark (0-100) or x to finish: ")
    while text != "x":
        if is_valid_mark(text):
            marks.append(int(text))
        else:
            print("Invalid mark ignored.")
        text = input("Enter a mark (0-100) or x to finish: ")
    return marks
def total_of(marks):
    total = 0
    for m in marks:
        total = total + m
    return total
 
def average_of(marks):
    return total_of(marks) / len(marks)
 
def highest_of(marks):
    highest = marks[0]
    for m in marks:
        if m > highest:
            highest = m
    return highest
 
def lowest_of(marks):
    lowest = marks[0]
    for m in marks:
        if m < lowest:
            lowest = m
    return lowest
BANDS = ["Outstanding", "Highly competent", "Competent",
         "Not yet competent", "Not achieved"]
 
def band_of(mark):
    if mark >= 80:
        return "Outstanding"
    elif mark >= 70:
        return "Highly competent"
    elif mark >= 50:
        return "Competent"
    elif mark >= 40:
        return "Not yet competent"
    else:
        return "Not achieved"
 
def count_bands(marks):
    counts = {}
    for name in BANDS:
        counts[name] = 0
    for m in marks:
        name = band_of(m)
        counts[name] = counts[name] + 1
    return counts
def print_report(marks):
    counts = count_bands(marks)
    low = counts["Not yet competent"] + counts["Not achieved"]
    percent = (len(marks) - low) / len(marks) * 100
    print()
    print("===== CLASS MARKS REPORT =====")
    print(f"Learners : {len(marks)}")
    print(f"Average  : {average_of(marks):.1f}")
    print(f"Highest  : {highest_of(marks)}")
    print(f"Lowest   : {lowest_of(marks)}")
    print("-" * 30)
    for name in BANDS:
        print(f"{name:<18}{counts[name]:>3}")
    print("-" * 30)
    print(f"Competent or better: {percent:.0f}%")
def main():
    marks = read_marks()
    if len(marks) == 0:
        print("No marks captured.")
    else:
        print_report(marks)
 
main()
