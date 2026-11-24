# NCV Level 4 | Day 4 Files Strings Batch | example: p_all
# Type it in Thonny, run it, then change one thing.
def read_lines(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            text = line.strip()
            if text != "":
                lines.append(text)
    return lines

def parse_marks(text):
    marks = []
    for piece in text.split(";"):
        marks.append(int(piece))
    return marks

def parse_line(text):
    parts = text.split(",")
    return parts[0], parts[1].strip(), parse_marks(parts[2])

def check_line(text):
    parts = text.split(",")
    if len(parts) != 3:
        return "expected 3 fields"
    if not (parts[0].isdigit() and len(parts[0]) == 7):
        return "bad student number"
    if parts[1].strip() == "":
        return "missing name"
    for piece in parts[2].split(";"):
        if not piece.isdigit():
            return "mark is not a number"
        if int(piece) > 100:
            return "mark above 100"
    return ""

def load_register(filename):
    learners = {}
    errors = []
    line_no = 0
    for text in read_lines(filename):
        line_no = line_no + 1
        message = check_line(text)
        if message == "":
            number, name, marks = parse_line(text)
            if number in learners:
                message = "duplicate student number"
            else:
                learners[number] = {"name": name, "marks": marks}
        if message != "":
            errors.append((line_no, message, text))
    return learners, errors

def average_of(values):
    total = 0
    for v in values:
        total = total + v
    return total / len(values)

def ranking(learners):
    rows = []
    for number in learners:
        rows.append((average_of(learners[number]["marks"]), number))
    n = len(rows)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if rows[j][0] < rows[j + 1][0]:
                rows[j], rows[j + 1] = rows[j + 1], rows[j]
    return rows

def report_lines(learners):
    lines = ["Rank  Number    Name          Average"]
    rows = ranking(learners)
    for position in range(len(rows)):
        avg, number = rows[position]
        name = learners[number]["name"]
        lines.append(f"{position + 1:<6}{number:<10}{name:<14}{avg:>6.1f}")
    return lines

def write_lines(filename, lines):
    with open(filename, "w") as f:
        for line in lines:
            f.write(line + "\n")

def error_lines(errors):
    lines = []
    for line_no, message, text in errors:
        lines.append(f"line {line_no}: {message}: {text}")
    return lines

def save_register(learners, filename):
    lines = []
    for number in learners:
        marks_text = ""
        for mark in learners[number]["marks"]:
            if marks_text != "":
                marks_text = marks_text + ";"
            marks_text = marks_text + str(mark)
        lines.append(number + "," + learners[number]["name"] + "," + marks_text)
    write_lines(filename, lines)

def main():
    try:
        learners, errors = load_register("learners.txt")
    except FileNotFoundError:
        print("learners.txt not found. Check the folder.")
        return
    print("Loaded:", len(learners), "Rejected:", len(errors))
    write_lines("report.txt", report_lines(learners))
    write_lines("errors.log", error_lines(errors))
    save_register(learners, "clean.txt")
    again, problems = load_register("clean.txt")
    print("Round trip same:", again == learners, len(problems))
    for line in report_lines(learners):
        print(line)

main()
