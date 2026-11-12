"""
RECORD CHECK  -  my version
===========================

Name  :  M01148448
Lane  :  IT
Date  :  13-11-2026
Run it:   python template.py
"""

# =================================================================== FUNCTIONS

def parse_line(raw_line):
    """Clean one messy server line and return it as a dict."""
    line = raw_line.strip().lower()
    hostname, rest = line.split(",", 1)
    record = {"hostname": hostname.strip()}
    for piece in rest.split(","):
        key, value = piece.split("=")
        record[key.strip()] = float(value.strip())
    return record


def status_of(used, total):
    """Return OVER LIMIT, WARNING or OK for a used/total pair."""
    percent = used / total * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


# ====================================================================== INPUT

raw_records = []
with open("server_records.txt") as f:
    for line in f:
        if line.strip() != "":
            raw_records.append(line)


# =============================================================== PROCESS + OUTPUT

total_records = 0
flagged = 0

for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record["used"], record["total"])
    print(record, status)

    total_records = total_records + 1
    if status != "OK":
        flagged = flagged + 1

print(f"{total_records} records checked, {flagged} flagged")


