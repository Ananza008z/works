import tkinter as tk
import time
import random

app = tk.Tk()
app.minsize(height=580, width=700)
app.title('Game 180 IQ')


def clock(timer, counter):
    #if stopper == 0:
    #def stop():
        #timer.config(text=counter)
        #pass
    counter += 1
    actual_time = 46 - counter
    if actual_time > -1:
        show_timer = 'เวลาที่เหลือ : ' + str(actual_time)
        timer.config(text=show_timer)
        timer.after(1000, clock, timer, counter)
    else:
        timer.config(text='หมดเวลา')
    #else:
        #timer.config(text=actual_time)
        
def random_number():
    clock(timer, 0)
    a = str(random.randint(0, 9))
    b = str(random.randint(0, 9))
    c = str(random.randint(0, 9))
    d = str(random.randint(0, 9))
    wanted_num = str(random.randint(10, 100))
    
    out = a + ' ' + b + ' ' + c + ' ' + d
    
    Num_line.configure(text=out)
    ans.configure(text=wanted_num)
    

Num_line = tk.Label(master=app,text='',font=40)
Num_line.pack(pady=40)

space = tk.Label(master=app, text='-----------------\nคำตอบที่ต้องการ', font=40)
space.pack(pady=10)

ans = tk.Label(master=app,text='',font=40)
ans.pack(pady=10)

button = tk.Button(master=app,text='กดเพื่อสุ่ม', command=random_number, font=40)
button.pack(pady=20)

timer = tk.Label(master=app, text='',font=40)
timer.pack(pady=10)

stop_bt = tk.Button(master=app, text='Stop', font=40)
app.mainloop()