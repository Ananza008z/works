print('Choose Your Order')
print('Code----Coffee name---------price----')
print('------------------------S-----M-----L')
print('-A-------Espresso------40----45----50')
print('-B------Cappuccino-----45----50----55')
print('-C---------Mocha-------40----50----60')
print('-D-----Black Coffee----50----55----60')
global Coffee_lst 
Cofee_lst = {'A':'Espresso', 'B':'Cappuccino', 'C':'Mocha', 'D':'Black Coffee'}
global price
price = {'A':{'S':40, 'M':45, 'L':50},
        'B':{'S':45, 'M':50, 'L':55},
        'C':{'S':40, 'M':50, 'L':60},
        'D':{'S':50, 'M':55, 'L':60}}
global totalprice
totalprice = 0
def get_size():
    size_in = str(input("Select size: "))
    if size_in not in 'SML':
        print('Error Size')
        get_size()
    else: return str(size_in)
    
def choose():
    global totalprice
    select = str(input("Enter cofee code X to quit: "))
    if select not in 'ABCDX':
        print("Error input")
        choose()
    elif select == 'X':
        print(f'Total          {totalprice}       baht')
        return
    else:
        size = get_size()
        quantities = int(input("How many cups: "))
        totalprice += price[select][size] * quantities
        print(f"Current Order {Cofee_lst[select]} For {quantities} Cup in total {totalprice}")
        choose()
choose()