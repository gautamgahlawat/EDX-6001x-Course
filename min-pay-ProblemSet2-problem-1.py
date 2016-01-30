Month = 0
Total_Paid = 0
for z in range(12):
    Month += 1
    Minimum_monthly_payment = round(balance * monthlyPaymentRate,2)
    Unpaid_Balance = balance - Minimum_monthly_payment
    Total_Paid+= Minimum_monthly_payment
    Monthly_interest_rate = annualInterestRate / 12
    Interest = Monthly_interest_rate * Unpaid_Balance
    Remaining_balance = round(Unpaid_Balance + Interest,2)
    balance = Remaining_balance
    for x in range(1):
        print "Month: "+str(Month)
        print "Minimum monthly payment: "+str(Minimum_monthly_payment) 
        print "Remaining balance: "+str(Remaining_balance)
print "Total paid: "+str(Total_Paid)
print "Remaining balance: "+str(balance)
    
