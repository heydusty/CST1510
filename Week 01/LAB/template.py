"""
RECORD CHECK  -  my version
===========================

Name  :  Akshat Mehrotra
Lane  :  IT
Date  :  3 October 2026

Run it:   python template.py


"""


hostname = input("Hostname      : ")
gb_used = float(input("GB used       : "))
gb_total = float(input("GB total      : "))




gb_free = gb_total - gb_used
percent_used = gb_used / gb_total * 100

# Extra line: room left before the disk hits 90% full.
# Why: admins usually get an alert at 90%, not at 100%, so this tells you how
# much you can still write before someone gets paged. A negative number means
# the disk is already past the warning level.
WARNING_LEVEL = 0.90
gb_until_warning = gb_total * WARNING_LEVEL - gb_used




print()
print("=" * 34)
print(f"  RECORD CHECK  -  {hostname}")
print("=" * 34)
print(f"  Used        : {gb_used:>10.2f} GB")
print(f"  Total       : {gb_total:>10.2f} GB")
print(f"  Free        : {gb_free:>+10.2f} GB")
print(f"  Percent     : {percent_used:>10.2f} %")
print(f"  To 90% warn : {gb_until_warning:>+10.2f} GB")
print("=" * 34)


