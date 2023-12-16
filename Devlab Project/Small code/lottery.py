lines = int(input())

lotto = []
corrector = True

for loop in range(lines):
    read_line = str(input().rstrip())
    if len(read_line) != 6 or len(read_line) % 6 != 0:
        corrector = False
        break
    if len(read_line) > 6:
        lotto += [read_line[i:i+6] for i in range(0, len(read_line), 6)]
        print(lotto)
        break
    else:
        lotto.append(read_line)

total_money = 0
cards = {}

for check in lotto:
    if check == '475632':
        total_money += 6000000
        cards[check] = ['first prize 6000000 bath']
        continue
    if check[0:3] in ['548', '629']:
        total_money += 4000
        cards[check] = ['3 digit prefix prize 4000 bath']
    if check[3:6] in ['255', '867']:
        total_money += 4000
        if check not in cards:
            cards[check] = ['3 digit suffix prize 4000 bath']
        else: cards[check].append('3 digit suffix prize 4000 bath')
    if check[4:6] == '82':
        total_money += 2000
        if check not in cards:
            cards[check] = ['2 digit suffix prize 2000 bath']
        else: cards[check].append('2 digit suffix prize 2000 bath')
if len(cards) != 0:
    print(len(cards))
    for k in cards:
        print(k, ','.join(cards[k]), end='.\n')
    print(f'You got {total_money} bath.')
elif corrector == False: print('Try again.')
else: print('Sorry you didnt get the prize this time.')
