animal1, quantity1 = input().split(' ')
animal2, quantity2 = input().split(' ')
animal3, quantity3 = input().split(' ')

legs = {'Dog':4, 'Cat':4, 'Chicken':2, 'Cow':4, 'Snake':0, 'Duck':2, 'Bird':2}

total = legs[animal1]*int(quantity1) + legs[animal2]*int(quantity2) + legs[animal3]*int(quantity3)

print(total)