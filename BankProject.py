class BankSystem():
    def __init__(self, balance):
        self.balance = 1000
        
    def deposit(self):
        confirm_deposit = input('Do you want to make a deposit? yes/no \n')
        if(confirm_deposit  == 'yes'):
            deposit_amount = eval(input('How much do you want to deposit?\n'))
            self.balance  = self.balance + deposit_amount
            print('Deposit was successful. New amount is {}'.format(self.balance))
            
    def withdraw(self):
        confirm_withdraw = input('Do you want to make a withdrawal? yes/no \n')
        if (confirm_withdraw == 'yes'):
            withdraw_amount = eval(input('How much do you want to withdraw? \n'))
            if(withdraw_amount > self.balance):
                confirm_overdraft = eval('You do not have sufficient funds to complete this transaction. \n Would you like to request an overdraft? yes/no \n')
                if(confirm_overdraft == 'yes'):
                    print('Your request is being processed and an email will be sent to you soon')
            else:
                 self.balance -= withdraw_amount
                 print('You have successfully withdrawn. Your New Amount is {}'.format(self.balance))
                    
bank = BankSystem(88)
bank.deposit()
bank.withdraw()
