from tkinter import *

root = Tk()
root.title("MyFirstCalc")
icon = PhotoImage(file="Images/icon.png")
root.iconphoto(False, icon)


#Global Variables
global flag
global Result
global memory
flag = 0
Result = 0
memory = 0

'''
Notes : 
1. Flag = 0 is for Addition and Subtraction
2. Flag = 1 is for Multiplication 
3. Flag = 2 is for Division
4. Flag and Result are global variables and can be used in all functions after defining in them
'''
#------------------------------------------------------Functions-----------------------------------------------------#
#Showing Number onto Display
def btn_click(number):
    global flag
    if InputField.get() == '0' and type(number) == int:
        InputField.delete(0, END)
        InputField.insert(0, int(number))
        flag = 0
    elif type(number) == int:
        if flag != 3:
            InputField.insert(END, int(number))
        else:
            InputField.delete(0, END)
            InputField.insert(0, int(number))
            flag = 0

#Adding Number to Previous Result(By Default Result is Zero)-------------------------------------------------------
def btn_add():
    global Result
    global flag
    if InputField.get() == '':
        pass
    elif flag == 0 or flag == 3:
        Result += float(InputField.get())
        InputField.delete(0, END)
    elif flag == 1:
        try:
            Result *= float(InputField.get())
        except:
            Result = 0
        InputField.delete(0, END)
        flag = 0
    elif flag == 2:
        if float(InputField.get()) == 0:
            InputField.delete(0, END)
            InputField.insert(0, 'Error')
        else:
            Result /= float(InputField.get())
            InputField.delete(0, END)
            flag = 0


#Subtracting Number from Previous Result(By Default Result is Zero)-------------------------------------------------
def btn_sub():
    global Result
    global flag
    if InputField.get() == '':
        pass
    elif flag == 0:
        try:
            Result += float(InputField.get())
        except:
            Result = float(InputField.get())
        InputField.delete(0, END)
        InputField.insert(0, '-')
    elif flag == 1:
        try:
            Result *= float(InputField.get())
        except:
            Result = 0
        InputField.delete(0, END)
        InputField.insert(0, '-')
        flag = 0
    elif flag == 2:
        if float(InputField.get()) == 0:
            InputField.delete(0, END)
            InputField.insert(0, 'Error')
            flag = 3
        else:
            Result /= float(InputField.get())
            InputField.delete(0, END)
            InputField.insert(0, '-')
            flag = 0


#Multipy the Sum by Upcoming Number--------------------------------------------------------------------------------
def btn_mul():
    global Result
    global flag
    if flag == 0:
        last_num = float(InputField.get())
        InputField.delete(0, END)
        Result += last_num
        flag = 1
    elif flag == 1:
        last_num = float(InputField.get())
        InputField.delete(0, END)
        Result *= last_num
        flag = 1
    elif flag == 2:
        last_num = float(InputField.get())
        InputField.delete(0, END)
        Result /= last_num
        flag = 1


#Divide Sum by Upcoming Number--------------------------------------------------------------------------------------
def btn_div():
    global Result
    global flag

    if flag == 0:
        last_num = float(InputField.get())
        InputField.delete(0, END)
        Result += last_num
        flag = 2
    elif flag == 1:
        last_num = float(InputField.get())
        InputField.delete(0, END)
        Result *= last_num
        flag = 2
    elif flag == 2:
        last_num = float(InputField.get())
        InputField.delete(0, END)
        Result /= last_num
        flag = 2


#Shows Final Result------------------------------------------------------------------------------------------------
def btn_eql():
    global Result
    global flag
    if InputField.get() == '':
        pass
    elif flag == 0 or flag == 3:
        Result += float(InputField.get())
        if Result == int(Result):
            InputField.delete(0, END)
            InputField.insert(0, int(Result))
        else:
            InputField.delete(0, END)
            InputField.insert(0, Result)
    elif flag == 1:
        Result *= float(InputField.get())
        if Result == int(Result):
            InputField.delete(0, END)
            InputField.insert(0, int(Result))
        else:
            InputField.delete(0, END)
            InputField.insert(0, Result)
    elif flag == 2:
        if float(InputField.get()) == 0:
            InputField.delete(0, END)
            InputField.insert(0, 'ERROR')
        else:
            Result /= float(InputField.get())
            if Result == int(Result):
                InputField.delete(0, END)
                InputField.insert(0, int(Result))
            else:
                InputField.delete(0, END)
                InputField.insert(0, Result)
    elif flag == 4:
        return
    Result = 0
    flag = 3


#Change the sign of number in Display Box------------------------------------------------------------------------
def btn_sign():
    x = (float(InputField.get())) * -1
    if x == int(x):
        InputField.delete(0, END)
        InputField.insert(0, int(x))
    else:
        InputField.delete(0, END)
        InputField.insert(0, x)


#Add Decimal in Display box--------------------------------------------------------------------------------------
def btn_dec():
    if '.' not in InputField.get():
        InputField.insert(END, '.')


