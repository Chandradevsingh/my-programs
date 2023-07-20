from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')        #String From Time
    min = time.strftime('%M')
    sec = time.strftime('%S')   
    am = time.strftime('%p')
    date = time.strftime('%d')
    Month = time.strftime('%m')
    Year = time.strftime('%y')
    Day = time.strftime('%a')

    lab_hr.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_date.config(text=date)
    lab_mon.config(text=Month)
    lab_year.config(text=Year)
    lab_day.config(text=Day)
    lab_hr.after(200, date_time)
    
clock = Tk()
clock.title('        ***Digital Clock***')
clock.geometry('1000x500')
clock.config(bg='yelloW')

lab_hr = Label(clock, text='00', font=('Times New Roman', 60, 'bold'), bg='red', fg='white')
lab_hr.place(x = 120, y = 50, height = 110, width = 100)

lab_hr_text = Label(clock, text='Hour', font=('Times New Roman', 20, 'bold'), bg='red', fg='white')
lab_hr_text.place(x = 120, y = 190, height = 40, width = 100)

lab_min = Label(clock, text='00', font=('Times New Roman', 60, 'bold'), bg='red', fg='white')
lab_min.place(x = 340, y = 50, height = 110, width = 100)

lab_min_text = Label(clock, text='Min.', font=('Times New Roman', 20, 'bold'), bg='red', fg='white')
lab_min_text.place(x = 340, y = 190, height = 40, width = 100)

lab_sec = Label(clock, text='00', font=('Times New Roman', 60, 'bold'), bg='red', fg='white')
lab_sec.place(x = 560, y = 50, height = 110, width = 100)

lab_sec_text = Label(clock, text='Sec.', font=('Times New Roman', 20, 'bold'), bg='red', fg='white')
lab_sec_text.place(x = 560, y = 190, height = 40, width = 100)

lab_am = Label(clock, text='00', font=('Times New Roman', 50, 'bold'), bg='red', fg='white')
lab_am.place(x = 780, y = 50, height = 110, width = 100)

lab_am_text = Label(clock, text='AM/PM', font=('Times New Roman', 20, 'bold'), bg='red', fg='white')
lab_am_text.place(x = 780, y = 190, height = 40, width = 100)

lab_date = Label(clock, text='00', font=('Times New Roman', 60, 'bold'), bg='red', fg='white')
lab_date.place(x = 120, y = 270, height = 110, width = 100)

lab_date_text = Label(clock, text='Date', font=('Times New Roman', 20, 'bold'), bg='red', fg='white')
lab_date_text.place(x = 120, y = 420, height = 40, width = 100)

lab_mon = Label(clock, text='00', font=('Times New Roman', 60, 'bold'), bg='red', fg='white')
lab_mon.place(x = 340, y = 270, height = 110, width = 100)

lab_mon_text = Label(clock, text='Month', font=('Times New Roman', 20, 'bold'), bg='red', fg='white')
lab_mon_text.place(x = 340, y = 420, height = 40, width = 100)

lab_year = Label(clock, text='00', font=('Times New Roman', 60, 'bold'), bg='red', fg='white')
lab_year.place(x = 560, y = 270, height = 110, width = 100)

lab_year_text = Label(clock, text='Year', font=('Times New Roman', 20, 'bold'), bg='red', fg='white')
lab_year_text.place(x = 560, y = 420, height = 40, width = 100)

lab_day = Label(clock, text='00', font=('Times New Roman', 42, 'bold'), bg='red', fg='white')
lab_day.place(x = 780, y = 270, height = 110, width = 100)

lab_day_text = Label(clock, text='Day', font=('Times New Roman', 20, 'bold'), bg='red', fg='white')
lab_day_text.place(x = 780, y = 420, height = 40, width = 100)

date_time()
clock.mainloop()