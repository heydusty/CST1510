"""
RECORD CHECK  -  my version
===========================

Name  :  Akshat Mehrotra
Lane  :  IT
Date  :  3 October 2026

Run it:   python template.py

Checks how full a server's disk is. Type "quit" as the hostname to stop.
"""

over_limit_count = 0

while True:
    # ================================================================ INPUT
    hostname = input("Hostname (or quit) : ")
    if hostname == "quit":
        break
    gb_used = float(input("GB used            : "))
    gb_total = float(input("GB total           : "))

    # ============================================================== PROCESS
    gb_free = gb_total - gb_used
    percent_used = (gb_used / gb_total) * 100

    if percent_used >= 100:
        status = "OVER LIMIT"
        over_limit_count = over_limit_count + 1
    elif percent_used >= 90:
        status = "WARNING"
    else:
        status = "OK"

    # =============================================================== OUTPUT
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {hostname}")
    print("=" * 34)
    print(f"  Used        : {gb_used:>10.2f}")
    print(f"  Total       : {gb_total:>10.2f}")
    print(f"  Free        : {gb_free:>10.2f}")
    print(f"  Percent     : {percent_used:>10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)
    print()

print(f"Records OVER LIMIT this session: {over_limit_count}")