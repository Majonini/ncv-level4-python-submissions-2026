def show_menu():
    print()
    print("===== MARKS ANALYSER =====")
    print("1. Add a mark")
    print("2. Show statistics")
    print("3. Search for a mark")
    print("4. Show marks above average")
    print("5. Exit")


# Validate marks
def is_valid_mark(text):
    return text.isdigit() and 0 <= int(text) <= 100


# Calculate average
def average_of(marks):
    return sum(marks) / len(marks)


# Find highest mark
def highest_of(marks):
    return max(marks)


# Find lowest mark
def lowest_of(marks):
    return min(marks)


# Add a mark
def add_mark(marks):
    text = input("Mark (0-100): ")

    if is_valid_mark(text):
        marks.append(int(text))
        print("Added successfully.")
    else:
        print("Invalid mark. Enter a whole number between 0 and 100.")


# Show statistics
def show_stats(marks):
    if len(marks) == 0:
        print("No marks yet.")
        return

    print()
    print("===== MARK STATISTICS =====")
    print("Learners:", len(marks))
    print("Average :", round(average_of(marks), 1))
    print("Highest :", highest_of(marks))
    print("Lowest  :", lowest_of(marks))


# Search for a mark
def search_mark(marks):
    text = input("Mark to find (0-100): ")

    if not is_valid_mark(text):
        print("Invalid mark. Search cancelled.")
        return

    target = int(text)
    found = False
    position = -1

    for i in range(len(marks)):
        if marks[i] == target and not found:
            found = True
            position = i

    if found:
        print("Found at position", position + 1)
    else:
        print("Not found.")


# Show marks above average
def show_above_average(marks):
    if len(marks) == 0:
        print("No marks yet.")
        return

    average = average_of(marks)
    found = False

    print()
    print("===== MARKS ABOVE AVERAGE =====")
    print("Class average:", round(average, 1))

    for i in range(len(marks)):
        if marks[i] > average:
            print("Learner", i + 1, ":", marks[i])
            found = True

    if not found:
        print("No marks above average.")


# Main program
def main():
    marks = []
    choice = ""

    while choice != "5":
        show_menu()
        choice = input("Choice: ")

        if choice == "1":
            add_mark(marks)

        elif choice == "2":
            show_stats(marks)

        elif choice == "3":
            search_mark(marks)

        elif choice == "4":
            show_above_average(marks)

        elif choice == "5":
            print("Goodbye.")

        else:
            print("Invalid choice. Enter 1, 2, 3, 4 or 5.")


# Start program
main()