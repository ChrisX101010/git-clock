import os
import datetime

# Digitalni prikaz brojeva (7x3 matrica)
DIGIT_MAP = {
    "0": ["111", "101", "101", "101", "101", "101", "111"],
    "1": ["010", "110", "010", "010", "010", "010", "111"],
    "2": ["111", "001", "001", "111", "100", "100", "111"],
    "3": ["111", "001", "001", "111", "001", "001", "111"],
    "4": ["101", "101", "101", "111", "001", "001", "001"],
    "5": ["111", "100", "100", "111", "001", "001", "111"],
    "6": ["111", "100", "100", "111", "101", "101", "111"],
    "7": ["111", "001", "001", "001", "001", "001", "001"],
    "8": ["111", "101", "101", "111", "101", "101", "111"],
    "9": ["111", "101", "101", "111", "001", "001", "111"],
    ":": ["000", "010", "000", "000", "010", "000", "000"]
}

def get_commit_positions():
    """Generiše commit pozicije na osnovu trenutnog vremena."""
    now = datetime.datetime.now()
    digits = f"{now.hour:02}:{now.minute:02}"  # HH:MM format

    positions = []
    start_x = 0  # Početna horizontalna pozicija na GitHub Contributions Graph-u
    for digit in digits:
        digit_map = DIGIT_MAP[digit]
        for y, row in enumerate(digit_map):
            for x, cell in enumerate(row):
                if cell == "1":
                    positions.append((start_x + x, y))  # Dodaj X,Y u gridu
        start_x += 4  # Razmak između cifara

    return positions

def create_commit(days_back):
    """Kreira commit za tačan dan u prošlosti."""
    commit_date = (datetime.datetime.now() - datetime.timedelta(days=days_back)).strftime("%Y-%m-%d")
    os.system(f'echo "{commit_date}" > commit.txt')
    os.system("git add commit.txt")
    os.system(f'GIT_AUTHOR_DATE="{commit_date}T12:00:00" GIT_COMMITTER_DATE="{commit_date}T12:00:00" git commit -m "Commit for {commit_date}"')

# Generiši commitove na tačnim mestima
commit_positions = get_commit_positions()
for x, y in commit_positions:
    day_offset = (52 - x) * 7 + y  # Pretvaranje u GitHub grid format
    create_commit(day_offset)

# Push commitova na GitHub
os.system("git push origin main")
