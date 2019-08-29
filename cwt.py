#!/usr/bin/env python
# coding: utf-8

# In[40]:


from decimal import Decimal

def pm(a): #plusminus
    if (a<0):
        return -1000
    else:
        return 1000
    
def dz(d): #duration zero ,rounds values if needed
    if (d%1==0):
        return round(d,0)
    else:
        return round(Decimal(d),3)

class Wall:
    def __init__(self, t, li, h, sh, d, w):
        self.t=Decimal(t)
        self.li=int(li)
        self.h=int(h)
        self.sh=int(sh)
        self.d=Decimal(d)
        self.w=int(w)
        
    def __str__(self):
        
            return ('{\n'+  
             '"_time":'+str(self.t)+',\n'+
             '"_lineIndex":'+str(int(self.li+pm(self.li)))+',\n'+
             '"_type":'+str(int(self.h*1000+self.sh+4001))+',\n'+
             '"_duration":'+str(dz(self.d))+',\n'+
             '"_width":'+str(int(self.w+1000))+'\n'
          '}')
            
        


# In[41]:


def shift(walls, ts, lis, hs, shs, ds, ws): #shift object
    newwalls=[]
    for x in walls:
        t=x.t+ts
        li=x.li+lis
        h=x.h+hs
        sh=x.sh+shs
        d=x.d+ds
        w=x.w+ws
        newwall=Wall(t,li,h,sh,d,w)
        newwalls.append(newwall)
        
    return newwalls


# In[42]:


def mirror(walls): # left right swap object
        newwalls=[]
        for x in walls:
            newwall=Wall(x.t,(-x.li)+4000-x.w,x.h,x.sh,x.d,x.w)
            newwalls.append(newwall)
        return newwalls  


# In[43]:


import json

def jsonparser():
    dataraw=inp.get("1.0", END)
    if (dataraw[-2]==","):
        dataraw=dataraw[:-2]
    if(dataraw[0]==","):
        dataraw=dataraw[1:]   
    data=json.loads('['+dataraw+']')
    global walls
    walls=[]
    global c
    c=0
    for x in data:
        t=x['_time']
        li=x['_lineIndex']
        if (li>=0) and (li<=3):
            li=li*1000+1000
        li=int(li-pm(li))
        ty=x['_type']
        if (ty>=4001):
            sh=((ty%10000)-4001)%1000
            h=(ty-4001-sh)//1000
        elif(ty>=1000):
            h=(ty-1000)
            sh=0
        elif(ty==1):
            h=1000
            sh=0
        elif(ty==0.5):
            h=500
            sh=394
            
        d=x['_duration']
        w=x['_width']
        if(w>=0) and (w<=4):
            w=w*1000+1000
        w=int(w-1000)
        newwall= Wall(t,li,h,sh,d,w)
        walls.append(newwall)
        #out.insert(INSERT,x)
        #out.insert(INSERT,',')
    printw()
    delvars()
    


# In[44]:


def nextw():
    global c
    if (c<len(walls)-1):
        c=c+1
    delvars()
        
def backw():
    global c
    if (c>0):
        c=c-1
    delvars()


# In[45]:


def editw():
    global c
    walls[c].t=Decimal(v1.get())
    walls[c].li=int(v2.get())
    walls[c].h=int(v3.get())
    walls[c].sh=int(v4.get())
    walls[c].d=Decimal(v5.get())
    walls[c].w=int(v6.get())
    printw()

def addw():
    t=Decimal(empty(v1.get()))
    li=int(empty(v2.get()))
    h=int(empty(v3.get()))
    sh=int(empty(v4.get()))
    d=Decimal(empty(v5.get()))
    w=int(empty(v6.get()))
    newwall=Wall(t,li,h,sh,d,w)
    walls.append(newwall)
    global c
    c=len(walls)-1
    delvars()
    printw()
    
def delw():
    global c
    if (len(walls)>0):
        walls.pop(c)
        if (c==0):
            c=c+1
        else:
            c=c-1
        delvars()
        printw()


