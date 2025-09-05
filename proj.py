import sys
import numpy as np
from PIL import ImageTk,Image
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
from temp import ep
from knn import kn
from svm import sa
from nbc import nb

def buttons():
    ageo=top.Text1.get("1.0",'end-1c')
    if ageo=="":
        ageo=0.0
    else:
        ageo=float(ageo)
    bpo=top.Text2.get("1.0",'end-1c')
    if bpo=="":
        bpo=0.0
    else:
        bpo=float(bpo)
    sgo=top.Text3.get("1.0",'end-1c')
    if sgo=="":
        sgo=0.0
    else:
        sgo=float(sgo)
    alo=top.Text4.get("1.0",'end-1c')
    if alo=="":
        alo=0.0
    else:
        alo=float(alo)
    suo=top.Text5.get("1.0",'end-1c')
    if suo=="":
        suo=0.0
    else:
        suo=float(suo)
    bgro=top.Text6.get("1.0",'end-1c')
    if bgro=="":
        bgro=0.0
    else:
        bgro=float(bgro)
    buo=top.Text7.get("1.0",'end-1c')
    if buo=="":
        buo=0.0
    else:
        buo=float(buo)
    sco=top.Text8.get("1.0",'end-1c')
    if sco=="":
        sco=0.0
    else:
        sco=float(sco)
    sodo=top.Text9.get("1.0",'end-1c')
    if sodo=="":
        sodo=0.0
    else:
        sodo=float(sodo)
    poto=top.Text10.get("1.0",'end-1c')
    if poto=="":
        poto=0.0
    else:
        poto=float(poto)
    hemoo=top.Text11.get("1.0",'end-1c')
    if hemoo=="":
        hemoo=0.0
    else:
        hemoo=float(hemoo)
    pcvo=top.Text12.get("1.0",'end-1c')
    if pcvo=="":
        pcvo=0.0
    else:
        pcvo=float(pcvo)
    wbcco=top.Text13.get("1.0",'end-1c')
    if wbcco=="":
        wbcco=0.0
    else:
        wbcco=float(wbcco)
    rbcco=top.Text14.get("1.0",'end-1c')
    if rbcco=="":
        rbcco=0.0
    else:
        rbcco=float(rbcco)
    rbco=top.Text15.get("1.0",'end-1c')
    if rbco=="":
        rbco=0.0
    else:
        rbco=float(rbco)
    pco=top.Text16.get("1.0",'end-1c')
    if pco=="":
        pco=0.0
    else:
        pco=float(pco)
    pcco=top.Text17.get("1.0",'end-1c')
    if pcco=="":
        pcco=0.0
    else:
        pcco=float(pcco)
    bao=top.Text18.get("1.0",'end-1c')
    if bao=="":
        bao=0.0
    else:
        bao=float(bao)
    htno=top.Text19.get("1.0",'end-1c')
    if htno=="":
        htno=0.0
    else:
        htno=float(htno)
    dmo=top.Text20.get("1.0",'end-1c')
    if dmo=="":
        dmo=0.0
    else:
        dmo=float(dmo)
    cado=top.Text21.get("1.0",'end-1c')
    if cado=="":
        cado=0.0
    else:
        cado=float(cado)
    appeto=top.Text22.get("1.0",'end-1c')
    if appeto=="":
        appeto=0.0
    else:
        appeto=float(appeto)
    peo=top.Text23.get("1.0",'end-1c')
    if peo=="":
        peo=0.0
    else:
        peo=float(peo)
    aneo=top.Text24.get("1.0",'end-1c')
    if aneo=="":
        aneo=0.0
    else:
        aneo=float(aneo)
    sarr=[[ageo,bpo,sgo,alo,suo,bgro,buo,sco,sodo,poto,hemoo,pcvo,wbcco,rbcco,rbco,pco,pcco,bao,htno,dmo,cado,appeto,peo,aneo]]
    print(sarr)
    return sarr

