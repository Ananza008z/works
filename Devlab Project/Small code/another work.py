import time

Shop_thing = {}
Shop_price = {}
Shop_name = "Ananzit COde Shop"
line = "----------------------"
n = int(input('Input number of all your thing: '))
for i in range(n):
    name = str(input('Name %d : ' % (i + 1)))
    Shop_thing[i + 1] = name
    price = str(input('Price %d : ' % (i + 1)))
    Shop_price[i + 1] = price
start = time.time()
total = 0
print(Shop_name)
print(line)

for i in range(n):
    print(Shop_thing[i + 1] + " : " + Shop_price[i + 1])
    total += int(Shop_price[i + 1])
print(line)
print("total in : %d" % total)

end = time.time()

print(end - start)
