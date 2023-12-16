n = int(input())

readline = [str(c) for c in input()]
readline.reverse()
rounds = 0

for index, value in enumerate(readline):
    if index == 0: continue
    if value != readline[index-1]:
        for k in range(index):
            readline[k] = value
        rounds += 1
readline = [int(x) for x in readline]
if all(readline) == False:
    rounds += 1
print(rounds)