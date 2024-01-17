import ttkbootstrap as ttk
import FontSetting as Font 
from datetime import datetime
import time
fs = Font.SetFontFamily('Poppins')

def update_time():
    nowTime = datetime.now().strftime("%H:%M:%S %p")
    timeUpdate.set(str(nowTime))
    root.after(1000, update_time)

root = ttk.Window(themename='darkly')
root.geometry('700x200')
root.title('Dark Clock')


timeUpdate = ttk.StringVar()
mainTimeLabel = ttk.Label(root, textvariable=timeUpdate,font=fs.setFont_size_style(60,'bold'))
mainTimeLabel.pack(anchor='center')

update_time()

root.mainloop()