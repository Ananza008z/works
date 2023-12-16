line = str(input())
n = str(input())

line = line.split(n)
print('\n',line, '\n')
for i, text in enumerate(line):
    print(i)
    if i == 0:
        print(f'{text}{n}')
    elif i == len(line)-1:
        print(f'{n}{text}')
    else:
        print(f'{n}{text}{n}')