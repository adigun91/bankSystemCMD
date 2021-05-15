from tkinter import *
root = Tk()
entry = Entry() #used to get input from users

d_label = Label(text='Enter the amount you want to deposit or withdraw below \n and click the appropriate button.',font=('verdana',18,'bold'), width=50)
d_label.grid(row=1,column=1,columnspan=5)

class BankSystemGUI():
    def __init__(self):
        self.balance = 1000
        self.user_input = Entry(font=('verdana',16,'bold'))
        self.user_input.grid(row=2,column=1,columnspan=5)
        
    def deposit(self):
        d_input = eval(Entry.get(self.user_input))
        self.balance += d_input
        d_label.configure(text='Deposit Successful!!! Your account balance is now {}'.format(self.balance))
        
    def withdraw(self):
        d_input = eval(Entry.get(self.user_input))
        if(d_input>self.balance):
            d_label.configure(text='You do not have sufficient balance. Would you like to request for an overdraft? yes/no \n')
            d_input2 = Entry.get(self.user_input)
            if(d_input2 == 'yes'):
                d_label.configure(text='Your request is being reviewed')
            else:
                d_label.configure(tex='Please try again later')
        else:
            self.balance += d_input
            d_label.configure(text='Withdraw Successful!!! Your account balance is now {}'.format(self.balance))
            

bank = BankSystemGUI()

deposit_btn = Button(text='Deposit', font=('verdana',18,'bold'), bg='green', command=bank.deposit, fg='black')
withdraw_btn = Button(text='Withdraw', font=('verdana',18,'bold'), bg='blue', command=bank.withdraw, fg='black')

deposit_btn.grid(row=4,column=2)
withdraw_btn.grid(row=4,column=4)

mainloop()