def create_window():
    window=tk.Toplevel()
    window.title("Result")
    window.geometry = ("1000000, 1000000")
    output = ep(buttons())
    outputnum =tk.Label(window,height=5,width=25,text=str(output[0]))
    outputnum.pack()
    outputnum1 =tk.Label(window,height=5,width=25,text=str(output[1]))
    outputnum1.pack()
    outputnum2 =tk.Label(window,height=5,width=50,text=str(output[2]))
    outputnum2.pack()
    button4 = tk.Button(window, text="close",height=5,width=25,command=window.destroy)
    button4.place()
    button4.pack()
def create_window1():
    window=tk.Toplevel()
    window.title("Result")
    window.geometry = ("1000000, 1000000")
    output = kn(buttons())
    outputnum =tk.Label(window,height=5,width=25,text= str(output[0]))
    outputnum.pack()
    outputnum1 =tk.Label(window,height=5,width=25,text=str(output[1]))
    outputnum1.pack()
    outputnum2 =tk.Label(window,height=5,width=50,text=str(output[2]))
    outputnum2.pack()
    button4 =tk.Button(window, text="close",height=5,width=25,command=window.destroy)
    button4.place()
    button4.pack()
def create_window2():
    window=tk.Toplevel()
    window.title("Result")
    window.geometry = ("1000000, 1000000")
    output = nb(buttons())
    outputnum =tk.Label(window,height=5,width=25,text= str(output[0]))
    outputnum.pack()
    outputnum1 =tk.Label(window,height=5,width=25,text=str(output[1]))
    outputnum1.pack()
    outputnum2 =tk.Label(window,height=5,width=50,text=str(output[2]))
    outputnum2.pack()
    button4 =tk.Button(window, text="close",height=5,width=25,command=window.destroy)
    button4.place()
    button4.pack()
    
