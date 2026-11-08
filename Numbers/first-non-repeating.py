"""Find the first non-repeating digit in a number.

Example:Input: 12234551
Output: 3"""
num = int(input("Enter a number: "))
l = []

while num > 0:
    d = num % 10
    l.append(d)
    num = num // 10

l.reverse()

s = {}

for i in l:
    if i not in s:
        s[i] = 1
    else:
        s[i] += 1

for i in s:
    if s[i] == 1:
        print(i)
        break
else:
    print("No non-repeating digit")
