actual_value = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'J':10, 'Q':11, 'K':12}

read_line = [c for c in input().split()]
read_line.sort(key=lambda x:actual_value[x])
print(' '.join(read_line))
