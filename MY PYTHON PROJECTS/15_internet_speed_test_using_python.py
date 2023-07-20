from tkinter import *
import speedtest

def speed_check():
    sp = speedtest.Speedtest()
    sp.get_servers()
    downloading_speed = str(round(sp.download()/10**6, 3)) + 'Mbps'        #in bits per seconds
    uploading_speed = 	str(round(sp.upload()/10**6, 3)) + 'Mbps' 
    lab_download.config(text=downloading_speed)
    lab_upload.config(text=uploading_speed)


sp = Tk()

sp.title('Internet Speed Test')
sp.geometry(('500x700'))
sp.config(bg='blue')
lab = Label(sp, text="Internet Speed Test", font=('Times New Roman', 20, 'bold'))        #bg='blue', fg='white'
lab.place(x = 60, y = 40, height=50, width=380)
lab = Label(sp, text="Download Speed", font=('Times New Roman', 20, 'bold'))
lab.place(x = 60, y = 130, height=50, width=380)
lab_download = Label(sp, text="00", font=('Times New Roman', 20, 'bold'))
lab_download.place(x = 60, y = 200, height=50, width=380)
lab = Label(sp, text="Upload Speed", font=('Times New Roman', 20, 'bold'))
lab.place(x = 60, y = 290, height=50, width=380)
lab_upload = Label(sp, text="00", font=('Times New Roman', 20, 'bold'))
lab_upload.place(x = 60, y = 360, height=50, width=380)

button = Button(sp, text='CHECK SPEED', font=('Times New Roman', 20, 'bold'), relief=RAISED, bg='red', command=speed_check)
button.place(x = 60, y = 450, height=50, width=380)

sp.mainloop()