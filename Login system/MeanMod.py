from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration")
        self.root.geometry("865x486+200+60")
        self.root.config(bg="white")
        
        #### BG Image ####
        self.bg=ImageTk.PhotoImage(file="images/math.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        main_frame=Frame(self.root,bg="white")
        main_frame.place(x=60,y=60,width=750,height=400)

        title=Label(main_frame,text="Mean Median Mode Calculator",font=("times new roman",25,"bold"),fg="lightgreen",bg="grey").pack()  #.place(x=0,y=0,width=750)

        nums=Label(main_frame,text="Enter numbers for calculation with comma(,) separated",font=("times new roman",20,"bold"),fg="black",bg="white").place(x=60,y=90)
        nums_var=StringVar()
        txt_nums=Entry(main_frame,textvariable=nums_var,font=("times new roman",15),bg="lightgrey")
        txt_nums.place(x=60,y=140,width=500,height=30)

        mean=Label(main_frame,text="Mean              :",font=("times new roman",25,"bold"),fg="black",bg="white").place(x=60,y=235)
        median=Label(main_frame,text="Median           :",font=("times new roman",25,"bold"),fg="black",bg="white").place(x=60,y=280)
        mode=Label(main_frame,text="Mode              :",font=("times new roman",25,"bold"),fg="black",bg="white").place(x=60,y=325)

        txt_mean=Entry(main_frame,font=("times new roman",15),bg="lightgrey")
        txt_mean.place(x=300,y=245)
        txt_median=Entry(main_frame,font=("times new roman",15),bg="lightgrey")
        txt_median.place(x=300,y=290)
        txt_mode=Entry(main_frame,font=("times new roman",15),bg="lightgrey")
        txt_mode.place(x=300,y=335)

        def calculate():
            try:
                if nums_var.get()=="":
                    messagebox.showerror("Error","Please enter numbers",parent=root)
                else:
                    ls=nums_var.get()
                    userlist=ls.split(",")
                    userlist=[int(i) for i in userlist]
                    meanvalue=str(Mean(userlist))
                    medianvalue=str(Median(userlist))
                    modevalue=str(Mode(userlist))
                    txt_mean.insert(5,meanvalue)
                    txt_median.insert(0,medianvalue)
                    txt_mode.insert(0,modevalue)
            except Exception as es:
                        messagebox.showerror("Error",f"Error due to {str(es)}",parent=root)
        def Mean(list_of_num):
            total=0
            for num in list_of_num:
                total+=num
            return total/len(list_of_num)

        def Mode(list_of_num):
            max_count=(0,0)
            for num in list_of_num:
                occurence=list_of_num.count(num)
                if occurence >max_count[0]:
                    max_count=(occurence,num)
            return max_count

        def Median(list_of_num):
            list_of_num.sort()
            if len(list_of_num) %2!=0:
                middle_index=int((len(list_of_num)-1)/2)
                return list_of_num[middle_index]
            elif len(list_of_num)%2==0:
                middle_index1=int(len(list_of_num)/2)
                middle_index2=int(len(list_of_num)/2)-1
                return (list_of_num[middle_index1]+list_of_num[middle_index2])/2
        
        btn_submit=Button(main_frame,text="Calculate",command=calculate,font=("times new roman",14),cursor="hand2",bd=0,bg="lightgreen",fg="White").place(x=60,y=180,width=300,height=35)
        btn_mean=Button(main_frame,text="Calculate",command=calculate,font=("times new roman",14),cursor="hand2",bd=0,bg="lightgreen",fg="White").place(x=100,y=180,width=300,height=35)
        
root=Tk()
obj=Register(root)
root.mainloop()
