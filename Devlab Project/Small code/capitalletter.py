import string

a = [1 if x in string.ascii_uppercase else 0 for x in input()]

if any(a) == False: print('All Small Letter')
elif all(a) == True: print('All Capital Letter')
else: print('Mix')
