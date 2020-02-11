#!/usr/bin/python3
# I wrote and debugged this code with all the convoluted "EAT" variable names.
# Was it confusing? Yes. Was debugging hard? Yes.
# Did I spend more time than I should have on this problem? Yes

def Eating(eat):
    return str(int(eat)*EATEATEAT)

# Merge eat and eats. For every 1 character in eats, add 2 from eat
# For example EAt("111111", "aaa") == "a11a11a11"
def EAt(eat, eats):
    print(eat, eats)
    eat1 = 0
    eat2 = 0
    eateat = 0 # index
    eAt = ""
    # while 1 and 2 are both less than (eat)
    while eat1 < len(eat) and eat2 < len(eats):
        # if eateat % 3 == 0
        if eateat%EATEATEAT == EATEATEATEATEAT//EATEATEATEAT:
            eAt += eats[eat2]
            eat2 += 1
        else:
            eAt += eat[eat1]
            eat1 += 1
        eateat += 1
    return eAt

# reverse
def aten(eat):
    return eat[::EATEATEAT-EATEATEATEAT]

def eaT(eat):
    return Eating(eat[:EATEATEAT]) + aten(eat)

# just an identity function
def aTE(eat):
    return eat#*len(eat)

# When input is len 3 = Eat9{123}
def Ate(eat):
    return "Eat" + str(len(eat)) + eat[:EATEATEAT]

def Eat(eat):
    # length of parameter must be 9
    if len(eat) == 9:
        # if str.isdigit(eat[:3]) and str.isdigit(eat[7:])
        # starts with 3 numbers and ends with 3 numbers
        if str.isdigit(eat[:EATEATEAT]) and\
            str.isdigit(eat[len(eat)-EATEATEAT+1:]):
                # eateat = EAt(, reverse(eat))
                a = eaT(eat)
                print("===", a)
                b = Ate(aten(eat))
                print("+++", b)
                eateat = EAt(a, b)
                print(aten(eat))
                if eateat == "E10a23t9090t9ae0140":
                    flag = "eaten_" + eat
                    print("absolutely EATEN!!! CTFlearn{",flag,"}")
                else:
                    print("thats not the answer. you formatted it fine tho, here's what you got\n>>", eateat)
        else:
            print("thats not the answer. bad format :(\n(hint: 123abc456 is an example of good format)")
    else:
        print("thats not the answer. bad length :(")

print("what's the answer")
eat = input()
EATEATEAT = len(eat)//3 # len(eat) // 3
EATEATEATEAT = EATEATEAT+1
EATEATEATEATEAT = EATEATEAT-1
Eat(eat)
