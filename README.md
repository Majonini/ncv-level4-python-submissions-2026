# NCV Technical Programming — Level 4 Python Submissions

**Lecturer Development Programme — Session 3: Advanced Python (NCV Level 4)**
**Dates:** Monday 16 November – Friday 20 November 2026

This repository is used **only** to submit your completed programming tasks.

> Complete each programming task locally, commit your changes and push them to your own GitHub fork. At the end of the five-day programme, submit one pull request to the facilitator's original repository. Your pull request does not need to be merged.

| Day | Date | Folder |
|---|---|---|
| Day 1 | Monday, 16 November 2026 | day-01 |
| Day 2 | Tuesday, 17 November 2026 | day-02 |
| Day 3 | Wednesday, 18 November 2026 | day-03 |
| Day 4 | Thursday, 19 November 2026 | day-04 |
| Day 5 | Friday, 20 November 2026 | day-05 |

## Where each step happens

| Step | Where |
|---|---|
| Fork the repository | GitHub website |
| Clone your fork | Terminal |
| Create task folders and write your programs | Terminal / Thonny |
| `git status` → `git add` → `git commit` → `git push` | Terminal |
| Submit the final pull request | GitHub website |

---

## 1. Fork this repository (GitHub website — once)

1. Sign in to **your own** GitHub account.
2. Open `https://github.com/fredre/ncv-level4-python-submissions-2026`.
3. Click **Fork** (top right).
4. Choose **your own account** as the owner, then click **Create fork**.
5. Check the address bar. It must show **your** majonini:
   `https://github.com/majonini/ncv-level4-python-submissions-2026`

## 2. Copy the clone URL from your fork

On **your fork** (not the original), click the green **Code** button, select **HTTPS** and copy the URL.

## 3. Clone your fork (terminal — once)

Replace `majonini` with your own GitHub majonini:

```bash
git clone https://github.com/majonini/ncv-level4-python-submissions-2026.git
```

## 4. Enter the local repository

```bash
cd ncv-level4-python-submissions-2026
```

## 5. Verify `origin`

```bash
git remote -v
git branch --show-current
```

`origin` must show **your** majonini, and the branch must be `main`. `origin` is the place your work is pushed to — your own fork. If it shows `fredre`, you cloned the wrong repository; ask the facilitator for help.

## 6. Create the task folder

The facilitator will announce the day and task. Example for Day 1, Task 1 (run from inside the repository folder):

```bash
mkdir -p day-01/task1
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force -Path "day-01/task1"
```

Task folders are named `task1`, `task2`, `task3`, … and numbering restarts each day. Do **not** create folders with your name.

## 7. Save your Python files in the task folder

Write your program in Thonny and save it directly into the task folder (**File → Save as…**), for example `day-01/task1/main.py`. Run it with **F5** to test it. Submit your `.py` files and any data files the program reads or writes (for example `.txt` or `.csv`), not the `__pycache__/` folder.

## 8. Check what changed — `git status`

```bash
git status
```

Your new files should appear under the correct `day-XX/taskN/` folder.

## 9. Stage the task — `git add`

```bash
git add day-01/task1/
git diff --cached --name-only
```

The second command lists exactly what will be committed. Avoid `git add .` — it may include files you did not intend to submit.

## 10. Commit — `git commit`

```bash
git commit -m "Day 1: Complete Task 1"
```

A commit saves your work in your **local** history only. It is not on GitHub yet.

## 11. Push — `git push`

```bash
git push origin main
```

This uploads your commits to your fork. Never type your GitHub account password into the terminal — sign in through the browser window or credential manager when prompted, or follow the facilitator's instructions.

## 12. Verify on GitHub

Open your fork in the browser, go to `day-01/task1/` and check that your files are there.

Repeat steps 6–12 for every task. **Do not fork or clone again.** Keep working in the same folder and on the `main` branch all week.

## 13. Final submission — one pull request (Day 5, GitHub website)

1. Run `git status` and `git push origin main` one last time.
2. Open **your fork** on GitHub.
3. Click **Contribute → Open pull request** (or **Pull requests → New pull request → compare across forks**).
4. Check the settings:
   - **base repository:** `fredre/ncv-level4-python-submissions-2026` — **base:** `main`
   - **head repository:** `majonini/ncv-level4-python-submissions-2026` — **compare:** `main`
5. Review the list of changed files.
6. Title: `NCV L4 Final Submission - majonini`, complete the template, then click **Create pull request**.
7. Copy the pull request URL and send it to the facilitator.

Keep your fork until the review is finished. Corrections can be committed and pushed to `main` in your fork — they update the same pull request automatically.

---

## Command reference

```bash
# Once
git clone https://github.com/majonini/ncv-level4-python-submissions-2026.git
cd ncv-level4-python-submissions-2026
git remote -v

# For every task (change the day and task number)
mkdir -p day-01/task1
git status
git add day-01/task1/
git diff --cached --name-only
git commit -m "Day 1: Complete Task 1"
git push origin main
```

**Day 2, Task 3 example:** `mkdir -p day-02/task3` → `git add day-02/task3/` → `git commit -m "Day 2: Complete Task 3"` → `git push origin main`
