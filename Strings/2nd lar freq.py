"""Find the second most frequently occurring character in a string.

Example:Input: "programming"
Output: 'g'"""
s = input("Enter a string: ")

seen = {}

for ch in s:
    if ch not in seen:
        seen[ch] = 1
    else:
        seen[ch] += 1

f = list(set(seen.values()))
f.sort(reverse=True)

if len(f) < 2:
    print("No second highest frequency")
else:
    for i in seen:
        if seen[i] == f[1]:
            print(i)
