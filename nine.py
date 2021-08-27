from math import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from tkinter import *
import matplotlib.pyplot as plt
import numpy

root = Tk()
root.title('Полет тела')
g = 9.80665
dx = 0.01
v = IntVar()
an = IntVar()
x0 = IntVar()
y0 = IntVar()
v2 = IntVar()
an2 = IntVar()
x02 = IntVar()
y02 = IntVar()
v3 = IntVar()
an3 = IntVar()
x03 = IntVar()
y03 = IntVar()
xmax = IntVar()
xmax2 = IntVar()
xmax3 = IntVar()
t = IntVar()
t2 = IntVar()
t3 = IntVar()
hmax = IntVar()
hmax2 = IntVar()
hmax3 = IntVar()



def func(x0, v, y0, an):
    y = x0 * tan(an) - (1 / (2 * v ** 2)) * ((g * x0 ** 2) / (cos(an) ** 2)) + y0
    if y == 0:
        return 0.0
    return y


def func2(x02, v2, y02, an2):
    y2 = x02 * tan(an2) - (1 / (2 * v2 ** 2)) * ((g * x02 ** 2) / (cos(an2) ** 2)) + y02
    if y2 == 0:
        return 0.0
    return y2


def func3(x03, v3, y03, an3):
    y3 = x03 * tan(an3) - (1 / (2 * v3 ** 2)) * ((g * x03 ** 2) / (cos(an3) ** 2)) + y03
    if y3 == 0:
        return 0.0
    return y3

def analysis():
    v = int(entry1.get())
    an = int(entry2.get())
    x0 = int(entry3.get())
    y0 = int(entry4.get())
    v2 = int(entry5.get())
    an2 = int(entry6.get())
    x02 = int(entry7.get())
    y02 = int(entry8.get())
    v3 = int(entry9.get())
    an3 = int(entry10.get())
    x03 = int(entry11.get())
    y03 = int(entry12.get())
    an = radians(an)
    an2 = radians(an2)
    an3 = radians(an3)

    t = 2 * v * sin(an) / g
    t2 = 2 * v2 * sin(an2) / g
    t3 = 2 * v3 * sin(an3) / g
    xmax = (v**2/g) * 2 * sin(an) * cos(an)
    xmax2 =  (v2**2/g) * 2 * sin(an2) * cos(an2)
    xmax3 = (v3**2/g) * 2 * sin(an3) * cos(an3)
    hmax = (v**2 / (2 * g)) * sin(an)**2
    hmax2 = (v2**2 / (2 * g)) * sin(an2)**2
    hmax3 = (v3**2 / (2 * g)) * sin(an3)**2

    dp1o.config(text=round(xmax,2))
    dp2o.config(text=round(xmax2,2))
    dp3o.config(text=round(xmax3,2))
    hm1o.config(text=round(hmax,2))
    hm2o.config(text=round(hmax2,2))
    hm3o.config(text=round(hmax3,2))
    timo.config(text=round(t,2))
    tim2o.config(text=round(t2,2))
    tim3o.config(text=round(t3,2))



    xlist = numpy.arange(x0, xmax, dx)
    xlist2 = numpy.arange(x02, xmax2, dx)
    xlist3 = numpy.arange(x03, xmax3, dx)

    ylist = [func(x0, v, y0, an) for x0 in xlist]
    ylist2 = [func2(x02, v2, y02, an2) for x02 in xlist2]
    ylist3 = [func3(x03, v3, y03, an3) for x03 in xlist3]


    def plot():
        a.cla()

        a.plot(xlist, ylist, color='red')
        a.plot(xlist2, ylist2, color='green')
        a.plot(xlist3, ylist3, color='blue')
        canvas.get_tk_widget().pack(side=TOP)
        canvas._tkcanvas.pack(side=TOP)


    plot()



topp = Label(root)
topp.pack(side='top')
first = LabelFrame(topp, text='Данные для 1 графика(красный)')
first.pack(side='left')

second = Label(first, text='Начальная скорость')
second.pack()

