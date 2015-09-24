import time

MainMenu = True
while MainMenu:

    odd = True
    prime = True
    binary = True
    physics = True


    print "-----------------"
    print "-----Welcome-----"
    print "-------to--------"
    print "------Pyth-------"
    print "-----------------"
    print "-------By:-------"
    print "------Pedro------"
    print "-----------------"

    time.sleep(1)
    
    print "Programs:"
    print "         Odd Numbers[1]"
    print "         Prime Numbers[2]"
    print "         Number to Binary[3]"
    print "         Physics Simulator[4]"
    print "         Exit[ext]"
    program = raw_input()

    if program == "1":
        print "Loading..."
        time.sleep(.7)
        print "---------------"
        print "--Odd Numbers--"
        print "---------------"
        time.sleep(1)
        while odd:
            print "Enter Number:",
            n = raw_input()
            if n == "ext":
                prime = False
                break
            n = float(n)
            if n % 2 == 1:
               print n,
               print "is a odd number."
            if n % 2 == 0:
                print n,
                print " is a pair number."
    

    if program == "2":
        print "Loading..."
        time.sleep(.7)
        print "-----------------"
        print "--Prime Numbers--"
        print "-----------------"
        time.sleep(1)
        while prime:
            print "Enter Number:",
            n = raw_input()
            if not n == "2":
                if n == "ext":
                    prime = False
                    break
                n = float(n)
                if n % 2 == 1:
                    y = n / 3.0
                    while y > 0:
                        y = y - 1
                    if not y == 0:
                       print n,
                       print " is not a prime number."
                    if y == 0:
                        print n,
                        print " is a prime number."
                if n % 2 == 0:
                    print n,
                    print " is not a prime number."
            if n == "1":
                print n,
                print " is not a prime number."
            if n == "2":
                print n,
                print "is a prime number."



    if program == "3":
        print "Loading..."
        time.sleep(.7)
        print "------------------"
        print "-Number to Binary-"
        print "------------------"
        time.sleep(1)
        while binary:
            equ = "="
            print "Enter number to convert:"
            s = raw_input()
            if s == "ext":
                binary = False
                break

            v = int(s) 

            bina = bin(v)[2:]  

            print v,
            print equ,
            print bina
    

    if program == "4":
        print "Loading..."
        time.sleep(.7)
        print "-------------------"
        print "-Physics Simulator-"
        print "-------------------"
        time.sleep(1)
        while physics:
            print "What height is the start(meters): " ,
            y0 = raw_input()

            if y0 == "ext":
                physics = False
                break

            print "What is the force being applied at the start: ",
            v0 = raw_input()

            if v0 == "ext":
                physics = False
                break

            a = -9.8
            dt = 0.01
            t = 0
            v = float(v0)
            y = float(y0)
            ymax = 0.0

            while y > -0.0000000001:
                t = t + dt
                v = v + a * dt
                y = y + v * dt

                if y > ymax:
                    ymax = y

            print "Time taken: " + str(t) + "s"
            print "Final velocity:" + str(v) + " m/s"
            print "Max Height: " + str(ymax) + " m"        


    if program == "ext":
        MainMenu = False


    