#Delete Last Number----------------------------------------------------------------------------------------------
def btn_del():
    if flag != 3:
        x = InputField.get()
        InputField.delete(0, END)
        InputField.insert(0, x[0:-1])
    else:
        InputField.delete(0, END)
        InputField.insert(0, 0)


# Clear Display--------------------------------------------------------------------------------------------------
def btn_clr():
    InputField.delete(0, END)
    InputField.insert(0, 0)


#Resets Calculator----------------------------------------------------------------------------------------------
def btn_ce():
    global Result
    Result = 0
    InputField.delete(0, END)
    InputField.insert(0, 0)

#Memory Functions-----------------------------------------------------------------------------------------------
def btn_mp():
    global memory
    try:
        memory += float(InputField.get())
    except:
        memory = float(InputField.get())
    InputField.delete(0, END)


def btn_mm():
    global memory
    memory += (float(InputField.get())) * -1
    InputField.delete(0, END)


def btn_mr():
    global memory
    if memory == int(memory):
        InputField.delete(0, END)
        InputField.insert(0, int(memory))
    else:
        InputField.delete(0, END)
        InputField.insert(0, memory)


def btn_mc():
    global memory
    memory = 0


#Inverse-----------------------------------------------------------------------------------------------------------
def btn_xby():
    x = 1 / float(InputField.get())
    if x == int(x):
        InputField.delete(0, END)
        InputField.insert(0, int(x))
    else:
        InputField.delete(0, END)
        InputField.insert(0, x)


#Square----------------------------------------------------------------------------------------------------------
def btn_xsq():
    x = float(InputField.get()) ** 2
    if x == int(x):
        InputField.delete(0, END)
        InputField.insert(0, int(x))
    else:
        InputField.delete(0, END)
        InputField.insert(0, x)


#Square Root-----------------------------------------------------------------------------------------------------
def btn_xrt():
    x = float(InputField.get()) ** (1/2)
    if x == int(x):
        InputField.delete(0, END)
        InputField.insert(0, int(x))
    else:
        InputField.delete(0, END)
        InputField.insert(0, x)


def btn_mod():
    global Result
    global flag
    if flag == 0:
        last_num = float(InputField.get())
        InputField.delete(0, END)
        Result += last_num
        flag = 4
    elif flag == 1:
        last_num = float(InputField.get())
        InputField.delete(0, END)
        Result *= last_num
        flag = 4
    elif flag == 2:
        last_num = float(InputField.get())
        InputField.delete(0, END)
        Result /= last_num
        flag = 4


#----------------------------------------------Body of Calculator---------------------------------------------------#
InputField = Entry(root, width=26, bd=0, font=("arial", 35), bg = "#f1f1f0", fg = "black", justify=RIGHT)
InputField.insert(0, 0)
InputField.bind("<Key>", lambda e: "break")
InputField.grid(row=1, column=0, columnspan=4, padx=20)

#Creating Images Labels
img0 = PhotoImage(file="Images/0.png").subsample(2,2)
img1 = PhotoImage(file="Images/1.png").subsample(2,2)
img2 = PhotoImage(file="Images/2.png").subsample(2,2)
img3 = PhotoImage(file="Images/3.png").subsample(2,2)
img4 = PhotoImage(file="Images/4.png").subsample(2,2)
img5 = PhotoImage(file="Images/5.png").subsample(2,2)
img6 = PhotoImage(file="Images/6.png").subsample(2,2)
img7 = PhotoImage(file="Images/7.png").subsample(2,2)
img8 = PhotoImage(file="Images/8.png").subsample(2,2)
img9 = PhotoImage(file="Images/9.png").subsample(2,2)
imgmod = PhotoImage(file="Images/mod.png").subsample(2, 2)
imgp = PhotoImage(file="Images/+.png").subsample(2,2)
imgm = PhotoImage(file="Images/-.png").subsample(2,2)
imgx = PhotoImage(file="Images/x.png").subsample(2,2)
imgd = PhotoImage(file="Images/d.png").subsample(2,2)
imgeq = PhotoImage(file="Images/=.png").subsample(2,2)
imgdec = PhotoImage(file="Images/..png").subsample(2,2)
imgac = PhotoImage(file="Images/ac.png").subsample(2,2)
imgc = PhotoImage(file="Images/c.png").subsample(2,2)
imgmp = PhotoImage(file="Images/m+.png").subsample(2,2)
imgmm = PhotoImage(file="Images/m-.png").subsample(2,2)
imgmc = PhotoImage(file="Images/mc.png").subsample(2,2)
imgmr = PhotoImage(file="Images/mr.png").subsample(2,2)
imgsign = PhotoImage(file="Images/sign.png").subsample(2,2)
imgdel = PhotoImage(file="Images/del.png").subsample(3,3)
imgxby = PhotoImage(file="Images/xby.png").subsample(2,2)
imgxsq = PhotoImage(file="Images/xsq.png").subsample(2,2)
imgxrt = PhotoImage(file="Images/xrt.png").subsample(2,2)
imgxcrt = PhotoImage(file="Images/xcrt.png").subsample(2,2)
imgxf = PhotoImage(file="Images/x!.png").subsample(2,2)


