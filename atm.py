print("welcome to sbi")
card=(input("insert the card:"))
if card=="credit" or "debit":
    print("in process")
    language=(input("select a language 'english':"))
    if language=="english":
        print("click next")
        pin=int(input("enter the 4-digit number:"))
        if pin==1999:
            print('proceed')
            type=input("select the type of account:")
            if type=="current" or 'saving':
                print("click ok")
                transaction=input("select the type of transaction:")
                if transaction=="withdrawal":
                    print('click next')
                    amount=int(input("enter the amount Rs.-----:"))
                    if amount>500 and amount<500000:
                        print("your transaction being processed")
                        balance=int(input("enter your last account balance:"))
                        if balance>500:
                            print(balance-amount)
                            print("is your remaining balance after transaction")
                            print("please collect your cash")
                            reciept=input("would you like to take reciept:")
                            if reciept=="yes":
                                print("your transaction is sucessful,thank you so much :)")
                            else:
                                print:("thank you for saving trees :)")
                        else:
                            print("sorry transaction cannot be processed")
                            print("inorder to maintain minimum balance in your account")
                    else:
                        print("no cash or")
                        print("you enter the amount above the transaction limit")
                else:
                    print("please select any one of the options")
            else:
                print("currently other services are not available sorry for inconvience")
        else:
            print("please enter correct pin")
    else:
        print("please select any one of the language")
else:
    print(" remove your card and insert it again")