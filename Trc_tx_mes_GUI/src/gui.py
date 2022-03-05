import tkinter as tk


def start():
    
    return

def check_freq():
    
    return

def check_box_state():

    return:


window = tk.Tk()
window.title("Модель приемника ТРЦ3")

#config size of main window
h_window = 1300
w_window = 580
offset_dx_window = 30
offset_dy_window = 10
#window.config(bg = "black")
resizable_x_window = False
resizable_y_window = False
icon = tk.PhotoImage(file = "data-model-icon-21.png")
window.iconphoto(False, icon)
window.geometry(f"{h_window}x{w_window}+{offset_dx_window}+{offset_dy_window}")
window.resizable(resizable_x_window, resizable_y_window)
#end

label0 = tk.Label(window,text = "Параметры входного сигнала",
                        relief = tk.RAISED,
                        bd = 2
                ).grid(row = 0, column = 0, columnspan=2,stick = 'we')

label1 = tk.Label(window,text = "      Частота           Уровень (в отсчетах)",
                        relief = tk.RAISED,
                        bd = 2
                ).grid(row = 1, column = 0, columnspan =2,stick = 'we')

Start_but = tk.Button(window, text ="Запустить моделирование",\
                        command = start).grid(row =19,\
                        column = 0, columnspan=2, stick='we'
                     )
                
freqs = ("420 Гц / 8 Гц", "420 Гц / 12 Гц",
         "480 Гц / 8 Гц", "480 Гц / 12 Гц",
         "565 Гц / 8 Гц", "565 Гц / 12 Гц",
         "720 Гц / 8 Гц", "720 Гц / 12 Гц",
         "780 Гц / 8 Гц", "780 Гц / 12 Гц",
         "75 Гц",         "125 Гц",
         "175 Гц",        "225 Гц",
         "275 Гц",         "325 Гц"
        )


for num_freq in range(len(freqs)):
    cb = freqs[num_freq]
    cb = tk.Checkbutton(window, text = freqs[num_freq]).grid(row =num_freq+3,\
     column =0, stick ='w')
    inp = freqs[num_freq] + " level"
    inp = tk.Entry(window).grid(row =num_freq+3,\
     column =1, stick ='e')


#window.grid_columnconfigure(0, minsize=15)
#window.grid_columnconfigure(1, weight=10)

window.mainloop()
