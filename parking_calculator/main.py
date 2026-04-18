from pathlib import Path
from datetime import datetime, timedelta

def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    fees = {}
    for line in data.splitlines()[2:]:
        parts = line.split("\t")
        try:
            start = datetime.fromisoformat(parts[2])
            end = datetime.fromisoformat(parts[4])
            fee = parking_fee_calculator(start, end)
            print(f"{fee} Ft")
            fees[parts[0]] = fee

        except ValueError:
            print("Nem megfelelő dátum formátum")
    
    with open("fees.txt", "w") as f:
        for plate, fee in fees.items():
            f.write(f"{plate}: {fee}Ft\n")
        

def parking_fee_calculator(start, end):
    time = end - start

    if time.days == 0:
        if time <= timedelta(minutes=30):
            return 0
        time -= timedelta(minutes=30)

        if time <= timedelta(hours=3):
            base_price = 0
            fee = 300
        else:
            base_price = 900
            fee = 500
            time -= timedelta(hours=3)
        
        if time.seconds % 3600 != 0:
            return base_price + (time // timedelta(hours=1) + 1) * fee
        else:
            return base_price + time // timedelta(hours=1) * fee
    else:
        if time.seconds % 3600 == 0:
            return time.days * 10000 + time.seconds // 3600 * 500
        else:
            return time.days * 10000 + (time.seconds // 3600 + 1) * 500

if __name__ == "__main__":
    main()
