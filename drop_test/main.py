from pathlib import Path
import math


def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    for line in data.splitlines():
        devices, height = line.split(", ") 
        print(min_num_of_drops(int(devices), int(height)))

def min_num_of_drops(n, h):
    if h == 1 or n == 1:
        return h
    
    drops = 0
    while True:
        drops += 1
        total = 0
        for k in range(1, n + 1):
            total += math.comb(drops, k)
        if total >= h:
            return drops

if __name__ == "__main__":
    main()
