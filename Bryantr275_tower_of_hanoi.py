# Raymond Bryant, Jr.
# CIS-2532-NET01
# Tower of Hanoi
# 04/28/24

def hanoi(n, source, destination, temp):
    if n == 1:
        print(f"{source} → {destination}")
    else:
        hanoi(n-1, source, temp, destination)
        print(f"{source} → {destination}")
        hanoi(n-1, temp, destination, source)


# Example usage:
n = 3  # Number of disks
source_peg = 1
destination_peg = 3
temp_peg = 2

print(
    f"Steps to move {n} disks from peg {source_peg} to peg {destination_peg}:")
hanoi(n, source_peg, destination_peg, temp_peg)