def create_window3():
    window=tk.Toplevel()
    window.title("Result")
    window.geometry = ("1000000, 1000000")
    output = sa(buttons())
    outputnum = tk.Label(window,height=5,width=250,text= str(output[0]))
    outputnum.pack()
    outputnum1 =tk.Label(window,height=5,width=25,text=str(output[1]))
    outputnum1.pack()
    outputnum2 =tk.Label(window,height=5,width=50,text=str(output[2]))
    outputnum2.pack()
    button4 = tk.Button(window, text="close",height=5,width=25,command=window.destroy)
    button4.place()
    button4.pack()

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    global top 
    top = Toplevel1 (root)
    root.title("CKD")
    #proj_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    #proj_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
          top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        top.geometry("600x450+650+150")
        top.title("CKD")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.0, rely=-0.022, relheight=1.029
                , relwidth=1.005)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        #bg_image=tk.PhotoImage(file=r'C:\Users\Akash\Desktop\Project\background2.png')
        #bg_image=bg_image.zoom(5)
        #self.Canvas1.pack(side='top',fill='both',expand='yes')
        #self.Canvas1.create_image(0,0,image=tk.PhotoImage(file=r'C:\Users\Akash\Desktop\Project\background2.png'),anchor='nw')

        self.Label1 = tk.Label(self.Canvas1)
        self.Label1.place(relx=0.066, rely=0.043, height=21, width=27)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Age''')

        self.Label2 = tk.Label(self.Canvas1)
        self.Label2.place(relx=0.017, rely=0.13, height=21, width=84)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Blood Pressure''')

        self.Label3 = tk.Label(self.Canvas1)
        self.Label3.place(relx=0.017, rely=0.216, height=21, width=86)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Specific gravity''')

        self.Label4 = tk.Label(self.Canvas1)
        self.Label4.place(relx=0.05, rely=0.324, height=21, width=52)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Albumin''')

        self.Label5 = tk.Label(self.Canvas1)
        self.Label5.place(relx=0.05, rely=0.432, height=21, width=36)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Sugar''')

        self.Label6 = tk.Label(self.Canvas1)
        self.Label6.place(relx=0.033, rely=0.54, height=21, width=82)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Blood Glucose''')

        self.Label7 = tk.Label(self.Canvas1)
        self.Label7.place(relx=0.033, rely=0.626, height=21, width=64)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''Blood Urea''')

        self.Label8 = tk.Label(self.Canvas1)
        self.Label8.place(relx=0.017, rely=0.734, height=21, width=104)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''Sodium Creatinine''')

        self.Text1 = tk.Text(self.Canvas1)
        self.Text1.place(relx=0.182, rely=0.043, relheight=0.052, relwidth=0.106)

        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(wrap="word")

        self.Text2 = tk.Text(self.Canvas1)
        self.Text2.place(relx=0.182, rely=0.13, relheight=0.052, relwidth=0.106)
        self.Text2.configure(background="white")
        self.Text2.configure(font="TkTextFont")
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#d9d9d9")
        self.Text2.configure(highlightcolor="black")
        self.Text2.configure(insertbackground="black")
        self.Text2.configure(selectbackground="#c4c4c4")
        self.Text2.configure(selectforeground="black")
        self.Text2.configure(wrap="word")

        self.Text3 = tk.Text(self.Canvas1)
        self.Text3.place(relx=0.182, rely=0.216, relheight=0.052, relwidth=0.106)

        self.Text3.configure(background="white")
        self.Text3.configure(font="TkTextFont")
        self.Text3.configure(foreground="black")
        self.Text3.configure(highlightbackground="#d9d9d9")
        self.Text3.configure(highlightcolor="black")
        self.Text3.configure(insertbackground="black")
        self.Text3.configure(selectbackground="#c4c4c4")
        self.Text3.configure(selectforeground="black")
        self.Text3.configure(wrap="word")

        self.Text4 = tk.Text(self.Canvas1)
        self.Text4.place(relx=0.182, rely=0.324, relheight=0.052, relwidth=0.106)

        self.Text4.configure(background="white")
        self.Text4.configure(font="TkTextFont")
        self.Text4.configure(foreground="black")
        self.Text4.configure(highlightbackground="#d9d9d9")
        self.Text4.configure(highlightcolor="black")
        self.Text4.configure(insertbackground="black")
        self.Text4.configure(selectbackground="#c4c4c4")
        self.Text4.configure(selectforeground="black")
        self.Text4.configure(wrap="word")

        self.Text5 = tk.Text(self.Canvas1)
        self.Text5.place(relx=0.182, rely=0.432, relheight=0.052, relwidth=0.106)

        self.Text5.configure(background="white")
        self.Text5.configure(font="TkTextFont")
        self.Text5.configure(foreground="black")
        self.Text5.configure(highlightbackground="#d9d9d9")
        self.Text5.configure(highlightcolor="black")
        self.Text5.configure(insertbackground="black")
        self.Text5.configure(selectbackground="#c4c4c4")
        self.Text5.configure(selectforeground="black")
        self.Text5.configure(wrap="word")

        self.Text6 = tk.Text(self.Canvas1)
        self.Text6.place(relx=0.182, rely=0.54, relheight=0.052, relwidth=0.106)
        self.Text6.configure(background="white")
        self.Text6.configure(font="TkTextFont")
        self.Text6.configure(foreground="black")
        self.Text6.configure(highlightbackground="#d9d9d9")
        self.Text6.configure(highlightcolor="black")
        self.Text6.configure(insertbackground="black")
        self.Text6.configure(selectbackground="#c4c4c4")
        self.Text6.configure(selectforeground="black")
        self.Text6.configure(wrap="word")

        self.Text7 = tk.Text(self.Canvas1)
        self.Text7.place(relx=0.182, rely=0.626, relheight=0.052, relwidth=0.106)

        self.Text7.configure(background="white")
        self.Text7.configure(font="TkTextFont")
        self.Text7.configure(foreground="black")
        self.Text7.configure(highlightbackground="#d9d9d9")
        self.Text7.configure(highlightcolor="black")
        self.Text7.configure(insertbackground="black")
        self.Text7.configure(selectbackground="#c4c4c4")
        self.Text7.configure(selectforeground="black")
        self.Text7.configure(wrap="word")

        self.Text8 = tk.Text(self.Canvas1)
        self.Text8.place(relx=0.216, rely=0.734, relheight=0.052, relwidth=0.106)

        self.Text8.configure(background="white")
        self.Text8.configure(font="TkTextFont")
        self.Text8.configure(foreground="black")
        self.Text8.configure(highlightbackground="#d9d9d9")
        self.Text8.configure(highlightcolor="black")
        self.Text8.configure(insertbackground="black")
        self.Text8.configure(selectbackground="#c4c4c4")
        self.Text8.configure(selectforeground="black")
        self.Text8.configure(wrap="word")

        self.Label9 = tk.Label(self.Canvas1)
        self.Label9.place(relx=0.348, rely=0.043, height=21, width=47)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(highlightbackground="#d9d9d9")
        self.Label9.configure(highlightcolor="black")
        self.Label9.configure(text='''Sodium''')

        self.Label10 = tk.Label(self.Canvas1)
        self.Label10.place(relx=0.348, rely=0.13, height=21, width=60)
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(activeforeground="black")
        self.Label10.configure(background="#d9d9d9")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(highlightbackground="#d9d9d9")
        self.Label10.configure(highlightcolor="black")
        self.Label10.configure(text='''Pottasium''')

        self.Label11 = tk.Label(self.Canvas1)
        self.Label11.place(relx=0.348, rely=0.216, height=21, width=79)
        self.Label11.configure(activebackground="#f9f9f9")
        self.Label11.configure(activeforeground="black")
        self.Label11.configure(background="#d9d9d9")
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(highlightbackground="#d9d9d9")
        self.Label11.configure(highlightcolor="black")
        self.Label11.configure(text='''Heamoglobin''')

        self.Label12 = tk.Label(self.Canvas1)
        self.Label12.place(relx=0.348, rely=0.324, height=21, width=65)
        self.Label12.configure(activebackground="#f9f9f9")
        self.Label12.configure(activeforeground="black")
        self.Label12.configure(background="#d9d9d9")
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(highlightbackground="#d9d9d9")
        self.Label12.configure(highlightcolor="black")
        self.Label12.configure(text='''Packed cell''')

        self.Label13 = tk.Label(self.Canvas1)
        self.Label13.place(relx=0.348, rely=0.432, height=21, width=68)
        self.Label13.configure(activebackground="#f9f9f9")
        self.Label13.configure(activeforeground="black")
        self.Label13.configure(background="#d9d9d9")
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(foreground="#000000")
        self.Label13.configure(highlightbackground="#d9d9d9")
        self.Label13.configure(highlightcolor="black")
        self.Label13.configure(text='''WBC Count''')

        self.Label14 = tk.Label(self.Canvas1)
        self.Label14.place(relx=0.348, rely=0.54, height=21, width=64)
        self.Label14.configure(activebackground="#f9f9f9")
        self.Label14.configure(activeforeground="black")
        self.Label14.configure(background="#d9d9d9")
        self.Label14.configure(disabledforeground="#a3a3a3")
        self.Label14.configure(foreground="#000000")
        self.Label14.configure(highlightbackground="#d9d9d9")
        self.Label14.configure(highlightcolor="black")
        self.Label14.configure(text='''RBC Count''')

        self.Label15 = tk.Label(self.Canvas1)
        self.Label15.place(relx=0.348, rely=0.626, height=21, width=28)
        self.Label15.configure(activebackground="#f9f9f9")
        self.Label15.configure(activeforeground="black")
        self.Label15.configure(background="#d9d9d9")
        self.Label15.configure(disabledforeground="#a3a3a3")
        self.Label15.configure(foreground="#000000")
        self.Label15.configure(highlightbackground="#d9d9d9")
        self.Label15.configure(highlightcolor="black")
        self.Label15.configure(text='''RBC''')

        self.Text9 = tk.Text(self.Canvas1)
        self.Text9.place(relx=0.464, rely=0.043, relheight=0.052, relwidth=0.106)

        self.Text9.configure(background="white")
        self.Text9.configure(font="TkTextFont")
        self.Text9.configure(foreground="black")
        self.Text9.configure(highlightbackground="#d9d9d9")
        self.Text9.configure(highlightcolor="black")
        self.Text9.configure(insertbackground="black")
        self.Text9.configure(selectbackground="#c4c4c4")
        self.Text9.configure(selectforeground="black")
        self.Text9.configure(wrap="word")

        self.Label16 = tk.Label(self.Canvas1)
        self.Label16.place(relx=0.348, rely=0.713, height=21, width=46)
        self.Label16.configure(activebackground="#f9f9f9")
        self.Label16.configure(activeforeground="black")
        self.Label16.configure(background="#d9d9d9")
        self.Label16.configure(disabledforeground="#a3a3a3")
        self.Label16.configure(foreground="#000000")
        self.Label16.configure(highlightbackground="#d9d9d9")
        self.Label16.configure(highlightcolor="black")
        self.Label16.configure(text='''Pus cell''')

        self.Text10 = tk.Text(self.Canvas1)
        self.Text10.place(relx=0.464, rely=0.13, relheight=0.052, relwidth=0.106)

        self.Text10.configure(background="white")
        self.Text10.configure(font="TkTextFont")
        self.Text10.configure(foreground="black")
        self.Text10.configure(highlightbackground="#d9d9d9")
        self.Text10.configure(highlightcolor="black")
        self.Text10.configure(insertbackground="black")
        self.Text10.configure(selectbackground="#c4c4c4")
        self.Text10.configure(selectforeground="black")
        self.Text10.configure(wrap="word")

        self.Text11 = tk.Text(self.Canvas1)
        self.Text11.place(relx=0.464, rely=0.324, relheight=0.052
                , relwidth=0.106)
        self.Text11.configure(background="white")
        self.Text11.configure(font="TkTextFont")
        self.Text11.configure(foreground="black")
        self.Text11.configure(highlightbackground="#d9d9d9")
        self.Text11.configure(highlightcolor="black")
        self.Text11.configure(insertbackground="black")
        self.Text11.configure(selectbackground="#c4c4c4")
        self.Text11.configure(selectforeground="black")
        self.Text11.configure(wrap="word")

        self.Text12 = tk.Text(self.Canvas1)
        self.Text12.place(relx=0.464, rely=0.216, relheight=0.052
                , relwidth=0.106)
        self.Text12.configure(background="white")
        self.Text12.configure(font="TkTextFont")
        self.Text12.configure(foreground="black")
        self.Text12.configure(highlightbackground="#d9d9d9")
        self.Text12.configure(highlightcolor="black")
        self.Text12.configure(insertbackground="black")
        self.Text12.configure(selectbackground="#c4c4c4")
        self.Text12.configure(selectforeground="black")
        self.Text12.configure(wrap="word")

        self.Text13 = tk.Text(self.Canvas1)
        self.Text13.place(relx=0.464, rely=0.432, relheight=0.052
                , relwidth=0.106)
        self.Text13.configure(background="white")
        self.Text13.configure(font="TkTextFont")
        self.Text13.configure(foreground="black")
        self.Text13.configure(highlightbackground="#d9d9d9")
        self.Text13.configure(highlightcolor="black")
        self.Text13.configure(insertbackground="black")
        self.Text13.configure(selectbackground="#c4c4c4")
        self.Text13.configure(selectforeground="black")
        self.Text13.configure(wrap="word")

        self.Text14 = tk.Text(self.Canvas1)
        self.Text14.place(relx=0.464, rely=0.54, relheight=0.052, relwidth=0.106)

        self.Text14.configure(background="white")
        self.Text14.configure(font="TkTextFont")
        self.Text14.configure(foreground="black")
        self.Text14.configure(highlightbackground="#d9d9d9")
        self.Text14.configure(highlightcolor="black")
        self.Text14.configure(insertbackground="black")
        self.Text14.configure(selectbackground="#c4c4c4")
        self.Text14.configure(selectforeground="black")
        self.Text14.configure(wrap="word")

        self.Text15 = tk.Text(self.Canvas1)
        self.Text15.place(relx=0.464, rely=0.626, relheight=0.052
                , relwidth=0.106)
        self.Text15.configure(background="white")
        self.Text15.configure(font="TkTextFont")
        self.Text15.configure(foreground="black")
        self.Text15.configure(highlightbackground="#d9d9d9")
        self.Text15.configure(highlightcolor="black")
        self.Text15.configure(insertbackground="black")
        self.Text15.configure(selectbackground="#c4c4c4")
        self.Text15.configure(selectforeground="black")
        self.Text15.configure(wrap="word")

        self.Text16 = tk.Text(self.Canvas1)
        self.Text16.place(relx=0.464, rely=0.713, relheight=0.052
                , relwidth=0.106)
        self.Text16.configure(background="white")
        self.Text16.configure(font="TkTextFont")
        self.Text16.configure(foreground="black")
        self.Text16.configure(highlightbackground="#d9d9d9")
        self.Text16.configure(highlightcolor="black")
        self.Text16.configure(insertbackground="black")
        self.Text16.configure(selectbackground="#c4c4c4")
        self.Text16.configure(selectforeground="black")
        self.Text16.configure(wrap="word")

        self.Label17 = tk.Label(self.Canvas1)
        self.Label17.place(relx=0.597, rely=0.043, height=21, width=88)
        self.Label17.configure(activebackground="#f9f9f9")
        self.Label17.configure(activeforeground="black")
        self.Label17.configure(background="#d9d9d9")
        self.Label17.configure(disabledforeground="#a3a3a3")
        self.Label17.configure(foreground="#000000")
        self.Label17.configure(highlightbackground="#d9d9d9")
        self.Label17.configure(highlightcolor="black")
        self.Label17.configure(text='''Pus cell clumps''')

        self.Label18 = tk.Label(self.Canvas1)
        self.Label18.place(relx=0.63, rely=0.151, height=21, width=48)
        self.Label18.configure(activebackground="#f9f9f9")
        self.Label18.configure(activeforeground="black")
        self.Label18.configure(background="#d9d9d9")
        self.Label18.configure(disabledforeground="#a3a3a3")
        self.Label18.configure(foreground="#000000")
        self.Label18.configure(highlightbackground="#d9d9d9")
        self.Label18.configure(highlightcolor="black")
        self.Label18.configure(text='''Bacteria''')

        self.Label19 = tk.Label(self.Canvas1)
        self.Label19.place(relx=0.597, rely=0.238, height=21, width=77)
        self.Label19.configure(activebackground="#f9f9f9")
        self.Label19.configure(activeforeground="black")
        self.Label19.configure(background="#d9d9d9")
        self.Label19.configure(disabledforeground="#a3a3a3")
        self.Label19.configure(foreground="#000000")
        self.Label19.configure(highlightbackground="#d9d9d9")
        self.Label19.configure(highlightcolor="black")
        self.Label19.configure(text='''Hypertension''')

        self.Label20 = tk.Label(self.Canvas1)
        self.Label20.place(relx=0.58, rely=0.324, height=31, width=94)
        self.Label20.configure(activebackground="#f9f9f9")
        self.Label20.configure(activeforeground="black")
        self.Label20.configure(background="#d9d9d9")
        self.Label20.configure(disabledforeground="#a3a3a3")
        self.Label20.configure(foreground="#000000")
        self.Label20.configure(highlightbackground="#d9d9d9")
        self.Label20.configure(highlightcolor="black")
        self.Label20.configure(text='''Diabetes Milletus''')

        self.Label21 = tk.Label(self.Canvas1)
        self.Label21.place(relx=0.58, rely=0.432, height=21, width=96)
        self.Label21.configure(activebackground="#f9f9f9")
        self.Label21.configure(activeforeground="black")
        self.Label21.configure(background="#d9d9d9")
        self.Label21.configure(disabledforeground="#a3a3a3")
        self.Label21.configure(foreground="#000000")
        self.Label21.configure(highlightbackground="#d9d9d9")
        self.Label21.configure(highlightcolor="black")
        self.Label21.configure(text='''Coronary disease''')

        self.Label22 = tk.Label(self.Canvas1)
        self.Label22.place(relx=0.614, rely=0.497, height=31, width=54)
        self.Label22.configure(activebackground="#f9f9f9")
        self.Label22.configure(activeforeground="black")
        self.Label22.configure(background="#d9d9d9")
        self.Label22.configure(disabledforeground="#a3a3a3")
        self.Label22.configure(foreground="#000000")
        self.Label22.configure(highlightbackground="#d9d9d9")
        self.Label22.configure(highlightcolor="black")
        self.Label22.configure(text='''Appetite''')

        self.Label23 = tk.Label(self.Canvas1)
        self.Label23.place(relx=0.597, rely=0.605, height=21, width=74)
        self.Label23.configure(activebackground="#f9f9f9")
        self.Label23.configure(activeforeground="black")
        self.Label23.configure(background="#d9d9d9")
        self.Label23.configure(disabledforeground="#a3a3a3")
        self.Label23.configure(foreground="#000000")
        self.Label23.configure(highlightbackground="#d9d9d9")
        self.Label23.configure(highlightcolor="black")
        self.Label23.configure(text='''Pedal Edema''')

        self.Label24 = tk.Label(self.Canvas1)
        self.Label24.place(relx=0.614, rely=0.691, height=31, width=54)
        self.Label24.configure(activebackground="#f9f9f9")
        self.Label24.configure(activeforeground="black")
        self.Label24.configure(background="#d9d9d9")
        self.Label24.configure(disabledforeground="#a3a3a3")
        self.Label24.configure(foreground="#000000")
        self.Label24.configure(highlightbackground="#d9d9d9")
        self.Label24.configure(highlightcolor="black")
        self.Label24.configure(text='''Anemia''')

        self.Text17 = tk.Text(self.Canvas1)
        self.Text17.place(relx=0.746, rely=0.043, relheight=0.052
                , relwidth=0.123)
        self.Text17.configure(background="white")
        self.Text17.configure(font="TkTextFont")
        self.Text17.configure(foreground="black")
        self.Text17.configure(highlightbackground="#d9d9d9")
        self.Text17.configure(highlightcolor="black")
        self.Text17.configure(insertbackground="black")
        self.Text17.configure(selectbackground="#c4c4c4")
        self.Text17.configure(selectforeground="black")
        self.Text17.configure(wrap="word")

        self.Text18 = tk.Text(self.Canvas1)
        self.Text18.place(relx=0.746, rely=0.151, relheight=0.052
                , relwidth=0.123)
        self.Text18.configure(background="white")
        self.Text18.configure(font="TkTextFont")
        self.Text18.configure(foreground="black")
        self.Text18.configure(highlightbackground="#d9d9d9")
        self.Text18.configure(highlightcolor="black")
        self.Text18.configure(insertbackground="black")
        self.Text18.configure(selectbackground="#c4c4c4")
        self.Text18.configure(selectforeground="black")
        self.Text18.configure(wrap="word")

        self.Text19 = tk.Text(self.Canvas1)
        self.Text19.place(relx=0.746, rely=0.238, relheight=0.052
                , relwidth=0.123)
        self.Text19.configure(background="white")
        self.Text19.configure(font="TkTextFont")
        self.Text19.configure(foreground="black")
        self.Text19.configure(highlightbackground="#d9d9d9")
        self.Text19.configure(highlightcolor="black")
        self.Text19.configure(insertbackground="black")
        self.Text19.configure(selectbackground="#c4c4c4")
        self.Text19.configure(selectforeground="black")
        self.Text19.configure(wrap="word")

        self.Text20 = tk.Text(self.Canvas1)
        self.Text20.place(relx=0.746, rely=0.324, relheight=0.052
                , relwidth=0.123)
        self.Text20.configure(background="white")
        self.Text20.configure(font="TkTextFont")
        self.Text20.configure(foreground="black")
        self.Text20.configure(highlightbackground="#d9d9d9")
        self.Text20.configure(highlightcolor="black")
        self.Text20.configure(insertbackground="black")
        self.Text20.configure(selectbackground="#c4c4c4")
        self.Text20.configure(selectforeground="black")
        self.Text20.configure(wrap="word")

        self.Text21 = tk.Text(self.Canvas1)
        self.Text21.place(relx=0.746, rely=0.41, relheight=0.052, relwidth=0.123)

        self.Text21.configure(background="white")
        self.Text21.configure(font="TkTextFont")
        self.Text21.configure(foreground="black")
        self.Text21.configure(highlightbackground="#d9d9d9")
        self.Text21.configure(highlightcolor="black")
        self.Text21.configure(insertbackground="black")
        self.Text21.configure(selectbackground="#c4c4c4")
        self.Text21.configure(selectforeground="black")
        self.Text21.configure(wrap="word")

        self.Text22 = tk.Text(self.Canvas1)
        self.Text22.place(relx=0.746, rely=0.497, relheight=0.052
                , relwidth=0.123)
        self.Text22.configure(background="white")
        self.Text22.configure(font="TkTextFont")
        self.Text22.configure(foreground="black")
        self.Text22.configure(highlightbackground="#d9d9d9")
        self.Text22.configure(highlightcolor="black")
        self.Text22.configure(insertbackground="black")
        self.Text22.configure(selectbackground="#c4c4c4")
        self.Text22.configure(selectforeground="black")
        self.Text22.configure(wrap="word")

        self.Text23 = tk.Text(self.Canvas1)
        self.Text23.place(relx=0.746, rely=0.583, relheight=0.052
                , relwidth=0.123)
        self.Text23.configure(background="white")
        self.Text23.configure(font="TkTextFont")
        self.Text23.configure(foreground="black")
        self.Text23.configure(highlightbackground="#d9d9d9")
        self.Text23.configure(highlightcolor="black")
        self.Text23.configure(insertbackground="black")
        self.Text23.configure(selectbackground="#c4c4c4")
        self.Text23.configure(selectforeground="black")
        self.Text23.configure(wrap="word")

        self.Text24 = tk.Text(self.Canvas1)
        self.Text24.place(relx=0.746, rely=0.691, relheight=0.052
                , relwidth=0.123)
        self.Text24.configure(background="white")
        self.Text24.configure(font="TkTextFont")
        self.Text24.configure(foreground="black")
        self.Text24.configure(highlightbackground="#d9d9d9")
        self.Text24.configure(highlightcolor="black")
        self.Text24.configure(insertbackground="black")
        self.Text24.configure(selectbackground="#c4c4c4")
        self.Text24.configure(selectforeground="black")
        self.Text24.configure(wrap="word")

        self.Button1 = tk.Button(top,command=create_window)
        self.Button1.place(relx=0.533, rely=0.867, height=34, width=67)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        #self.Button1.configure(command=proj_support.NBC)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''NBC''')

        self.Button2 = tk.Button(top,command=create_window1)
        self.Button2.place(relx=0.033, rely=0.867, height=34, width=67)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        #self.Button2.configure(command=proj_support.RFC)
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''RFC''')

        self.Button3 = tk.Button(top,command=create_window2)
        self.Button3.place(relx=0.767, rely=0.867, height=34, width=67)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''SVM''')

        self.Button4 = tk.Button(top,command=create_window3)
        self.Button4.place(relx=0.3, rely=0.867, height=34, width=77)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''KNN''')

      
        
if __name__ == '__main__':
    vp_start_gui()





