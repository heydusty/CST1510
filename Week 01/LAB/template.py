"""
RECORD CHECK  -  my version
===========================

Name  :  Akshat Mehrotra
Lane  :  IT
Date  :  3 October 2026

Run it:   python template.py

Checks how full a server's disk is: asks for the hostname, the GB used and
the GB total, then reports free space, percentage used and how much room is
left before the disk reaches a 90% warning level.
"""



hostname = input("Hostname      : ")
gb_used = float(input("GB used       : "))
gb_total = float(input("GB total      : "))



gb_free = gb_total - gb_used
percent_used = gb_used / gb_total * 100


WARNING_LEVEL = 0.90
gb_until_warning = gb_total * WARNING_LEVEL - gb_used



print("=" * 34)
print(f"  RECORD CHECK  -  {hostname}")
print("=" * 34)
print(f"  Used        : {gb_used:>10.2f} GB")
print(f"  Total       : {gb_total:>10.2f} GB")
print(f"  Free        : {gb_free:>+10.2f} GB")
print(f"  Percent     : {percent_used:>10.2f} %")
print(f"  To 90% warn : {gb_until_warning:>+10.2f} GB")
print("=" * 34)


