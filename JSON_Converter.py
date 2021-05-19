# Created By: Giwon Kim
# Date: May 18, 2021

import json
import csv
with open ("Badge_Audit_Table.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    next(reader)
    data = {"Audits":[]}
    for row in reader:
        data["Audits"].append({row[0]:{"Human_Rights_Labor":{"Conflict":row[1], "Child_Labor": row[2], "Forced_Labor": row[3]}, "Health_and_Safety":{"Occupational_Health_and_Safety":row[4], "Community_Health_and_Safety":row[5]}, "Environmental":{"Water_Consumption_Abstraction":row[6], "Tailings":row[7], "Pollution":row[8]}}})

with open ("Badge_Audit_Table.json", "w") as f:
    json.dump(data, f, indent=4)
