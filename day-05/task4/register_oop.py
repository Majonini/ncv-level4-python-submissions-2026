# NCV Level 4 | Day 5 OOP Integration PoE | example: q_all
# Type it in Thonny, run it, then change one thing.
def read_lines(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            text = line.strip()
            if text != "":
                lines.append(text)
    return lines

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

def write_lines(filename, lines):
    with open(filename, "w") as f:
        for line in lines:
            f.write(line + "\n")

class Learner:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self._marks = []

    def add_mark(self, mark):
        if mark < 0 or mark > 100:
            return False
        self._marks.append(mark)
        return True

    def get_marks(self):
        return self._marks[:]

    def average(self):
        if len(self._marks) == 0:
            return None
        total = 0
        for m in self._marks:
            total = total + m
        return total / len(self._marks)

    def __str__(self):
        return f"{self.number} {self.name} {self._marks}"

    def to_line(self):
        marks_text = ""
        for mark in self._marks:
            if marks_text != "":
                marks_text = marks_text + ";"
            marks_text = marks_text + str(mark)
        return self.number + "," + self.name + "," + marks_text

class Register:
    def __init__(self):
        self.learners = {}
        self.errors = []

    def add(self, learner):
        if learner.number in self.learners:
            return False
        self.learners[learner.number] = learner
        return True

    def count(self):
        return len(self.learners)

    def load(self, filename):
        line_no = 0
        for text in read_lines(filename):
            line_no = line_no + 1
            message = check_line(text)
            if message == "":
                parts = text.split(",")
                learner = Learner(parts[0], parts[1].strip())
                for piece in parts[2].split(";"):
                    learner.add_mark(int(piece))
                if not self.add(learner):
                    message = "duplicate student number"
            if message != "":
                self.errors.append((line_no, message, text))

    def ranking(self):
        rows = []
        for number in self.learners:
            rows.append((self.learners[number].average(), number))
        n = len(rows)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if rows[j][0] < rows[j + 1][0]:
                    rows[j], rows[j + 1] = rows[j + 1], rows[j]
        return rows

    def report_lines(self):
        lines = ["Rank  Number    Name          Average"]
        rows = self.ranking()
        for position in range(len(rows)):
            avg, number = rows[position]
            name = self.learners[number].name
            lines.append(f"{position + 1:<6}{number:<10}{name:<14}{avg:>6.1f}")
        return lines

    def save(self, filename):
        lines = []
        for number in self.learners:
            lines.append(self.learners[number].to_line())
        write_lines(filename, lines)

    def error_lines(self):
        lines = []
        for line_no, message, text in self.errors:
            lines.append(f"line {line_no}: {message}: {text}")
        return lines

def main():
    reg = Register()
    try:
        reg.load("learners.txt")
    except FileNotFoundError:
        print("learners.txt not found. Check the folder.")
        return
    print("Loaded:", reg.count(), "Rejected:", len(reg.errors))
    write_lines("report.txt", reg.report_lines())
    write_lines("errors.log", reg.error_lines())
    reg.save("clean.txt")
    again = Register()
    again.load("clean.txt")
    print("Round trip same:", again.report_lines() == reg.report_lines())
    for line in reg.report_lines():
        print(line)

main()
