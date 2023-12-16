x = {'A':1, 'B':2}
sort_item = sorted(x.items(), key=lambda k:k[1], reverse=True)
for key, value in sort_item:
    print(key, value)