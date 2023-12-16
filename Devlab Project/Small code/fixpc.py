import ast
import string

pc = []

for i in range(3):
    pc.append(str(input()))
new_file = []
for k in pc:
    key, values = k.split(':')
    if key == 'GUITAR':
        delete_virus = values.strip('][').split(',')
        for check in delete_virus:
            new = [1 if c in string.ascii_letters else 0 for c in check.strip()]
            if all(new) == True:new_file.append(check.strip())
            
passage = ','.join(new_file)
print(f'GUITAR:[{passage}]')
