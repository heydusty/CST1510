"""
RECORD CHECK WITH PANDAS  -  my version
=======================================

Name  :  M01148448
Lane  :  IT
Date  :  08/11/2026

Run it:   python template.py
"""

import pandas as pd
import matplotlib.pyplot as plt

# =========================================================== THRESHOLD
# Read my own CSV and add a percent column (whole column at once, no loop)
servers = pd.read_csv("servers_it.csv")
servers["percent"] = (servers["used_gb"] / servers["total_gb"]) * 100

print("=== All servers ===")
print(servers)
print()

# ============================================================= TYPICAL
# Add a status column with .apply() and a one-expression lambda.
# Disks are flagged at 90% (critical) and 80% (warning) because a disk
# that is nearly full can stop a server writing logs or data.
servers["status"] = servers["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 90 else ("WARNING" if p >= 80 else "OK")
)

# Boolean filter, no loop: only the rows that are not OK
needs_attention = servers[servers["status"] != "OK"]
print("=== Servers that need attention ===")
print(needs_attention)
print()

# =========================================================== EXCELLENT
# Count per status
status_counts = servers.groupby("status")["hostname"].count()
print("=== Servers per status ===")
print(status_counts)

# Save the full DataFrame to a new CSV
servers.to_csv("servers_report.csv", index=False)

# One bar chart of the counts per status, saved as a PNG
status_counts.plot(kind="bar", title="Servers per status")
plt.ylabel("Number of servers")
plt.tight_layout()
plt.savefig("status_counts.png")
plt.show()