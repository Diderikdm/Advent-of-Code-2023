from datetime import datetime
now = datetime.now()

for x in range(1, 26):
    try:
        n = datetime.now()
        day = f"day{str(x).rjust(2, '0')}"
        print(day)
        __import__(day)
        b = datetime.now()
        print(b - n, "\n")
    except:
        continue

print("all days", b - now)
