import customtkinter as ctk
import string
import ast

global string_lst
string_lst = [str(c) for c in string.ascii_uppercase]
global enter_9label, enter_5label, enter_first_row, enter_first_row2, enter_max5, enter_max9, enter_name5, enter_name9, enter_ID5, enter_ID9
def read_from_output_file():
    try:
        with open('config.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                key, value = line.strip().split(': ')
                if key == 'column_9sub':
                    column_letters = ast.literal_eval(value)
                    first_letter = column_letters[0]
                    last_letter = column_letters[-1]
                    enter_9label.insert(0, f"{first_letter}-{last_letter}")
                elif key == 'column_5sub':
                    column_letters = ast.literal_eval(value)
                    first_letter = column_letters[0]
                    last_letter = column_letters[-1]
                    enter_5label.insert(0, f"{first_letter}-{last_letter}")
                elif key == 'first_row_5':
                    enter_first_row2.insert(0, value)
                elif key == 'first_row_9':
                    enter_first_row.insert(0, value)
                elif key == 'max_9':
                    enter_max9.insert(0, value)
                elif key == 'max_5':
                    enter_max5.insert(0, value)
                elif key == 'name9':
                    enter_name9.insert(0, value)
                elif key == 'name5':
                    enter_name5.insert(0, value)
                elif key == 'id9':
                    enter_ID9.insert(0, value)
                elif key == 'id5':
                    enter_ID5.insert(0, value)
    except FileNotFoundError:
        error.configure(text='ไม่พบบันทึกการตั้งค่า กรุณากรอกใหม่ให้ครบ')
def submit():
    global enter_9label, enter_first_row, enter_5label, enter_first_row2, error, enter_max5, enter_max9
    score_9column = str(enter_9label.get()).upper()
    try:
        first_row_9 = int(enter_first_row.get())
    except ValueError:
        error.configure(text='กรุณากรอกตัวเลข(ช่อง 9 วิชา)')
        return

    column_9sub = []
    for a in range(string_lst.index(score_9column[0]), string_lst.index(score_9column[-1]) + 1):
        column_9sub.append(string_lst[a])

    score_5column = str(enter_5label.get()).upper()
    try:
        first_row_5 = int(enter_first_row2.get())
    except ValueError:
        error.configure(text='กรุณากรอกตัวเลข(ช่อง 5 วิชา)')
        return
    try:
        max_9 = int(enter_max9.get())
    except ValueError: error.configure(text='โปรดกรอกคะแนนเต็ม 9 วิชา')
    try:
        max_5 = int(enter_max5.get())
    except ValueError: error.configure(text='โปรดกรอกคะแนนเต็ม 5 วิชา')
    column_5sub = []
    for b in range(string_lst.index(score_5column[0]), string_lst.index(score_5column[-1]) + 1):
        column_5sub.append(string_lst[b])
    full_row9 = column_9sub + list(string_lst[string_lst.index(column_9sub[-1])+1]) + list(string_lst[string_lst.index(column_9sub[-1])+2])
    full_row5 = column_5sub + list(string_lst[string_lst.index(column_5sub[-1])+1]) + list(string_lst[string_lst.index(column_5sub[-1])+2])
    try:
        name9 = str(enter_name9.get()).upper()
    except ValueError: error.configure(text='โปรดกรอกคอลัมน์ชื่อ 9 วิชา')
    try:
        name5 = str(enter_name5.get()).upper()
    except ValueError: error.configure(text='โปรดกรอกคอลัมน์ชื่อ 5 วิชา')
    
    try:
        id9 = str(enter_ID9.get()).upper()
    except ValueError: error.configure(text='โปรดกรอกคอลัมน์รหัสนักเรียน 9 วิชา')
    try:
        id5 = str(enter_ID5.get()).upper()
    except ValueError: error.configure(text='โปรดกรอกคอลัมน์รหัสนักเรียน 5 วิชา')

    # Write the values into a text file
    with open('config.txt', 'w') as file:
        file.write(f'column_9sub: {column_9sub}\n')
        file.write(f'column_5sub: {column_5sub}\n')
        file.write(f'first_row_5: {first_row_5}\n')
        file.write(f'first_row_9: {first_row_9}\n')
        file.write(f'max_9: {max_9}\n')
        file.write(f'max_5: {max_5}\n')
        file.write(f'full_row9: {full_row9}\n')
        file.write(f'full_row5: {full_row5}\n')
        file.write(f'name9: {name9}\n')
        file.write(f'name5: {name5}\n')
        file.write(f'id9: {id9}\n')
        file.write(f'id5: {id5}\n')
    file.close()
    
    saved.configure(text='Setting Saved!')

def config():
    global enter_9label, enter_first_row, enter_5label, enter_first_row2, error, enter_max5, enter_max9, saved, enter_name5, enter_name9, enter_ID5, enter_ID9
    frame = ctk.CTkFrame(master=app, height=200)
    frame.pack(padx=100, pady=10, fill='both')
    
    rank9 = ctk.CTkLabel(master=frame, text="9 วิชา", font=('Arial', 30))
    rank9.pack()
    frame2 = ctk.CTkFrame(master=frame, height=200)
    frame2.pack(padx=100, pady=10, fill='both')
    
    ctk.CTkLabel(master=frame2, text='ตำแหน่งคะแนน(หลัก): ', font=('Arial', 20)).grid(column=0, row=0)
    enter_9label = ctk.CTkEntry(master=frame2, placeholder_text='A-Z')
    enter_9label.grid(column=1, row=0, padx=20)
    
    ctk.CTkLabel(master=frame2, text='แถวของนักเรียนคนแรก: ', font=('Arial', 20)).grid(column=0, row=1, pady=5)
    enter_first_row = ctk.CTkEntry(master=frame2, placeholder_text='กรอกตัวเลข')
    enter_first_row.grid(column=1, row=1, padx=20)

    ctk.CTkLabel(master=frame2, text='คะแนนเต็ม', font=('Arial', 20)).grid(column=0, row=2)
    enter_max9 = ctk.CTkEntry(master=frame2, placeholder_text='กรอกตัวเลข: ')
    enter_max9.grid(column=1, row=2, padx=20)

    ctk.CTkLabel(master=frame2, text='คอลัมน์ของชื่อนักเรียน: ',font=('Arial', 20)).grid(column=0,row=3)
    enter_name9 = ctk.CTkEntry(master=frame2, placeholder_text="Enter Name Column", font=('Arial', 10))
    enter_name9.grid(column=1, row=3, padx=20)

    ctk.CTkLabel(master=frame2, text='คอลัมน์เลขประจำตัวนักเรียน: ', font=('Arial', 20)).grid(column=0, row=4, padx=10)
    enter_ID9 = ctk.CTkEntry(master=frame2, placeholder_text='Enter ID Column', font=('Arial', 10))
    enter_ID9.grid(column=1, row=4, padx=20)

    
    #End Of Rank 9 Subject

    rank5 = ctk.CTkLabel(master=frame, text="5 วิชา", font=('Arial', 30))
    rank5.pack(pady=30)
    frame3 = ctk.CTkFrame(master=frame, height=200)
    frame3.pack(padx=100, pady=10, fill='both')
    
    ctk.CTkLabel(master=frame3, text='ตำแหน่งคะแนน(หลัก): ', font=('Arial', 20)).grid(column=0, row=0)
    enter_5label = ctk.CTkEntry(master=frame3, placeholder_text='A-Z')
    enter_5label.grid(column=1, row=0, padx=20)

    ctk.CTkLabel(master=frame3, text='แถวของนักเรียนคนแรก: ', font=('Arial', 20)).grid(column=0, row=1, pady=5)
    enter_first_row2 = ctk.CTkEntry(master=frame3, placeholder_text='กรอกตัวเลข')
    enter_first_row2.grid(column=1, row=1, padx=20)
    
    ctk.CTkLabel(master=frame3, text='คะแนนเต็ม: ', font=('Arial', 20)).grid(column=0, row=2)
    enter_max5 = ctk.CTkEntry(master=frame3, placeholder_text='กรอกตัวเลข')
    enter_max5.grid(column=1, row=2, padx=20)
    
    ctk.CTkLabel(master=frame3, text='คอลัมน์ของชื่อนักเรียน: ',font=('Arial', 20)).grid(column=0,row=3)
    enter_name5 = ctk.CTkEntry(master=frame3, placeholder_text="Enter Name Column", font=('Arial', 10))
    enter_name5.grid(column=1, row=3, padx=20)

    ctk.CTkLabel(master=frame3, text='คอลัมน์เลขประจำตัวนักเรียน: ', font=('Arial', 20)).grid(column=0, row=4, padx=10)
    enter_ID5 = ctk.CTkEntry(master=frame3, placeholder_text='Enter ID Column', font=('Arial', 10))
    enter_ID5.grid(column=1, row=4, padx=20)
    
    #End Of Rank 5 Subject
    
    error = ctk.CTkLabel(master=app, text='', font=('Arial', 20), text_color='red')
    error.pack()
    
    submit_bt = ctk.CTkButton(master=app, text='Save Config', font=('Arial', 30), command=submit)
    submit_bt.pack(pady=10)
    
    saved = ctk.CTkLabel(master=app, text='', font=('Arial', 35))
    saved.pack(pady=20)
def main():
    global app, enter_9label, enter_5label, enter_first_row, enter_first_row2
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    app = ctk.CTk()
    app.geometry("804x600")
    app.minsize(width=804, height=600)
    app.title("Ranking Program By Anansit")
    
    label = ctk.CTkLabel(master=app, text="Setting Config", font=('Arial', 20))
    label.pack()
    
    config()
    
    read_from_output_file()  # Call the function to read from output.txt
    
    app.mainloop()

