"""
RECORD CHECK  -  my version
===========================

Name  : Dusty - Akshat Mehrotra
Lane  : IT
Date  : October 11, 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""



def status_of(percent):
    """Return the status based on percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    return "OK"


def check(value, limit):
    """Return free space and usage percentage."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent



label = input("Enter server name: ")
value = float(input("Enter GB used: "))
limit = float(input("Enter total GB: "))



difference, percent = check(value, limit)
status = status_of(percent)




print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"Used       : {value:>10.2f}")
print(f"Total      : {limit:>10.2f}")
print(f"Free       : {difference:>10.2f}")
print(f"Percent    : {percent:>10.2f} %")
print(f"Status     : {status:>10}")

print("=" * 34)


