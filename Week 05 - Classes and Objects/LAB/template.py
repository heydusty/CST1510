"""
RECORD CHECK  -  my version
===========================

Name  :  AKSHAT MEHROTRA - DUSTY
Lane  :  IT
Date  :  October 22, 2026

Run it:   python template.py


# 1. Define a class called Record.


class Record:
    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Store the hostname, GB used and GB total."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return OVER LIMIT, WARNING or OK."""
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"



# 2. Create your records.

def load_records(path):
    """Read label,value,limit lines from a file and return a list of Records."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records

records = load_records("servers.txt")



# 3. Print a report for each record.



for record in records:
    status = record.status()
    if status == "OVER LIMIT":
        Record.over_limit_count += 1

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"  GB used   : {record.value}")
    print(f"  GB total  : {record.limit}")
    print(f"  Status    : {status}")
    print("=" * 34)

print()
print(f"{Record.over_limit_count} of {len(records)} servers were OVER LIMIT")


