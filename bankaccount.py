''' A bank account experience that allows you to view the balance of, deposit to and withdraw from your account'''

def BankAccount(object):
  balance = 0
  
  def __init__ (self, name):
    self.name = name
    
    
  def __repr__(self):
    print "test 2"
    return "%s's account. Balanace: %.2f" %(self.name, self.balance)

  def show_balance(self):
    print "Balance: %.2f" % self.balance
    
  def deposit(self, amount):
    if amount <= 0:
      print "You can't deposit that amount"
      return
    else:
      print "Depositing $%.2f..." % amount
      self.balance += amount
      self.show_balance()
      
  def withdraw(self, amount):
    if amount >self.balance:
      print "You can't withdraw that amount"
      return
    else:
      print "Withdrawing $%.2f..." % amount
      self.balance -= amount
      self.show_balance()
      
my_account = BankAccount("Your-name-here")
print my_account
my_account.show_balance()
account.deposit(2000)
account.withdraw(1000)
print account

    