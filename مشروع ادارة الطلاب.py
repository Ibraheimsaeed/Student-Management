from tkinter import*
from tkinter import ttk
import pymysql
import random

class Student :
    def __init__(self,root) :
        self.root = root
        self.root.geometry('1250x647+1+1')
        self.root.title('برنامج اداراة تسجيل الطلاب ')
        self.root.configure(background='silver')
        self.root.resizable(False,False)
        title = Label(self.root ,
        text='تسجيل',
        bg='#33CEFF',
        font=('monospace',14),
        fg='white'
        )
        title.pack(fill=X)
        #-----------------------varibales---------
        self.id_var = IntVar()
        self.name_var = StringVar()
        self.phone_var= StringVar()
        self.emali_var = StringVar()
        self.mohel_var = StringVar()
        self.gender_var= StringVar()
        self.ser_var = StringVar()
        self.adress_var = StringVar()
        self.del_var = StringVar()
        self.ser_com = StringVar()
        #=----------ادوات التحكم بالبرنامج----------
        manage_frame=Frame(self.root,bg='white')
        manage_frame.place(x=1050,y=30,width=210,height=400)
        id_mange = Label(manage_frame,text='الرقم التسلسي')
        id_mange.pack()
        en_mange=Entry(manage_frame,textvariable=self.id_var,justify='center',bd='2')
        en_mange.pack()
        labl_name=Label(manage_frame,text='اسم الطالب')
        labl_name.pack()
        en_name=Entry(manage_frame,textvariable=self.name_var,justify='center',bd='2')
        en_name.pack()
        labl_email=Label(manage_frame,text='ايميل الطالب')
        labl_email.pack()
        en_email=Entry(manage_frame,textvariable=self.emali_var,justify='center',bd='2')
        en_email.pack()
        labl_phone=Label(manage_frame,text='هاتف الطالب')
        labl_phone.pack()
        en_phone=Entry(manage_frame,textvariable=self.phone_var,justify='center',bd='2')
        en_phone.pack()
        labl_cirti=Label(manage_frame,text='مؤهلات الطالب')
        labl_cirti.pack()
        en_cirti=Entry(manage_frame,textvariable=self.mohel_var,justify='center',bd='2')
        en_cirti.pack()
        label_gender=Label(manage_frame,text='اختر نوع الطالب')
        label_gender.pack()
        com_gender = ttk.Combobox(manage_frame,textvariable=self.gender_var,justify='center')
        com_gender['value'] = ('انثي','ذكر')
        com_gender.pack()
        labl_address=Label(manage_frame,text='عنوان الطالب')
        labl_address.pack()
        en_adress=Entry(manage_frame,textvariable=self.adress_var,justify='center',bd='2')
        en_adress.pack()
        labl_delete=Label(manage_frame,text=' حذف الطالب برقم التسلسلي',fg='red')
        labl_delete.pack()
        en_del=Entry(manage_frame,textvariable=self.del_var,justify='center',bd='2')
        en_del.pack()
        #-----الازرار----------------
        btn_frame = Frame(self.root,bg='white')
        btn_frame.place(x=1050,y=435,width=220,height=252)
        lab_control= Label(btn_frame,bg='#33CEFF',text='لوحة التحكم',fg='black',font=('Daco',14,'bold'))
        lab_control.pack(fill=X)
        btn_add =Button(btn_frame,text='اضافة الطالب',bg='#A3D93F',font=('Daco',14,'bold'),fg='black',command=self.data_student)
        btn_add.place(x=33,y=33,width=150,height=30)
        btn_del =Button(btn_frame,text='ازالة الطالب',bg='#A3D93F',font=('Daco',14,'bold'),fg='black',command=self.delete)
        btn_del.place(x=33,y=70,width=150,height=30)
        btn_try =Button(btn_frame,text='تعديل بيانات الطالب',bg='#A3D93F',font=('Daco',14,'bold'),fg='black',command=self.update)
        btn_try.place(x=33,y=107,width=150,height=30)
        btn_empty =Button(btn_frame,text=' افراغ الحقول',bg='#A3D93F',font=('Daco',14,'bold'),fg='black',command=self.clear)
        btn_empty.place(x=33,y=144,width=150,height=30)
        btn_close =Button(btn_frame,text=' اغلاق البرنامج',bg='#A3D93F',font=('Daco',14,'bold'),fg='black',command=root.quit)
        btn_close.place(x=33,y=181,width=150,height=30)
        #........البحث............
        ser_frame = Frame(self.root,bg = 'white')
        ser_frame.place(x=1,y=30,width=1042,height=35)
        lab_ser =Label(ser_frame,text='البحث عن الطالب',bg='white')
        lab_ser.place(x=940,y=5)
        com_ser=ttk.Combobox(ser_frame,justify='right',textvariable=self.ser_com)
        com_ser['value']=('id','name','emial','phone')
        com_ser.place(x=790,y=5)
        en_ser=Entry(ser_frame,textvariable=self.ser_var,justify='center',bd='2')
        en_ser.place(x=660,y=5)
        btn_search =Button(ser_frame,text=' بحث' ,font=('Daco',14,'bold'),fg='black',bg='#3FA1D9',command=self.search)
        btn_search.place(x=590,y=5,width=50,height=20)

        #عرض البيانات والنتائج ..........
        frame_results =Frame(self.root,bg='#f2f4f4')
        frame_results.place(x=1,y=70,width=1042,height=650)
        #.........scoroll.......
        scollbar_x = Scrollbar(frame_results , orient=HORIZONTAL )
        scollbar_y = Scrollbar(frame_results,orient=VERTICAL)
        #..treeview..
        self.student_table = ttk.Treeview(frame_results , 
        columns=('id','name','phone','email','certi','gender','adress'),
        xscrollcommand=scollbar_x.set ,
        yscrollcommand=scollbar_y.set )
        self.student_table.place(x=19,y=1,width=1034,height=645)
        scollbar_x.pack(side=BOTTOM,fill=Y)
        scollbar_y.pack(side=LEFT,fill=X)
        scollbar_x.config(command=self.student_table.xview)
        scollbar_y.config(command=self.student_table.yview) 
        self.student_table['show'] = 'headings'
        self.student_table.heading('adress',text='عنوان الطالب')
        self.student_table.heading('id',text='الرقم التسلسلي ')
        self.student_table.heading('email',text=' ايميل الطالب')
        self.student_table.heading('phone',text='رقم الطالب')
        self.student_table.heading('certi',text='مؤهلات الطالب')
        self.student_table.heading('gender',text='حنس الطالب')
        self.student_table.heading('name',text='اسم الطالب')
        self.student_table.column('name',width=100)
        self.student_table.column('id',width=100)
        self.student_table.column('email',width=100)
        self.student_table.column('phone',width=100)
        self.student_table.column('certi',width=100)
        self.student_table.column('gender',width=100)
        self.student_table.column('adress',width=100)
        self.student_table.bind('<ButtonRelease-1>',self.get_cursor)
        #.........data base....
        self.fatch_all()
    def data_student(self):
        con =pymysql.connect(host='localhost',user='root',password= '',database='students')
        cr = con.cursor()
        cr.execute('insert into student values(%s,%s,%s,%s,%s,%s,%s)',(
                                                    self.id_var.get(),
                                                    self.name_var.get(),
                                                    self.phone_var.get(),
                                                    self.emali_var.get(),
                                                    self.mohel_var.get(),
                                                    self.gender_var.get(),
                                                    self.adress_var.get()
                                               
                                                                     ))
        
        con.commit()
        self.fatch_all()
        self.clear()
        con.close()

    def fatch_all(self):
        con = pymysql.connect(host='localhost',user='root',password='',database='students')
        cr = con.cursor()
        cr.execute('select * from student')
        rows = cr.fetchall()
        if len(rows)!= 0 :
            self.student_table.delete(*self.student_table.get_children())
            for row in rows :
                self.student_table.insert('',END,value=row)
            con.commit()
        con.close()


    def delete(self):
        con = pymysql.connect(host='localhost',user='root',password='',database='students')
        cr = con.cursor()
        cr.execute('delete from student where id=%s ',self.del_var.get())
        
        con.commit()
        self.fatch_all()
        con.close()
    
    def clear(self):
        self.name_var.set('')
        self.id_var.set('')
        self.phone_var.set('')
        self.emali_var.set('')
        self.del_var.set('')
        self.mohel_var.set('')
        self.gender_var.set('')
        self.adress_var.set('')

    def get_cursor(self,ev):
        row_content = self.student_table.focus()
        contents = self.student_table.item(row_content)
        row=contents['values']
        self.id_var.set(row[0])
        self.name_var.set(row[1])
        self.emali_var.set(row[2])
        self.phone_var.set(row[3])
        self.mohel_var.set(row[4])
        self.gender_var.set(row[5])
        self.adress_var.set(row[6])

    def update(self):
        con =pymysql.connect(host='localhost',user='root',password= '',database='students')
        cr = con.cursor()
        cr.execute('update student set adress=%s,name=%s,phone=%s,email=%s,mohel=%s,gender=%s where id=%s  ',(
                                                    self.id_var.get(),
                                                    self.name_var.get(),
                                                    self.phone_var.get(),
                                                    self.emali_var.get(),
                                                    self.mohel_var.get(),
                                                    self.gender_var.get(),
                                                    self.adress_var.get()
                                               
                                                                     ))
        
        con.commit()
        self.fatch_all()
        self.clear()
        con.close()


    def search(self):
        con = pymysql.connect(host='localhost',user='root',password='',database='students')
        cr = con.cursor()
        cr.execute('select * from student where '+ str(self.ser_com.get())+" LIKE '%"+str(self.ser_var.get())+"%'")
        rows = cr.fetchall()
        if len(rows)!= 0 :
            self.student_table.delete(*self.student_table.get_children())
            for row in rows :
                self.student_table.insert('',END,value=row)

            con.commit()
    
        con.close()
    
   


        


root = Tk()
ob = Student(root)
root.mainloop()
