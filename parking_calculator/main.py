from pathlib import Path
from datetime import datetime, timedelta

def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    for line in data.splitlines()[2:]:
        parts = line.split("\t")
        print(parking_fee_calculator(parts[2], parts[4]))

def parking_fee_calculator(start, end):
    start = datetime.fromisoformat(start)
    end = datetime.fromisoformat(end)
    time = end - start

    if time.days == 0:
        if time <= timedelta(minutes=30):
            return 0
        time -= timedelta(minutes=30)

        if time <= timedelta(hours=3):
            if time.seconds % 3600 != 0:
                return (time // timedelta(hours=1) + 1) * 300  
            else:
                return time // timedelta(hours=1) * 300
        time -= timedelta(hours=3)

        if time < timedelta(hours=20, minutes=30):
            if time.seconds % 3600 != 0:
                return 900 + (time // timedelta(hours=1) + 1) * 500
            else:
                return 900 + time // timedelta(hours=1) * 500
    else:
        if time.seconds % 3600 == 0:
            return time.days * 10000 + time.seconds // 3600 * 500
        else:
            return time.days * 10000 + (time.seconds // 3600 + 1) * 500

if __name__ == "__main__":
    main()
