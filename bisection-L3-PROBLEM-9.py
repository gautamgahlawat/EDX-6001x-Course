print "Please think of a number between 0 and 100!"
x= 100
low = 0
high = x
guess_number = (high+low)/2
while True:
    print "Is your secret number" +str(guess_number)+"?"
    user_input = raw_input("Enter 'h' to indicate the guess is too high. \
    Enter 'l' to indicate the guess is too low. \
    Enter 'c' to indicate I guessed correctly.")
    if user_input == 'h':
        high = guess_number
        guess_number = (high+low)/2
    elif user_input =='l':
        low = guess_number
        guess_number = (high+low)/2
    elif user_input == 'c':
        print "Game over. Your secret number was:" +str(guess_number)
        break
    else:
        print "Sorry, I did not understand your input."