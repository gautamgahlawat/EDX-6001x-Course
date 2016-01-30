real_balance = balance
lower_bound = balance / 12
Monthly_interest_rate = annualInterestRate / 12
upper_bound =(balance*(1+ Monthly_interest_rate)**12)/12.0
guess_ans = (lower_bound + upper_bound)/2
def year(payment, real_balance):
    '''
    takes in the payment which is the guess_ans and real_balance 
    which is the balance given
    as like the previos problem set.
    '''
    for z in range(12):
        
        Monthly_interest_rate = annualInterestRate / 12
        Unpaid_Balance = real_balance - guess_ans
        Interest = Monthly_interest_rate * Unpaid_Balance
        Remaining_balance = round(Unpaid_Balance + Interest,2)
        real_balance = Remaining_balance
        if real_balance <= 0:
            break
    return real_balance
    
while True:
    x = year(guess_ans,balance)
    if abs(x-0.01)<0.1:
       print("Lowest Payment: " + str(guess_ans));
       break;     
    elif x<0:
       upper_bound = guess_ans;
       guess_ans = round((upper_bound+lower_bound)/2,2);
    else :
       lower_bound = guess_ans;
       guess_ans = round((upper_bound+lower_bound)/2,2);