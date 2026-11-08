"""Find the sum of digits until a single digit is obtained.

Example:
Input: 9875

9 + 8 + 7 + 5 = 29
2 + 9 = 11
1 + 1 = 2

Output: 2"""
num = int(input("Enter a number: "))

total = 0

while num > 0:
    d = num % 10
    total += d
    num //= 10

while total > 9:
    num = total
    total = 0

    while num > 0:
        d = num % 10
        total += d
        num //= 10

print(total)
