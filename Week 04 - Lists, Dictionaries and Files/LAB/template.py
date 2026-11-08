"""
RECORD CHECK  -  my version
===========================

Name  : Akshat Mehrotra - Dusty
Lane  : IT
Date  : October 17, 2026

Run it:   python template.py


"""



def check_record(value, limit):
    """Work out the difference, percent and status for one server."""
    difference = value - limit
    percent = (value / limit) * 100
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    return difference, percent, status


def print_report(label, difference, percent, status):
    """Print one line of the report for a server."""
    print(f"{label}: {difference} GB, {percent:.1f}%, {status}")




records = [
    {"label": "srv-01", "value": 87, "limit": 120},
    {"label": "srv-02", "value": 125, "limit": 120},
    {"label": "srv-03", "value": 110, "limit": 120},
]



for record in records:
    difference, percent, status = check_record(record["value"], record["limit"])
    print_report(record["label"], difference, percent, status)


