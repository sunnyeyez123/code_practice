'''a program that will calculate the monthly car payment a user should expect
to make after taking out a car loan*/  '''


def CarLoan():
  car_loan = 10000
  loan_length = 3
  interest_rate = 5
  down_payment =2000

  if loan_length <= 0 or interest_rate <=0:
    print "Error! You must take out a valid car loan."
  elif( down_payment > car_loan):
    print "The car can be paid in full."
  else:
    remaining_balance = car_loan - down_payment
    months = loan_length *12
    monthly_balance = remaining_balance/months
    interest = (monthly_balance*interest_rate)/100
    monthly_payment = monthly_balance + interest
    print monthly_payment


CarLoan()
