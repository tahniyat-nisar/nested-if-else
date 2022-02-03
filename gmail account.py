first_name=input("enter your first name:-")
if first_name>="A" and first_name<="z":
    print("next")
    last_name=input("enter your last name:-")
    if last_name>="A" and last_name<="z":
        print("next")
        print(first_name ,last_name)
        user_name=input("enter the user name:-")
        if user_name>="A" and user_name<="z":
            print("next")
            print("ok",user_name)
            print("enter a strong password mixed of numbers and characters:-\n for that let's take few steps:-")
            var_a=input("enter atleast one upper case and lower case letters:")
            if (var_a>="A" and var_a<="Z")or(var_a>="a" and var_a<="z"):
                print("next")
                var_b=input("enter atleast one special character:")
                if var_b in ("~!@#$%&*+:;'.?/%^-_='\|`"):
                    print("next")
                    var_c=int(input("enter atleast one number:"))
                    if var_c>=0 and var_c<=1000:
                       var_d=(var_a+var_b+str(var_c))
                       print(var_d)
                     # if var_c in ("0123456789"):
                     # if var_c==str(0,1,2,3,4,5,6,7,8,9):
                     #     print(var_a+var_b+var_c)
                       if len(var_d)==8:
                           print(" now you have password is strong")
                           mobile_num=(input ("enter your mobile number:"))
                           if len(mobile_num)==10:
                               print("confirm your mobile number")
                               print(mobile_num)
                               verification=(input("enter a 4-digit verfication code send to your mobile number:"))
                               if len(verification)==4:
                                   print("checking...")
                                   print("submit")
                                   print("congragulations, welocome to your new gmail account")
                               else:
                                   print('please check the code')
                                   print("click resend code button")
                           else:
                               print("please enter correct mobile number")
                       else:
                            print("it is not strong password?\nplease enter 8 characters only")
                    else:
                        print("please enter atleast one number")
                else:
                    print("please enter atleast one special character")
            else:
                print("please enter atleast one upper and lower case letter ")
        else:
            print(" please enter your username in letter only")
    else:
        print("please enter your last name only")
else:
    print("please enter your first name only")
            
            


                        
                


            
        




