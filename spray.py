import os
import random
from datetime import datetime, timedelta
import subprocess

# ================= CONFIG =================
REPO_PATH = "d:/python/other/git/activity-log"
BRANCH = "main"

START_DATE = datetime(2025, 1, 1)
END_DATE   = datetime(2025, 12, 31)

FILES = ["data.txt", "feature.py", "notes.md"]

MESSAGES = [
    "initial setup", "working on feature", "fixing bug", "refactoring code",
    "improving performance", "updating docs", "testing changes", "cleanup",
    "minor fix", "restructuring", "updating dependencies", "WIP",
    "resolving merge conflicts", "adding comments", "optimizing queries",
    "refactor project structure", "setup tests", "bump version"
]
# ==========================================

def run(cmd, env=None):
    subprocess.run(cmd, shell=True, check=True, cwd=REPO_PATH, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

os.chdir(REPO_PATH)
for f in FILES:
    if not os.path.exists(f):
        with open(f, "w", encoding="utf-8") as file:
            file.write("# init\n")

print(f"Planning 2025 Git Spray (Target exactly 440 commits)...")

# --- Pre-calculate the entire year's commit sequence ---
days = []
current_date = START_DATE
while current_date <= END_DATE:
    days.append(current_date)
    current_date += timedelta(days=1)

commit_counts = [0] * len(days)
total_commits_needed = 440

# 1. Project Sprints (4 major projects across the year, lasting 15-20 days each)
sprint_centers = [random.randint(30, len(days)-30) for _ in range(4)]
for center in sprint_centers:
    for offset in range(-12, 12):
        if 0 <= center + offset < len(days):
            if random.random() < 0.65: # 65% chance of activity during sprint days
                commit_counts[center + offset] += random.randint(1, 4)

# 2. Weekend Hackathons (5-8 random coding bursts during weekends)
weekend_spikes = [random.randint(0, len(days)-1) for _ in range(8)]
for spike in weekend_spikes:
    # Only trigger if it randomly falls near a weekend, or force it to closest weekend
    commit_counts[spike] += random.randint(5, 8)

# 3. Distribute remaining commits as scattered background activity
current_total = sum(commit_counts)
while current_total < total_commits_needed:
    idx = random.randint(0, len(days)-1)
    # Prefer weekdays for casual commits (70% weekday bias vs weekend absence)
    if days[idx].weekday() < 5 or random.random() < 0.4:
        commit_counts[idx] += 1
        current_total += 1

# 4. If we overshot 440, precisely trim down
while sum(commit_counts) > total_commits_needed:
    idx = random.randint(0, len(days)-1)
    if commit_counts[idx] > 0:
        commit_counts[idx] -= 1

print(f"Algorithm distributed exactly {sum(commit_counts)} commits across 2025.")
print("Starting commit generation (this may take 1-2 minutes).......")

total_commits = 0
for i, date in enumerate(days):
    count = commit_counts[i]
    for _ in range(count):
        file = random.choice(FILES)

        with open(file, "a", encoding="utf-8") as f:
            f.write(f"# update on {date}\n")

        # Realistic hours: Late mornings or evenings
        hour = random.choice([10, 11, 14, 15, 16, 20, 21, 22, 23, 0, 1])
        minute = random.randint(0, 59)

        date_str = date.strftime(f"%Y-%m-%d {hour}:{minute}:00")
        msg = random.choice(MESSAGES)

        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = date_str
        env["GIT_COMMITTER_DATE"] = date_str

        run(f'git add {file}', env=env)
        run(f'git commit --date="{date_str}" -m "{msg}"', env=env)
        total_commits += 1

print(f"✅ Generated EXACTLY {total_commits} realistic commits for 2025.")
print("Pushing to GitHub...")

try:
    subprocess.run(f"git push origin {BRANCH}", shell=True, check=True, cwd=REPO_PATH)
    print("✅ Successfully pushed 2025 timeline to GitHub!")
except subprocess.CalledProcessError:
    print("❌ Push failed. Try manually: git push origin main")
