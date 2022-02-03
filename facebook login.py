print("enter your user name or email ID:-")
#name=input("enter your user name:")
user_name=input("Do you have user name then type it if not then press 'enter'':-")
if ((user_name>="a"and user_name<="z")or(user_name>="A" and user_name<="Z")):
    print("checking...")
    password=input("enter your password or type forgot password:-")
    if password=="Ab12@!7":
        print("log in")
        print("welcome to your facebook account")
        print("click 'continue' to get started")
    elif password=="forgot password":
        forgot_password=int(input("enter your mobile number to send verifiction code:"))
        # if len(forgot_password)==10
        if forgot_password<=9999999999:
            var_a=input("confirm your mobile number by 'yes' or 'no':-")
            if var_a=="yes":
                print(forgot_password)
                print("ok proceed")
                verification=input("enter 4-digit verification code:-")
                if len(verification)==4:
                    print("ok your verification code is:",verification)
                    print("now create new strong password mixed of numbers,characters and special characters")
                    print("let's take a few steps to create a pasword:-")
                    step_1=(input("enter upper case or lower case letter:-"))
                    if (step_1>="A"and step_1<="Z")or(step_1>="a" and step_1<="z"):
                        print("ok next")
                        step_2=int(input("enter a number:"))
                        if step_2>=0:
                            print("ok next")
                            step_3=(input("enter a special character:"))
                            if step_3 in ("~!@#$%^&*_-=+:;,./\|'"):
                                print("ok")
                                if len(step_1+str(step_2)+step_3)==8:                                    
                                    print("your new password:-",step_1+str(step_2)+step_3)
                                    print("click on log in")
                                    print("continue")
                                else:
                                    print("please enter 8 characters only")
                            else:
                                print("please enter atleast one special character")
                        else:
                            print("please enter atleast one number")
                    else:
                        print("please enter atleast one upper case and lower case letter")
                else:
                    print("please enter code correctly")
                    print("click on resend the code")
            else:
                if var_a=="no":
                    print("renter your mobile number")
        else:
            print("please check and enter valid 10 digit mobile number")
    else:
        print("incorrect password")
else:
    email=input("enter your email address:-")
    if((email>="a"and email<="z")or(email>="A" and email<="Z"))or(email in (0,1,2,3,4,5,6,7,8,9)or(emai in(_, ))):
        print(email+"@gmail.com")
        password=input("enter your password or type forgot password:-")
    if password=="Ab12@!7":
        print("log in")
        print("welcome to your facebook account")
        print("click 'continue' to get started")
    elif password=="forgot password":
        forgot_password=int(input("enter your mobile number to send verifiction code:"))
        # if len(forgot_password)==10
        if forgot_password<=9999999999:
            var_a=input("confirm your mobile number by 'yes' or 'no':-")
            if var_a=="yes":
                print(forgot_password)
                print("ok proceed")
                verification=input("enter 4-digit verification code:-")
                if len(verification)==4:
                    print("ok your verification code is:",verification)
                    print("now create new strong password mixed of numbers,characters and special characters")
                    print("let's take a few steps to create a pasword:-")
                    step_1=(input("enter upper case or lower case letter:-"))
                    if (step_1>="a"and step_1<="z")or(step_1>="A"and step_1<="Z"):
                        print("ok next")
                        step_2=int(input("enter a number:"))
                        if (step_2>=0):
                            print("ok next")
                            step_3=(input("enter a special character:"))
                            if step_3 in ("~!@#$%^&*_-=+:;,./\|'"):
                                print("ok")
                                if len(step_1+str(step_2)+step_3)==8:                                    
                                    print("your new password:-",step_1+str(step_2)+step_3)
                                    print("click on log in")
                                else:
                                    print("please enter 8 characters only")
                            else:
                                print("please enter atleast one special character")
                        else:
                            print("please enter atleast one number")
                    else:
                        print("please enter atleast one upper case and lower case letter")
                else:
                    print("please enter code correctly")
                    print("click on resend the code")
            else:
                if var_a=="no":
                    print("renter your mobile number")
        else:
            print("please check and enter valid 10 digit mobile number")
    else:
        print("incorrect password")