# In[46]:


import os

def savew():
    if (len(se.get())>0):
        name=se.get()
        data=''
        newpath = r'Presets' 
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        for x in walls:
            data=data+str(x)+','
        if (not os.path.isfile("Presets/"+name+".txt")):
            lb.insert(END, name)
        with open("Presets/"+name+".txt", 'w') as file:
            file.write(data)
    
def delsw():
    name=lb.get(ACTIVE)
    os.remove("Presets/"+name+".txt")
    lb.delete(ANCHOR)
    
def loadpresets():
    try:
        for x in os.listdir("Presets/"):
            lb.insert(END,os.path.basename(x)[:-4])
    except:
        pass
def loadw(a):
    try:
        name=lb.get(ACTIVE)
        with open("Presets/"+name+".txt", 'r') as file:
            content=file.read()[:-1]
        data=json.loads('['+content+']')
        global walls
        if(a==0):
            walls=[]
        global c
        c=0
        for x in data:
            t=x['_time']
            li=x['_lineIndex']
            li=int(li-pm(li))
            ty=x['_type']
            if (ty>=4001):
                h=((ty // 1000)-4)
                sh=((ty-(h*1000))-4001)
            else:
                h=(ty-1000)
                sh=0
            d=x['_duration']
            w=x['_width']
            w=int(w-1000)
            newwall= Wall(t,li,h,sh,d,w)
            walls.append(newwall)
            #out.insert(INSERT,x)
            #out.insert(INSERT,',')
        printw()
        delvars()
    
    except:
        pass


# In[47]:


def mirrorw():
    global walls
    walls=mirror(walls)
    printw()
    
def shiftw():
    global walls
    ts=Decimal(empty(v11.get()))
    lis=int(empty(v22.get()))
    hs=int(empty(v33.get()))
    shs=int(empty(v44.get()))
    ds=Decimal(empty(v55.get()))
    ws=int(empty(v66.get()))
    walls=shift(walls, ts, lis, hs, shs, ds, ws)
    printw()
    
def mirrorwp():
    global walls
    for x in mirror(walls):
        walls.append(x)
    printw()
    
def shiftwp():
    global walls
    ts=Decimal(empty(v11.get()))
    lis=int(empty(v22.get()))
    hs=int(empty(v33.get()))
    shs=int(empty(v44.get()))
    ds=Decimal(empty(v55.get()))
    ws=int(empty(v66.get()))
    for x in shift(walls, ts, lis, hs, shs, ds, ws):
        walls.append(x)
    printw()

def sbsiw(): #step-by-step-increase, owalls are original walls/starting walls, s are shifts, times are how often
    global walls
    owalls=walls
    ts=Decimal(empty(v11.get()))
    lis=int(empty(v22.get()))
    hs=int(empty(v33.get()))
    shs=int(empty(v44.get()))
    ds=Decimal(empty(v55.get()))
    ws=int(empty(v66.get()))
    times=int(empty(v77.get()))
    a=len(walls)
    for x in range (times):
        newwalls=[]
        for y in range (a):
            newwall= Wall(owalls[y].t+ts, owalls[y].li+lis, owalls[y].h+hs, owalls[y].sh+shs, owalls[y].d+ds, owalls[y].w+ws)
            walls.append(newwall)
            newwalls.append(newwall)
        owalls=newwalls
    printw()
    


# In[48]:


def clear():
    inp.delete("1.0",END)
    out.delete("1.0",END)
    global walls
    walls=[]
    v1.delete(0,END)
    v2.delete(0,END)
    v3.delete(0,END)
    v4.delete(0,END)
    v5.delete(0,END)
    v6.delete(0,END)
    v11.delete(0,END)
    v22.delete(0,END)
    v33.delete(0,END)
    v44.delete(0,END)
    v55.delete(0,END)
    v66.delete(0,END)
    v77.delete(0,END)
    
def printw():
    global walls
    out.delete("1.0",END)
    output=""
    for x in walls:
        output+=str(x)+","
    out.insert(INSERT,output[:-1])
        
def delvars():
    global c
    v1.delete(0,END)
    v2.delete(0,END)
    v3.delete(0,END)
    v4.delete(0,END)
    v5.delete(0,END)
    v6.delete(0,END)
    if (len(walls)>0):
        v1.insert(INSERT,walls[c].t)
        v2.insert(INSERT,walls[c].li)
        v3.insert(INSERT,walls[c].h)
        v4.insert(INSERT,walls[c].sh)
        v5.insert(INSERT,dz(walls[c].d))
        v6.insert(INSERT,walls[c].w)
    
def empty(a):
    if(len(a)==0):
        return 0
    else:
        return a


# In[49]:


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# In[50]:


import math

def circle(swall, r): #startwall radius
    global walls
    rs=r*r*1000
    r=r*1000
    
    for a in range (r): #left side
        x=-r+a #konvertierung auf normale walls
        y=(1/3)*round(math.sqrt(rs-(x*x)),3)
        walls.append(Wall(swall.t,x,swall.h,x,swall.d,swall.w))


# In[51]:


from tkinter import *

global walls
global c

window = Tk()
window.title("Custom Wall Tool") 


# In[ ]:


try:
    window.iconbitmap(resource_path('tama.ico'))
except:
    pass
    
btnjson = Button(window, text="Read Json",command=jsonparser)
btnshift = Button(window, text="Shift", command=shiftw, width=8)
btnmirror = Button(window, text="Mirror", command=mirrorw, width=8)
btnshiftp = Button(window, text="+Shift", command=shiftwp, width=8)
btnmirrorp = Button(window, text="+Mirror", command=mirrorwp, width=8)
btninc = Button(window, text="Increase step-by-step", command=sbsiw, width=18)
btnadd = Button(window, text="Add New Wall",command=addw, width=14)
btndel = Button(window, text="Delete Wall",command=delw, width=14)
btnclear = Button(window, text="Clear All",command=clear)
btnjson.grid(column=2, row=0,columnspan=2)
btnshift.grid(column=5, row=11)
btnmirror.grid(column=6, row=11)
btnshiftp.grid(column=5, row=12)
btnmirrorp.grid(column=6, row=12)
btninc.grid(column=5, row=10, columnspan=2)
btnadd.grid(column=2, row=9, columnspan=2)
btndel.grid(column=2, row=10, columnspan=2)
btnclear.grid(column=5, row=0,columnspan=2)

btnnext=Button(window, text="Forth", command=nextw, width=6)
btnlast=Button(window, text="Back", command= backw, width=6)
btnedit=Button(window, text="Confirm Changes", command=editw, width=14)
btnnext.grid(column=2, row=12)
btnlast.grid(column=3,row=12)
btnedit.grid(column=2,row=11, columnspan=2)

#scroll1=tk.Scrollbar(window, command=inp.yview)
#scroll2=tk.Scrollbar(window, command=out.yview)
#scroll1.grid(row=0, column=1, sticky='nsew',rowspan=15)
#scroll2.grid(row=0, column=8, sticky='nsew',rowspan=15)
inp= Text(window, width=20, height=30)
inp.grid(column=0, row=1, rowspan=14)
#inp['yscrollcommand'] = scroll1.set
inp.focus_set()

il=Label(window,text="Input")
il.grid(column=0,row=0)


ol=Label(window,text="Output")
ol.grid(column=7,row=0)

out= Text(window, width=20, height=30)
out.grid(column=7, row=1, rowspan=14)
#out['yscrollcommand'] = scroll2.set

sl=Label(window, text="Name:")
sl.grid(column=8,row=1)

se=Entry(window,width=10)
se.grid(column=9,row=1)

btnsave=Button(window, text="Save Preset",width=15,command=savew)
btnsave.grid(column=8,row=2,columnspan=2)

lb=Listbox(window)
lb.grid(column=8, row=3, columnspan=2, rowspan=3)

btndele=Button(window,text="Delete Preset", command=delsw)
btnloade=Button(window,text="Load Preset", command=lambda:loadw(0))
btnloadep=Button(window,text="+Load Preset", command=lambda:loadw(1))
btndele.grid(column=8, row=7)
btnloade.grid(column=8,row=6)
btnloadep.grid(column=9,row=6)

h1=Label(window, text="Data", font="Verdana 10 bold underline")
h1.grid(column=2, row=2, columnspan=2)

h2=Label(window, text="Shift/Steps", font="Verdana 10 bold underline")
h2.grid(column=5, row=2, columnspan=2)

l1=Label(window, text="Time:")
l1.grid(column=2, row=3)
v1=Entry(window, width=8)
v1.grid(column=3, row=3)

l2=Label(window, text="LineIndex:")
l2.grid(column=2, row=4)
v2=Entry(window, width=8)
v2.grid(column=3, row=4)

l3=Label(window, text="Height:")
l3.grid(column=2, row=5)
v3=Entry(window, width=8)
v3.grid(column=3, row=5)

l4=Label(window, text="Start Height:")
l4.grid(column=2, row=6)
v4=Entry(window, width=8)
v4.grid(column=3, row=6)

l5=Label(window, text="Duration:")
l5.grid(column=2, row=7)
v5=Entry(window, width=8)
v5.grid(column=3, row=7)

l6=Label(window, text="Width:")
l6.grid(column=2, row=8)
v6=Entry(window, width=8)
v6.grid(column=3, row=8)

l11=Label(window, text="Time:")
l11.grid(column=5, row=3)
v11=Entry(window, width=8)
v11.grid(column=6, row=3)

l22=Label(window, text="LineIndex:")
l22.grid(column=5, row=4)
v22=Entry(window, width=8)
v22.grid(column=6, row=4)

l33=Label(window, text="Height:")
l33.grid(column=5, row=5)
v33=Entry(window, width=8)
v33.grid(column=6, row=5)

l44=Label(window, text="Start Height:")
l44.grid(column=5, row=6)
v44=Entry(window, width=8)
v44.grid(column=6, row=6)

l55=Label(window, text="Duration:")
l55.grid(column=5, row=7)
v55=Entry(window, width=8)
v55.grid(column=6, row=7)

l66=Label(window, text="Width:")
l66.grid(column=5, row=8)
v66=Entry(window, width=8)
v66.grid(column=6, row=8)

l77=Label(window, text="Steps:")
l77.grid(column=5, row=9)
v77=Entry(window, width=8)
v77.grid(column=6, row=9)

h3=Label(window, text="Allowed", font="bold",fg="green")
h3.grid(column=4, row=2)

lv1=Label(window, text=">0", font="bold",fg="green")
lv1.grid(column=4, row=3)

lv2=Label(window, text="any", font="bold",fg="green")
lv2.grid(column=4, row=4)

lv3=Label(window, text="0-4000", font="bold",fg="green")
lv3.grid(column=4, row=5)

lv4=Label(window, text="0-999", font="bold",fg="green")
lv4.grid(column=4, row=6)

lv5=Label(window, text="any", font="bold",fg="green")
lv5.grid(column=4, row=7)

lv6=Label(window, text="any", font="bold",fg="green")
lv6.grid(column=4, row=8)

lv7=Label(window, text="int >0", font="bold",fg="green")
lv7.grid(column=4, row=9)

credit=Label(window,text="Discord: ManDynasty#4729")
credit.grid(column=5,row=14, columnspan=2)

loadpresets()
clear()

def select_all_out(event):
    out.tag_add(SEL, "1.0", END)
    out.mark_set(INSERT, "1.0")
    out.see(INSERT)
    return 'break'

def select_all_inp(event):
    inp.tag_add(SEL, "1.0", END)
    inp.mark_set(INSERT, "1.0")
    inp.see(INSERT)
    return 'break'

out.bind("<Control-Key-a>", select_all_out)
inp.bind("<Control-Key-a>", select_all_inp)

window.mainloop()


# In[ ]:





# In[ ]:




