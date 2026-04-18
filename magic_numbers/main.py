from pathlib import Path


def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    for num in data.splitlines():
        if num.isnumeric():
            print(next_magic_num(int(num)))
        else:
            nums = num.split("^")
            print(next_magic_num(int(nums[0]) ** int(nums[1])))

def next_magic_num(n):
    num_len = len(str(n))
    first_half = str(n)[:((num_len + 1) // 2)]
    first_half_reversed = int(first_half[::-1])
    second_half = str(n)[(num_len // 2):]
    multiplier = 10**((num_len + 1) // 2)

    if first_half_reversed > int(second_half):
        first_half = int(first_half)
    else:
        first_half = int(first_half) + 1
        first_half_reversed = int(str(first_half)[::-1])
    
    if (num_len % 2 == 0):
        return first_half * multiplier + first_half_reversed
    else:
        return int(str(first_half)[:-1]) * multiplier + first_half_reversed

if __name__ == "__main__":
    main()
