import os
from lineNotify import lineNotify

if os.path.exists("Usage_Monitor.txt"):
    with open("Usage_Monitor.txt", "r", encoding="utf-8") as f:
        output = f.read().split(" ")[28]
        # IntOutput = output.split(".")[0]
        # IntOutput = round(float(IntOutput))
        # if IntOutput < 25 :

        lineNotify("CPU usage " + output + " used!")