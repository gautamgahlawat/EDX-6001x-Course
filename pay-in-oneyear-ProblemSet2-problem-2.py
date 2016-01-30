real_balance = balance
min_payment= 10
Month = 0

while True:
    for z in range(12):
        Month += 1 
        Monthly_interest_rate = annualInterestRate / 12
        Unpaid_Balance = balance - min_payment
        Interest = Monthly_interest_rate * Unpaid_Balance
        Remaining_balance = round(Unpaid_Balance + Interest,2)
        balance = Remaining_balance
        
    if  balance>0:
        min_payment +=10
        balance = real_balance
    else:
        print "Lowest Payment: "+str(min_payment)
        break
        

    
    
