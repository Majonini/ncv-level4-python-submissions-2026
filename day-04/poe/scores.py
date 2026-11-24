def read_scores(filename):
    scores = {}
    with open(filename) as f:
        for line in f:
            text = line.strip()
            if text != "":
                name, mark = text.split(",")
                if name not in scores:
                    scores[name] = []
                scores[name].append(int(mark))
    return scores
 
def best_of(scores):
    best = ""
    best_mark = -1
    for name in scores:
        for mark in scores[name]:
            if mark > best_mark:
                best_mark = mark
                best = name
    return best, best_mark
 
scores = read_scores("scores.csv")
for name in scores:
    print(f"{name:<8}{scores[name]}")
print("Best:", best_of(scores))