#Creating Buttons For Calculator
btn1 = Button(root, image=img1, padx=20, pady=20, bg="black", command=lambda: btn_click(1))
btn2 = Button(root, image=img2, padx=20, pady=20, bg="black", command=lambda: btn_click(2))
btn3 = Button(root, image=img3, padx=20, pady=20, bg="black", command=lambda: btn_click(3))
btn4 = Button(root, image=img4, padx=20, pady=20, bg="black", command=lambda: btn_click(4))
btn5 = Button(root, image=img5, padx=20, pady=20, bg="black", command=lambda: btn_click(5))
btn6 = Button(root, image=img6, padx=20, pady=20, bg="black", command=lambda: btn_click(6))
btn7 = Button(root, image=img7, padx=20, pady=20, bg="black", command=lambda: btn_click(7))
btn8 = Button(root, image=img8, padx=20, pady=20, bg="black", command=lambda: btn_click(8))
btn9 = Button(root, image=img9, padx=20, pady=20, bg="black", command=lambda: btn_click(9))
btn0 = Button(root, image=img0, padx=20, pady=20, bg="black", command=lambda: btn_click(0))

btnmod = Button(root, image=imgmod, padx=20, pady=20, bg="black", command=btn_mod)
btnxby = Button(root, image=imgxby, padx=20, pady=20, bg="black", command=btn_xby)
btnxsq = Button(root, image=imgxsq, padx=20, pady=20, bg="black", command=btn_xsq)
btnxrt = Button(root, image=imgxrt, padx=20, pady=20, bg="black", command=btn_xrt)

btnadd = Button(root, image=imgp, padx=20, pady=20, bg="black", command=btn_add)
btnsub = Button(root, image=imgm, padx=21, pady=20, bg="black", command=btn_sub)
btnmul = Button(root, image=imgx, padx=20, pady=20, bg="black", command=btn_mul)
btndiv = Button(root, image=imgd, padx=21, pady=20, bg="black", command=btn_div)

btnclr = Button(root, image=imgc, padx=20, pady=20, bg="black", command=btn_clr)
btnce = Button(root, image=imgac, padx=16, pady=20, bg="black", command=btn_ce)
btndel = Button(root, image=imgdel, padx=14, pady=20, bg="black", command=btn_del)

btneql = Button(root, image=imgeq, padx=20, pady=20, bg="black", command=btn_eql)
btndec = Button(root, image=imgdec, padx=21, pady=20, bg="black", command=btn_dec)
btnsign = Button(root, image=imgsign, padx=14, pady=20, bg="black", command=btn_sign)

btnmp = Button(root, image=imgmp, padx=16, pady=20, bg="black", command=btn_mp)
btnmm = Button(root, image=imgmm, padx=18, pady=20, bg="black", command=btn_mm)
btnmr = Button(root, image=imgmr, padx=16, pady=20, bg="black", command=btn_mr)
btnmc = Button(root, image=imgmc, padx=16, pady=20, bg="black", command=btn_mc)

#Configure
root.geometry("400x500")

for i in range(1,9):
    for j in range(4):
        Grid.rowconfigure(root, i, weight=1)
        Grid.columnconfigure(root, j, weight=1)


#Positining the Buttons
btnmc.grid(row=2, column=0, sticky="NSEW")
btnmr.grid(row=2, column=1, sticky="NSEW")
btnmp.grid(row=2, column=2, sticky="NSEW")
btnmm.grid(row=2, column=3, sticky="NSEW")

btnce.grid(row=3, column=0, sticky="NSEW")
btnclr.grid(row=3, column=1, sticky="NSEW")
btndel.grid(row=3, column=2, sticky="NSEW")
btnsign.grid(row=3, column=3, sticky="NSEW")

btnxby.grid(row=4, column=0, sticky="NSEW")
btnxsq.grid(row=4, column=1, sticky="NSEW")
btnxrt.grid(row=4, column=2, sticky="NSEW")
btndiv.grid(row=4, column=3, sticky="NSEW")

btn7.grid(row=5, column=0, sticky="NSEW")
btn8.grid(row=5, column=1, sticky="NSEW")
btn9.grid(row=5, column=2, sticky="NSEW")
btnmul.grid(row=5, column=3, sticky="NSEW")

btn4.grid(row=6, column=0, sticky="NSEW")
btn5.grid(row=6, column=1, sticky="NSEW")
btn6.grid(row=6, column=2, sticky="NSEW")
btnsub.grid(row=6, column=3, sticky="NSEW")

btn1.grid(row=7, column=0, sticky="NSEW")
btn2.grid(row=7, column=1, sticky="NSEW")
btn3.grid(row=7, column=2, sticky="NSEW")
btnadd.grid(row=7, column=3, sticky="NSEW")

btnmod.grid(row=8, column=0, sticky="NSEW")
btn0.grid(row=8, column=1, sticky="NSEW")
btndec.grid(row=8, column=2, sticky="NSEW")
btneql.grid(row=8, column=3, sticky="NSEW")



root.mainloop()
