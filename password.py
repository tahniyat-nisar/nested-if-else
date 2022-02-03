var_a=input("enter atleast one upper case letter and lower case:-")
if (var_a>="a" and var_a<="z")or(var_a>="A"and var_a<="Z"):
    pass
    # print("next")
    b=int(input("enter atleast one digit:-"))
    if b>=0:
        pass
        # print("next")
        c=input("enter a special character:-")
        # if c=="@" or c=="#" or c=="!" or c=="~" or c=="&" or c=="$" or c=="%" or c=="*":
        if c in ("@#!~%&*$"):
            d=(var_a+str(b)+c)
            print(d)
            if len(d)>0:
                print("it is a strong password")
            else:
                print("it is not strong password")
        else:
            ("please enter atleast one special character")
    else:
        ("please enter atleast one number")
else:
    ("please enter a uppercase and lowercase letters only")







# psswrd=input("enter a strong password:-")
# if psswrd>="A" and psswrd<='Z':
#     if psswrd>="a" and psswrd<="z":
#         if psswrd>=0:
#         #   if psswrd in ("0123456789"):
#            if psswrd in ("~,!,@,#,$,%,&,*"):
#                if len(psswrd)==8:
#                     print(psswrd)
#                     print("sign in")
#                else:
#                     print("your password should have 8 characters only")
#            else:
#                 print("please enter atleast one special characters ")
#         else:
#             print("please enter atleast one number ")
#     else:
#         print("please enter atleast one lower case alphabet")
# else:
#     print("please enter atleast one upper case alphabet")



