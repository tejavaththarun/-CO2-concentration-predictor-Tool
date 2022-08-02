from tkinter import *

def answer():
    x1 = float(x.get())
    x2 = float(y.get())
    x3 = float(z.get())
    Ans = (-4208.46*x1)-(599.844*x2)+(334.189*x3)-(2.2*(x1 ** 2)) + (42.285 * x1 * x2) + (2.587 * x1 * x3) + (318.2008 * (x2 ** 2)) - (14.679 * x2 * x3) + (0.00634 * (x3 ** 2)) - (148475.938)
    #print(Ans)
    if Ans>=1000 and Ans<=3000:
        return "Open 25% of Your window."
    if Ans >=3000 and Ans<=5000:
        return "Open 50% of Your window."
    if Ans>=5000:
        return "Open the Entire Window."
    #return Ans

def getans():
    x1 = float(x.get())
    x2 = float(y.get())
    x3 = float(z .get())
    Ans = (-4208.46 * x1) - (599.844 * x2) + (334.189 * x3) - (2.2 * (x1 ** 2)) + (42.285 * x1 * x2) + (2.587 * x1 * x3) + (318.2008 * (x2 ** 2)) - (14.679 * x2 * x3) + (0.00634 * (x3 ** 2)) - (148475.938)
    return Ans

def succesful():
    ans_screen = Toplevel(screen)
    ans_screen.title("Success")
    ans_screen.geometry("300x200")
    value = answer()
    Label(ans_screen, text=value).pack()
    Label(ans_screen, text="The Co2 Gas Percentage : ").pack()
    value2 = getans()
    Label(ans_screen, text=value2).pack()


def main():
    global entry1, entry2, entry3, screen
    global x, y, z
    screen = Tk()
    screen.title("predictor tool")
    screen.geometry("600x600")
    Label(screen, text="CO2 Concentration Predictor Inside a Car Cabin:", font=('Georgia', 20, 'bold italic'), fg='black').pack()
    Label(screen,text="").pack()
    x = StringVar()
    Label(screen,text="Relative humidity in % : ",fg='red',font=("Georgia",14,'bold')).pack()
    entry1 = Entry(screen,width=10, textvariable=x).pack()
    Label(screen,text="").pack()
    y = StringVar()
    Label(screen,text="Temperature in Celsius :",fg='red',font=("Georgia",14,'bold')).pack()
    entry2 = Entry(screen,width=10, textvariable=y).pack()
    Label(screen,text="").pack()
    z = StringVar()
    Label(screen,text="Exposure time (in seconds)  :",fg='red',font=("Georgia",14,'bold')).pack()
    entry3 = Entry(screen,width=10, textvariable=z).pack()
    Label(screen,text="").pack()
    Label(screen,text="----------------------").pack()
    Label(screen,text="").pack()
    Button(screen,text='Calculate',height=1,width=10,fg='black',activeforeground='red',command=succesful).pack()
    screen.mainloop()

main()