entry1 = Entry(first, width=10, textvariable=v)
entry1.pack()

third = Label(first, text='Угол выстрела')
third.pack()

entry2 = Entry(first, width=10, textvariable=an)
entry2.pack()

fourth = Label(first, text='Начальная координата x')
fourth.pack()

entry3 = Entry(first, width=10, textvariable=x0)
entry3.pack()

fifth = Label(first, text='Начальная координата y')
fifth.pack()

entry4 = Entry(first, width=10, textvariable=y0)
entry4.pack()

secondb = LabelFrame(topp, text='Данные для 2 графика(зеленый)')
secondb.pack(side='left')

second = Label(secondb, text='Начальная скорость')
second.pack()

entry5 = Entry(secondb, width=10, textvariable=v2)
entry5.pack()

third = Label(secondb, text='Угол выстрела')
third.pack()

entry6 = Entry(secondb, width=10, textvariable=an2)
entry6.pack()

fourth = Label(secondb, text='Начальная координата x')
fourth.pack()

entry7 = Entry(secondb, width=10, textvariable=x02)
entry7.pack()

fifth = Label(secondb, text='Начальная координата y')
fifth.pack()

entry8 = Entry(secondb, width=10, textvariable=y02)
entry8.pack()

thirdb = LabelFrame(topp, text='Данные для 3 графика(синий)')
thirdb.pack(side='left')

second = Label(thirdb, text='Начальная скорость')
second.pack()

entry9 = Entry(thirdb, width=10, textvariable=v3)
entry9.pack()

third = Label(thirdb, text='Угол выстрела')
third.pack()

entry10 = Entry(thirdb, width=10, textvariable=an3)
entry10.pack()

fourth = Label(thirdb, text='Начальная координата x')
fourth.pack()

entry11 = Entry(thirdb, width=10, textvariable=x03)
entry11.pack()

fifth = Label(thirdb, text='Начальная координата y')
fifth.pack()

entry12 = Entry(thirdb, width=10, textvariable=y03)
entry12.pack()

f = Figure()
canvas = FigureCanvasTkAgg(f)
FigureCanvasTkAgg.draw
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
a = f.add_subplot(111)


first = LabelFrame(topp, text='Расчет')
first.pack(side='bottom')
button = Button(first, text="Сгенерировать", command=analysis)
button.pack(side='top')
firstr = LabelFrame(first, text='Данные первого графика(красного)')
firstr.pack(side='left')
dp1 = Label(firstr, text='Дальность полета 1 тела')
dp1.pack()
dp1o = Label(firstr, text='')
dp1o.pack()
hm1 = Label(firstr, text='Максимальная высота полета 1 тела')
hm1.pack()
hm1o = Label(firstr, text='')
hm1o.pack()
tim = Label(firstr, text='Время полета 1 тела')
tim.pack()
timo = Label(firstr, text='')
timo.pack()
secondr = LabelFrame(first, text='Данные второго графика(зеленого)')
secondr.pack(side='left')
dp2 = Label(secondr, text='Дальность полета 2 тела')
dp2.pack()
dp2o = Label(secondr, text='')
dp2o.pack()
hm2 = Label(secondr, text='Максимальная высота полета 2 тела')
hm2.pack()
hm2o = Label(secondr, text='')
hm2o.pack()
tim2 = Label(secondr, text='Время полета 2 тела')
tim2.pack()
tim2o = Label(secondr, text='')
tim2o.pack()
thirdr = LabelFrame(first, text='Данные третьего графика(синего)')
thirdr.pack(side='left')
dp3 = Label(thirdr, text='Дальность полета 3 тела')
dp3.pack()
dp3o = Label(thirdr, text='')
dp3o.pack()
hm3 = Label(thirdr, text='Максимальная высота полета 3 тела')
hm3.pack()
hm3o = Label(thirdr, text='')
hm3o.pack()
tim3 = Label(thirdr, text='Время полета 3 тела')
tim3.pack()
tim3o = Label(thirdr, text='')
tim3o.pack()

root.mainloop()










