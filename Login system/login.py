from tkinter import*
from PIL import Image,ImageTk,ImageDraw
import pymysql
from tkinter import messagebox
import random
import smtplib
from math import*
class Login_window:
    
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN")
        self.root.geometry("1365x767+0+0")
        self.root.config(bg="white")

        #### Image ####
        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=700)

        right_lbl=Label(self.root,bg="#031F3C",bd=0)
        right_lbl.place(x=700,y=0,relheight=1,relwidth=1)
        
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=120,width=900,height=500)

        self.bg=ImageTk.PhotoImage(file="images/account.png")
        bg=Label(login_frame,image=self.bg,bd=0).place(x=90,y=150)

        title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),fg="lightgreen",bg="white").place(x=295,y=80)
        email=Label(login_frame,text="E-MAIL ADDRESS",font=("times new roman",20,"bold"),fg="grey",bg="white").place(x=295,y=150)
        self.txt_email=Entry(login_frame,font=("times new roman",15),bg="lightgrey")
        self.txt_email.place(x=295,y=190,width=350,height=30)

        pass_=Label(login_frame,text="PASSWORD",font=("times new roman",20,"bold"),fg="grey",bg="white").place(x=295,y=230)
        self.txt_pass_=Entry(login_frame,font=("times new roman",15),bg="lightgrey")
        self.txt_pass_.place(x=295,y=270,width=350,height=30)

        btn_reg=Button(login_frame,text="Register new Account",command=self.signup_window,font=("times new roman",14),cursor="hand2",bd=0,bg="white",fg="green").place(x=295,y=310)
        btn_login=Button(login_frame,text="Login",command=self.login,font=("times new roman",25),cursor="hand2",bd=0,bg="lightgreen",fg="green").place(x=295,y=350,width=350,height=50)
    
    def signup_window(self):
        self.root.destroy()
        import signup
    
    def login(self):
        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="registrationinfo")
                cur=con.cursor()
                cur.execute("select * from user where email=%s and password=%s",(self.txt_email.get(),self.txt_pass_.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.root)
                else:
                    # messagebox.showinfo("Success","Welcome, Please verify otp which is send to your phone no.",parent=self.root)
                    self.root2=root
                    self.root2.title("OTP Verification")
                    self.root2.geometry("400x400+450+150")
                    self.root2.config(bg="white")
                    self.root2.resizable(False,False)

                    forget_frame=Frame(self.root,bg="white")
                    forget_frame.place(x=0,y=0,relwidth=1,relheight=1)

          ##########------------ To verify OTP           
                    def otpverify():
                        try:
                            
                            if otpkey != int(self.txt_otp.get()):
                                messagebox.showerror("Error","INVALID OTP ENTERED",parent=self.root2)
                            elif self.txt_otp.get()=="":
                                messagebox.showerror("Error","Please enter otp is sent to you email",parent=self.root2)
                            elif otpkey == int(self.txt_otp.get()):
                                    messagebox.showinfo("Success","Correct OTP",parent=self.root2)
                                    self.root.destroy()
                                    import MeanMod
                        except Exception as es:
                            messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root2)
          
          ###########-------------To Send OTP          
                    def sendotp(code):
                        server=smtplib.SMTP('smtp.gmail.com',587)
                        server.starttls()
                        server.login('rohanpandey2120@gmail.com','qglivxurcbzqvnko')
                        msg="Hello Your OTP is"+ str(code)
                        server.sendmail('rohanpandey2120@gmail.com',self.txt_email.get(),msg)
                        server.quit()
          ###########-----------------------to Generate OTP          
                    def otpcreator():
                        otpkey1=random.randint(1000,9999)
                        print(otpkey1)
                        print(type(otpkey1))
                        sendotp(otpkey1)
                        return otpkey1
                    otpkey=otpcreator()

          ###########-----------Labels of OTP Verificaation Window           
                    otp=Label(forget_frame,text="OTP Verification",font=("times new roman",25,"bold"),fg="grey",bg="lightgreen")
                    otp.place(x=0,y=30,width=420)
                    self.txt_otp=Entry(forget_frame,font=("times new roman",15),bg="lightgrey")
                    self.txt_otp.place(x=98,y=120,width=200,height=30)

                    btn_submit=Button(forget_frame,text="Submit",command=otpverify,font=("times new roman",14),cursor="hand2",bd=0,bg="lightgreen",fg="white").place(x=100,y=180,width=200,height=35)
                    btn_resend=Button(forget_frame,text="Resend OTP",command=otpcreator,font=("times new roman",14),cursor="hand2",bd=0,bg="lightgreen",fg="white").place(x=100,y=220,width=200,height=35)
                con.close()
            except Exception as es:
                    messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)

    
root=Tk()
obj=Login_window(root)
root.mainloop()