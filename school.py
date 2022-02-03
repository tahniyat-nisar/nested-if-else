age=int(input("enter your age:"))
if age>=18:
    print("college jate ho ya nahi:")
    college=input("haan ya na:")
    if college=="haan":
        print("kounsa field chuna hai apne:")
        field=input("MBBS,Engineering,CA,B.Pharmacy:")
        if field=="MBBS":
            print("apko ko job milne me 5 saal lagenge")
        elif field==("CA"):
            print("apko ko job milne me 4 saal lagenge")
        elif field==("Engineering"):
            print("apko ko job milne me 4 saal lagenge")
        elif field=="B.Pharmacy":
            print("apko ko job milne me 3 saal lagenge")
    else:
        if college=="na":
            print("apki shaadi hogayi:")
            shaadi=input("haan ya na:")
            if shaadi=="haan":
                print("kounsi waali shaadi")
                kounsi=input("arrange ya love:")
                if kounsi=="arrange":
                    print("happy married life")
                elif kounsi=="love":
                    print("kahan par shadi huyi hai apki:")
                    kahan_par=input("temple ya court:")
                    if kahan_par=="temple":
                        print("God Bless You")
                    elif kahan_par=="court":
                        print("congragulations")
            else:
                if shaadi=="na":
                    print("Bas aise hi puchilya")
else:
    if age<18:
        print("apki umar",age,"ki hai toh phir ap school ja rahe ho:")
        school=input("haan ya na:")
        if school=="haan":
            print("kounsa subject apko pasand hai")
            pasand=input("sicence ya social studies:")
            if pasand==("sicence"):
                print("ap scientist,doctor,engineer,mathematician adi ban sakte ho")
                print("accha hai aur khoob padho")
            elif pasand==("social studies"):
                print("ap economist,public servent,Business man adi ban sakte ho")
                print("accha hai aur khoob padho")
        else:
            if school=="na":
                print("ap ko school jana chahiye")


        






