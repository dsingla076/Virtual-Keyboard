from tkinter import *
from PIL import ImageTk

#functinality part

def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)
    
def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)
    


def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)
            
def signup_page():
    login_window.destroy()
    import signup


login_window=Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0,0)
login_window.title('Login Page')
bgImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(login_window,image=bgImage)

bgLabel.place(x=0,y=0)

heading=Label(login_window,text='USER LOGIN',font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='firebrick1')
heading.place(x=605,y=120)

usernameEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)

Frame1=Frame(login_window,width=250,height=2,bg='firebrick1').place(x=580,y=222)

passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',password_enter)
Frame2=Frame(login_window,width=250,height=2,bg='firebrick1').place(x=580,y=282)

openeye=PhotoImage(file='openeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2'
                 ,command=hide)
eyeButton.place(x=800,y=255)


forwardButton=Button(login_window,text="Forward Password?",bd=0,bg='white',activebackground='white',cursor='hand2' ,font=('Microsoft Yahei UI Light',9,'bold'),fg='firebrick1',activeforeground='firebrick')
forwardButton.place(x=715,y=290)

LoginButton=Button(login_window,text='Login', font=('Open Sans', 16, 'bold'), fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=0,width=19)  
LoginButton.place(x=578,y=350)

orLabel=Label(login_window,text='----------------OR---------------' ,font=('Open Sans', 16),fg='firebrick1',bg='white')
orLabel.place(x=583,y=400)

facebook_logo=PhotoImage(file='facebook.png')
fbLabel=Label(login_window, image=facebook_logo,bg='white')
fbLabel.place(x=640,y=440)

google_logo=PhotoImage(file='google.png')
googleLabel=Label(login_window, image=google_logo,bg='white')
googleLabel.place(x=690,y=440)

twitter_logo=PhotoImage(file='twitter.png')
twitterLabel=Label(login_window, image=twitter_logo,bg='white')
twitterLabel.place(x=740,y=440)

signupLabel=Label(login_window, text="Don't have an account?", font=('Open Sans', '9', 'bold'), bg='white',fg='firebrick1') 
signupLabel.place(x=590,y=500)

newaccountButton=Button(login_window,text='Create new one', font=('Open Sans', 9, 'bold underline'), fg='blue',bg='white',activeforeground='blue',activebackground='white',cursor='hand2',bd=0,command=signup_page)  
newaccountButton.place(x=727,y=500)

login_window.mainloop()