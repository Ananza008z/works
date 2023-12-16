numlst = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10}

readline = []
while True:
    x = str(input())
    if x == '000':
        break
    else:
        readline.append([c.lower() for c in x])
    
for line in readline:
    print(f'{numlst[line[0]]}+{numlst[line[1]]}={numlst[line[0]]+numlst[line[1]]}')
    
print('Exit...')