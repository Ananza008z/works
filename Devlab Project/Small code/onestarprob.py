n = str(input()).strip()

er = 'Compile Error!'
if n[0:8] == 'printf("':
    if n[len(n)-3:len(n)] == '");':
        print(n[8:len(n)-3])
    else: print(er)
else:print(er)