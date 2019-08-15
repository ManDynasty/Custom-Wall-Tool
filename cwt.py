#!/usr/bin/env python
# coding: utf-8

# In[47]:


def pm(a): #plusminus
    if (a<0):
        return -1
    else:
        return 1

class Wall:
    def __init__(self, t, li, h, sh, d, w):
        self.t=t
        self.li=li
        self.h=h
        self.sh=sh
        self.d=d
        self.w=w
        
    def __str__(self):
        
            return ('{\n'+  
             '"_time":'+str(self.t)+',\n'+
             '"_lineIndex":'+str(int(self.li*1000+1000*pm(self.li)))+',\n'+
             '"_type":'+str(int(self.h*1000000+self.sh*1000*3/4+4001))+',\n'+
             '"_duration":'+str(self.d)+',\n'+
             '"_width":'+str(int(self.w*1000+1000))+'\n'
          '}')
            
        


# In[ ]:



        
        


# In[48]:


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


# In[49]:


def mirror(walls): # left right swap object
        newwalls=[]
        for x in walls:
            newwall=Wall(x.t,(-x.li)+4-x.w,x.h,x.sh,x.d,x.w)
            newwalls.append(newwall)
        return newwalls  


# In[50]:


import json

def jsonparser():
    data=json.loads('['+inp.get("1.0", END)+']')
    global walls
    walls=[]
    global c
    c=0
    for x in data:
        t=x['_time']
        li=x['_lineIndex']
        li=int((li-1000*pm(li))/1000)
        ty=x['_type']
        if (ty>=4001):
            h=((ty // 1000)-4)/1000
            sh=((ty % 10000)-4001)*4/3/1000
        else:
            h=(ty-1000)/1000
            sh=0
        d=x['_duration']
        w=x['_width']
        w=int((w-1000)/1000)
        newwall= Wall(t,li,h,sh,d,w)
        walls.append(newwall)
        #out.insert(INSERT,x)
        #out.insert(INSERT,',')
    printw()
    delvars()
    


# In[51]:


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


# In[52]:


def editw():
    global c
    walls[c].t=float(v1.get())
    walls[c].li=float(v2.get())
    walls[c].h=float(v3.get())
    walls[c].sh=float(v4.get())
    walls[c].d=float(v5.get())
    walls[c].w=float(v6.get())
    printw()

def addw():
    t=float(empty(v1.get()))
    li=float(empty(v2.get()))
    h=float(empty(v3.get()))
    sh=float(empty(v4.get()))
    d=float(empty(v5.get()))
    w=float(empty(v6.get()))
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


# In[53]:


def mirrorw():
    global walls
    walls=mirror(walls)
    printw()
    
def shiftw():
    global walls
    ts=float(empty(v11.get()))
    lis=float(empty(v22.get()))
    hs=float(empty(v33.get()))
    shs=float(empty(v44.get()))
    ds=float(empty(v55.get()))
    ws=float(empty(v66.get()))
    walls=shift(walls, ts, lis, hs, shs, ds, ws)
    printw()
    
def mirrorwp():
    global walls
    for x in mirror(walls):
        walls.append(x)
    printw()
    
def shiftwp():
    global walls
    ts=float(empty(v11.get()))
    lis=float(empty(v22.get()))
    hs=float(empty(v33.get()))
    shs=float(empty(v44.get()))
    ds=float(empty(v55.get()))
    ws=float(empty(v66.get()))
    for x in shift(walls, ts, lis, hs, shs, ds, ws):
        walls.append(x)
    printw()

def sbsi(owall, ts, lis, hs, shs, ds, ws, times): #step-by-step-increase, owall is original wall/starting wall, s are shifts, times are how often
    newwalls=[]
    for x in range (times):
        newwall= Wall(owall.t+ts, owall.li+lis, owall.h+hs, owall.sh+shs, owall.d+ds, owall.w+ws)
        newwalls.append(newwall)
        owall=newwall
    return newwalls

def sbsiw():
    global walls
    owalls=walls
    ts=float(empty(v11.get()))
    lis=float(empty(v22.get()))
    hs=float(empty(v33.get()))
    shs=float(empty(v44.get()))
    ds=float(empty(v55.get()))
    ws=float(empty(v66.get()))
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
    


# In[54]:


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
    for x in walls:
        out.insert(INSERT,x)
        out.insert(INSERT,",")
        
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
        v5.insert(INSERT,walls[c].d)
        v6.insert(INSERT,walls[c].w)
    
def empty(a):
    if(len(a)==0):
        return 0
    else:
        return a


# In[ ]:


import tkinter as tk
from tkinter import *

global walls
global c

window = Tk()
window.title("Custom Wall Tool") 
window.iconbitmap('tama.ico')
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

lv3=Label(window, text="0-4", font="bold",fg="green")
lv3.grid(column=4, row=5)

lv4=Label(window, text="0-1.33", font="bold",fg="green")
lv4.grid(column=4, row=6)

lv5=Label(window, text="any", font="bold",fg="green")
lv5.grid(column=4, row=7)

lv6=Label(window, text=">0", font="bold",fg="green")
lv6.grid(column=4, row=8)

lv7=Label(window, text="int >0", font="bold",fg="green")
lv7.grid(column=4, row=9)

credit=Label(window,text="Discord: ManDynasty#4729")
credit.grid(column=5,row=14, columnspan=2)

clear()
window.mainloop()


# In[ ]:




