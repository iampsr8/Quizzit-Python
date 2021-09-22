from tkinter import*
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='Prateek8',database='quiz')
mc=mydb.cursor()
win0=Tk()
win1=Toplevel()
win2=Toplevel()
win3=Toplevel()
win4=Toplevel()
win5=Toplevel()
win6=Toplevel()
win7=Toplevel()
win8=Toplevel()
win9=Toplevel()
win10=Toplevel()
win0.geometry('400x350')
win1.geometry('350x250')
win2.geometry('400x350')
win3.geometry('480x550')
win4.geometry('400x400')
win5.geometry('380x300')
win6.geometry('450x400')
win7.geometry('550x650')
win8.geometry('450x450')
win9.geometry('500x500')
win10.geometry('560x520')
win0.configure(bg='navajo white')
win1.configure(bg='navajo white')
win2.configure(bg='navajo white')
win3.configure(bg='navajo white')
win4.configure(bg='navajo white')
win5.configure(bg='navajo white')
win6.configure(bg='light cyan')
win7.configure(bg='light cyan')
win8.configure(bg='light cyan')
win9.configure(bg='light cyan')


global a
a=1
global b
b=1
global k
k=1
global c

global score_count
score_count=0


win1.withdraw()
win2.withdraw()
win3.withdraw()
win4.withdraw()
win5.withdraw()
win6.withdraw()
win7.withdraw()
win8.withdraw()
win9.withdraw()
win10.withdraw()


# Labels----------------------------------------------------------------------

lf3=LabelFrame(win0,width=200,height=50,bg='navajo white')
lf3.place(relx=0.5,rely=0.3,anchor=CENTER)
l6=Label(lf3,text='QUIZZIT',font=('Arial bold',15),bg='navajo white')
l6.place(relx=0.5,rely=0.5,anchor=CENTER)


lf4=LabelFrame(win1,width=200,height=50,bg='navajo white')
lf4.place(relx=0.5,rely=0.2,anchor=CENTER)
l7=Label(lf4,text='QUIZZIT',font=('Arial bold',17),bg='navajo white')
l7.place(relx=0.5,rely=0.5,anchor=CENTER)
l8=Label(win1,text='Username',font=('Arial bold',12))
l8.place(relx=0.2,rely=0.45,anchor=CENTER)
l9=Label(win1,text='Password',font=('Arial bold',12))
l9.place(relx=0.2,rely=0.6,anchor=CENTER)


l10=Label(win2,text='SUBJECT NAME',font=('Arial bold',13))
l10.place(relx=0.22,rely=0.2,anchor=CENTER)
l11=Label(win2,text='NO OF OPTIONS',font=('Arial bold',13))
l11.place(relx=0.22,rely=0.4,anchor=CENTER)

lf5=LabelFrame(win6,width=200,height=50,bg='light cyan')
lf5.place(relx=0.5,rely=0.16,anchor=CENTER)
l12=Label(lf5,text='QUIZZIT',font=('Arial bold',17),bg='light cyan')
l12.place(relx=0.5,rely=0.5,anchor=CENTER)
l13=Label(win6,text='ENTER NAME',font=('Arial bold',13),bg='light cyan')
l13.place(relx=0.24,rely=0.38,anchor=CENTER)
l14=Label(win6,text='REGISTRATION NO',font=('Arial bold',13),bg='light cyan')
l14.place(relx=0.2,rely=0.55,anchor=CENTER)


lf6=LabelFrame(win7,width=300,height=50,bg='light cyan')
lf6.pack()
l16=Label(win7,height=3,bg='light cyan')
l16.pack(fill=X)



#Entries and Text-----------------------------------------------------


e1=Entry(win1,width=20,font=('Arial',11))
e1.place(relx=0.58,rely=0.45,anchor=CENTER)
e2=Entry(win1,width=20,font=('Arial',11))
e2.place(relx=0.58,rely=0.6,anchor=CENTER)

e3=Entry(win2,width=20,font=('Arial',12))
e3.place(relx=0.66,rely=0.2,anchor=CENTER)
e4=Entry(win2,width=20,font=('Arial',12))
e4.place(relx=0.66,rely=0.4,anchor=CENTER)

e5=Entry(win6,width=20,font=('Arial',12))
e5.place(relx=0.6,rely=0.38,anchor=CENTER)
e6=Entry(win6,width=20,font=('Arial',12))
e6.place(relx=0.6,rely=0.55,anchor=CENTER)








lf2=LabelFrame(win3,width=180,height=50,bg='navajo white')
# lb2=Label(lf2,text=e3.get().upper(),font=11)
lf2.pack()
# lb2.place(relx=0.5,rely=0.5,anchor=CENTER)
lb3=Label(win3,height=3,bg='navajo white')
lb3.pack(fill=X)
l0=Label(win4,text='ENTER QUESTION',font=('Arial bold',12))
l0.place(relx=0.23,rely=0.06,anchor=CENTER)
txt=Text(win4,width=45,height=4)
txt.place(relx=0.5,rely=0.20,anchor=CENTER)
l1=Label(win4,text='Option A',font=('Arial bold',10))
l1.place(relx=0.13,rely=0.4,anchor=CENTER)
l2=Label(win4,text='Option B',font=('Arial bold',10))
l2.place(relx=0.6,rely=0.4,anchor=CENTER)
l3=Label(win4,text='Option C',font=('Arial bold',10))
l3.place(relx=0.13,rely=0.6,anchor=CENTER)
l4=Label(win4,text='Option D',font=('Arial bold',10))
l4.place(relx=0.6,rely=0.6,anchor=CENTER)
l5=Label(win4,text='Correct Option',font=('Arial bold',10))
l5.place(relx=0.2,rely=0.73,anchor=CENTER)



o1=Entry(win4,width=12,font=('Arial',10))
o1.place(relx=0.37,rely=0.4,anchor=CENTER)
o2=Entry(win4,width=12,font=('Arial',10))
o2.place(relx=0.82,rely=0.4,anchor=CENTER)
o3=Entry(win4,width=12,font=('Arial',10))
o3.place(relx=0.37,rely=0.6,anchor=CENTER)
o4=Entry(win4,width=12,font=('Arial',10))
o4.place(relx=0.82,rely=0.6,anchor=CENTER)
o5=Entry(win4,width=12,font=('Arial',10))
o5.place(relx=0.47,rely=0.73,anchor=CENTER)







# Commands-----------------------------------------------------------------------------


def teacher():
    win0.withdraw()
    win1.deiconify()
    win1.mainloop()


def student():
    win0.withdraw()
    win6.deiconify()
    win6.mainloop()




def color(par):
    win8.withdraw()
    win7.deiconify()
    btn[par].config(bg='green2')
    mg.config(text="")
    



def start():
    win6.withdraw()
    win7.deiconify()
    global s1
    s1=e5.get()
    global s2
    s2=e6.get()
    global s_final
    s_final="""INSERT INTO score(name,regno) VALUES(%s,%s)"""

    mc.execute(s_final,(s1,s2))
    mydb.commit()


    l15=Label(lf6,text=e3.get().upper(),font=('Arial bold',15),bg='light cyan')
    l15.place(relx=0.5,rely=0.5,anchor=CENTER)



    global btn
    btn=[]
    global k
    global lf_btn
    lf_btn=[]


    for i in range(a-1):
        lf_btn.append(LabelFrame(win7,width=150,height=50,bg='snow'))
        lf_btn[i].pack()
 
        btn.append(Button(lf_btn[i],text='Question '+str(k),width=20,bg='snow',font=10,height=2,    command=lambda k=k: display(k)))
        btn[i].pack()
        k+=1
   
    win7.mainloop()


def login():
    win1.withdraw()
    win2.deiconify()
    win2.mainloop()

def win3open():
    win2.withdraw()
    win3.deiconify()
    lb2=Label(lf2,text=e3.get().upper(),font=('Arial bold',15),bg='navajo white')
    lb2.place(relx=0.5,rely=0.5,anchor=CENTER)
    win3.mainloop()

def go():
    win3.withdraw()
    win5.deiconify()
    l12=Label(win5,text=e3.get().upper() + ' QUESTION SET CREATED\nWITH '+str(c)+' QUESTIONS.',font=('Arial bold',12),bg='navajo white')
    l12.place(relx=0.5,rely=0.3,anchor=CENTER)
    win5.mainloop()

def createnew():
    win5.withdraw()
    win2.deiconify()

def exit():
    win5.withdraw()
    win0.deiconify()

def add():
    global a
    global b
    win3.withdraw()
    win4.deiconify()
    a+=1
    txt.delete("1.0","end")
    o1.delete(0, 'end')
    o2.delete(0, 'end')
    o3.delete(0, 'end')
    o4.delete(0, 'end')
    o5.delete(0, 'end')
    

def done():
    global a
    global b
    win4.withdraw()
    win3.deiconify()
    for i in range(b,a):
        lf=LabelFrame(win3,width=150,height=50,bg='snow')
        lf.pack()
        lb=Label(lf,text='Question '+str(i),font=9,bg='snow')
        lb.place(relx=0.5,rely=0.5,anchor=CENTER)
    b+=1


    global sql1
    sql1=txt.get("1.0",'end-1c')
    global sql2
    sql2=o1.get()
    global sql3
    sql3=o2.get()
    global sql4
    sql4=o3.get()
    global sql5
    sql5=o4.get()
    global sql6
    sql6=o5.get()
    global c
    c=a-1
    sql_final="""INSERT INTO teacher VALUES(%s,%s,%s,%s,%s,%s,%s)
    """

    mc.execute(sql_final,(c,sql1,sql2,sql3,sql4,sql5,sql6))
    mydb.commit()
    win4.mainloop()



def display(num):
    win7.withdraw()
    win8.deiconify()
    b13.config(bg='snow')
    b14.config(bg='snow')
    b15.config(bg='snow')
    b16.config(bg='snow')

    sql=("""SELECT qs FROM teacher WHERE slno=%s""")
    mc.execute(sql,(num,))
    global res
    
    for x in mc:
        res=x
    global mg
    mg=Message(win8,font=('Arial',14),width=350,bg='snow')
    mg.config(text=res[0])
    mg.place(relx=0.5,rely=0.13,anchor=CENTER)

    sql_op="""SELECT op1,op2,op3,op4 FROM teacher WHERE slno=%s"""
    mc.execute(sql_op,(num,))
    option=mc.fetchone()


    # label for option names--------------------

    l17=Label(win8,text='(A)',font=('Arial bold',12),bg='light cyan')
    l17.place(relx=0.12,rely=0.4,anchor=CENTER)
    l18=Label(win8,text='(B)',font=('Arial bold',12),bg='light cyan')
    l18.place(relx=0.54,rely=0.4,anchor=CENTER)
    l19=Label(win8,text='(C)',font=('Arial bold',12),bg='light cyan')
    l19.place(relx=0.12,rely=0.6,anchor=CENTER)
    l20=Label(win8,text='(D)',font=('Arial bold',12),bg='light cyan')
    l20.place(relx=0.54,rely=0.6,anchor=CENTER)




    b13.config(text=option[0])
    b14.config(text=option[1])
    b15.config(text=option[2])
    b16.config(text=option[3])

    global correct_option
    sql_correct="""SELECT crrop FROM teacher WHERE slno=%s"""
    mc.execute(sql_correct,(num,))
    correct_option=mc.fetchone()

    b12=Button(win8,text='DONE',width=15,font=('Arial bold',12),command=lambda: color(num-1))
    b12.place(relx=0.5,rely=0.85,anchor=CENTER)
    win8.mainloop()


def click1():
    global score_count
    b13.config(bg='green2')
    b14.config(bg='snow')
    b15.config(bg='snow')
    b16.config(bg='snow')
    if(correct_option[0]=='a'):
        score_count+=1
def click2():
    global score_count
    b13.config(bg='snow')
    b14.config(bg='green2')
    b15.config(bg='snow')
    b16.config(bg='snow')
    if(correct_option[0]=='b'):
        score_count+=1
def click3():
    global score_count
    b13.config(bg='snow')
    b14.config(bg='snow')
    b15.config(bg='green2')
    b16.config(bg='snow')
    if(correct_option[0]=='c'):
        score_count+=1
def click4():
    global score_count
    b13.config(bg='snow')
    b14.config(bg='snow')
    b15.config(bg='snow')
    b16.config(bg='green2')
    if(correct_option[0]=='d'):
        score_count+=1


def go_to_result():
    global l25
    global l26
    global student_score
    global ftch
    ftch=("""SELECT sl FROM score WHERE name=%s""")
    global val
    mc.execute(ftch,(s1,))
    val=mc.fetchone()
    # print(val)
    xyz="""UPDATE score SET score=%s WHERE sl=%s"""
    mc.execute(xyz,(score_count,val[0]))
    mydb.commit()
    win7.withdraw()
    win9.deiconify()
    global result_fetch
    result_fetch="""SELECT score FROM score WHERE name=%s"""
    mc.execute(result_fetch,(s1,))
    student_score=mc.fetchone()

    # Result labels-------

    lf7=LabelFrame(win9,width=200,height=50,bg='light cyan')
    lf7.place(relx=0.5,rely=0.15,anchor=CENTER)
    l21=Label(lf7,text='RESULT',font=('Arial bold',15),bg='light cyan')
    l21.place(relx=0.5,rely=0.5,anchor=CENTER)
    l22=Label(win9,text='NAME:',font=('Arial bold',12),bg='light cyan')
    l22.place(relx=0.2,rely=0.4,anchor=CENTER)
    l23=Label(win9,text='REG NO:',font=('Arial bold',12),bg='light cyan')
    l23.place(relx=0.2,rely=0.55,anchor=CENTER)
    l24=Label(win9,text='SCORE:',font=('Arial bold',12),bg='light cyan')
    l24.place(relx=0.2,rely=0.7,anchor=CENTER)
    l25=Label(win9,font=('Arial bold',12),bg='light cyan')
    l25.place(relx=0.55,rely=0.4,anchor=CENTER)
    l25.config(text=s1.upper())
    l26=Label(win9,font=('Arial bold',12),bg='light cyan')
    l26.place(relx=0.55,rely=0.55,anchor=CENTER)
    l26.config(text=s2)
    l27=Label(win9,text=student_score[0],font=('Arial bold',12),bg='light cyan')
    l27.place(relx=0.5,rely=0.7,anchor=CENTER)

    win9.mainloop()


def teacher_results():
    win2.withdraw()
    win10.deiconify()
    lf8=LabelFrame(win10,width=200,height=50,bg='snow')
    lf8.place(relx=0.5,rely=0.1,anchor=CENTER)
    l28=Label(lf8,text='RESULTS',font=('Arial bold',15),bg='snow')
    l28.place(relx=0.5,rely=0.5,anchor=CENTER)
    l29=Label(win10,text='Sl No',font=('Arial bold',13))
    l29.place(relx=0.18,rely=0.25,anchor=CENTER)
    l30=Label(win10,text='NAME',font=('Arial bold',13))
    l30.place(relx=0.45,rely=0.25,anchor=CENTER)
    l31=Label(win10,text='SCORE',font=('Arial bold',13))
    l31.place(relx=0.75,rely=0.25,anchor=CENTER)

    sql_stud_result="""SELECT sl,name,score FROM score"""
    mc.execute(sql_stud_result)

    w=8
    for i in mc:
        res_lb1=Label(win10,text=i[0],font=('Arial bold',11))
        res_lb1.place(relx=0.18,rely=0.25+w/100,anchor=CENTER)
        res_lb2=Label(win10,text=i[1],font=('Arial bold',11))
        res_lb2.place(relx=0.45,rely=0.25+w/100,anchor=CENTER)
        res_lb3=Label(win10,text=i[2],font=('Arial bold',11))
        res_lb3.place(relx=0.75,rely=0.25+w/100,anchor=CENTER)
        w+=8
    

    win10.mainloop()




def start_new():
    global score_count
    # global a
    # global b
    global k
    score_count=0
    e5.delete(0, 'end')
    e6.delete(0, 'end')
    for i in range(a-1):
        btn[i].destroy()
    for i in range(a-1):
        lf_btn[i].destroy()


    b13.config(bg='snow')
    b14.config(bg='snow')
    b15.config(bg='snow')
    b16.config(bg='snow')
    l25.config(text="")
    l26.config(text="")
    # a=1
    # b=1
    k=1

    win9.withdraw()
    win0.deiconify()









    
# Buttons-------------------------------------------------------------------------------

b3=Button(win0,text='STUDENT',font=('Arial Bold',12),width=13,command=student)
b3.place(relx=0.3,rely=0.7,anchor=CENTER)
b4=Button(win0,text='TEACHER',font=('Arial Bold',12),width=13,command=teacher)
b4.place(relx=0.73,rely=0.7,anchor=CENTER)

b5=Button(win1,text='LOGIN',font=('Arial Bold',12),width=12,command=login)
b5.place(relx=0.5,rely=0.82,anchor=CENTER)


b6=Button(win2,text='ADD',width=10,font=('Arial bold',12),command=win3open)
b6.place(relx=0.3,rely=0.8,anchor=CENTER)
b7=Button(win2,text='RESULTS',width=12,font=('Arial bold',12),command=teacher_results)
b7.place(relx=0.65,rely=0.8,anchor=CENTER)

b8=Button(win5,text='EXIT',width=10,font=('Arial bold',10),command=exit)
b8.place(relx=0.25,rely=0.8,anchor=CENTER)
b9=Button(win5,text='CREATE NEW',width=13,font=('Arial bold',10),command=createnew)
b9.place(relx=0.68,rely=0.8,anchor=CENTER)

b10=Button(win6,text='START',width=12,font=('Arial bold',13),command=start)
b10.place(relx=0.5,rely=0.75,anchor=CENTER)



b2=Button(win4,text='DONE',width=10,font=('Arial bold',10),command=done)
b2.place(relx=0.5,rely=0.85, anchor=CENTER)
b0=Button(win3,text='GO',width=10,font=('Arial bold',10),command=go)
b0.place(relx=0.7,rely=0.85, anchor=CENTER)
b1=Button(win3,text='ADD',width=10,font=('Arial bold',10),command=add)
b1.place(relx=0.3,rely=0.85, anchor=CENTER)



b11=Button(win7,text='GO',width=12,font=('Arial bold',12),command=go_to_result)
b11.place(relx=0.5,rely=0.85,anchor=CENTER)

b17=Button(win9,text='START NEW\nQUIZ',width=12,font=('Arial bold',12),command=start_new)
b17.place(relx=0.5,rely=0.85,anchor=CENTER)



# Option labels and buttons---------------------------------------


b13=Button(win8,width=13,bg='snow',font=('Arial bold',11),command=click1)
b13.place(relx=0.34,rely=0.4,anchor=CENTER)
b14=Button(win8,width=13,bg='snow',font=('Arial bold',11),command=click2)
b14.place(relx=0.77,rely=0.4,anchor=CENTER)
b15=Button(win8,width=13,bg='snow',font=('Arial bold',11),command=click3)
b15.place(relx=0.34,rely=0.6,anchor=CENTER)
b16=Button(win8,width=13,bg='snow',font=('Arial bold',11),command=click4)
b16.place(relx=0.77,rely=0.6,anchor=CENTER)


win0.mainloop()