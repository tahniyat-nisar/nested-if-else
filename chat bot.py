print("welcome to XYZ helpdesk,I am here to help you and will connect you to a customer support agent(through call,chat or email)\nIf i don't have answer.")
print("what can i help you with:-")
print("1.Delivery related query")
print("2.cancel order")
print("3.others")
user_input=int(input("choose a number:-"))
if (user_input==1):
    print("1.delivery agent number")
    print("2.where is my order")
    print("3.faster delivery request")
    user_prblm=int(input("choose a number:-"))
    if user_prblm==1:
        print("'9112778890'is your delivery agent number")
        print("make a call to track your order")
    elif user_prblm==2:
            print("I'm sorry that your product has not been delivered yet")
            print("I have raised a complaint and you will recieve an update by tommorrow")
    else:
        if user_prblm==3:
                print("ok we have placed fast delivery request on your item")
                print("but you may need to pay additional charges to it")
elif (user_input==2):
    print("ok this item will get added to later")  
else:
    if user_input==3:
        print("name the issue" )     
        prblm=input("describe the other issues:-")
        print("we understand and apologize for the inconvience you have been facing our team will be working on it.")
