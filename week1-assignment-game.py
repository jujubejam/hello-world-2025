# ascii Art
ramenVendor = """


　　　　　    ／三三三三三三三三＼
　　　　　  ／三三三三三三三三三三＼
     lllll､|￣￣|￣￣|￣￣|￣￣|￣￣|
　   l三三l|  R | A  | M  | E  | N  |
　   |三三||＿＿|＿＿|＿＿|＿＿|＿＿|＼
　   ヽ三ﾉ  || ﾐ;;....;;ﾐ　       ||　Ω
  ∬_＿_ ﾂｰ  ||（｀・ω ・´）　∬ ∬  || []
 　＼≠／ 三 || O　　 　と彡|￣￣| ||
   〔二二二二二二二二二二二二二二二二二〕
　　　   　|＿＿＿＿＿＿＿＿＿＿＿__|
           　| |  ヽ.;;;;;;,ノ | | 
￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣


"""

customerWaiting = """


            ///"\.                ///"\.  
           (・ω ・)              (・ω ・)
     @@@@@/  \./  \.       @@@@@/  \./  \.
   @(・= ・)@ :  : \.    @(・= ・)@ :  : \.
   /' \./ '\  :  | ))    /' \./ '\  :  | ))
  ((|  :  |))=o==|      ((|  :  |))=o==|
    |_____||%%|%%|        |_____||%%|%%|
    |_:_:_||%%|%%|        |_:_:_||%%|%%|
     /_|_\  /_|_\.         /_|_\  /_|_\.
   

"""

springOnion = """

( @  ( @  ( @  ( @  ( @  ( @  ( @  
( @  ( @  ( @  ( @  ( @  ( @  ( @ 
( @  ( @  ( @  ( @  ( @  ( @  ( @

"""

boiledNoodles = """


           ___,.-------..__  
     _,-'   ∬ ∬ ∬ ∬ ∬ ∬ ∬  `'--._ 
   ;'    ∬ ∬ ∬ ∬ ∬ ∬ ∬ ∬ ∬ ∬ ∬∬  `: 
  (   ∬ ∬ ∬ ∬ ∬ ∬ ∬ ∬ ∬ ∬ ∬ ∬ ∬ ∬  )
   :.   ∬ ∬ ∬ ∬ ∬ ∬ ∬ ∬ ∬ ∬ ∬ ∬ ∬ ,;
    `.`--._'_  ∬ ∬ ∬ ∬ ∬ ___.--','
      `.     ``-------''     ,'
         -.               ,-
            `-._______.-'


"""

ramenFinished = """   


           ___,.-------..__  
     _,-',-'-. @ @ @ @      `'--._ 
   ;'   / ,-. \ @ @  ∬ ∬ ∬ ∬ ∬ ∬ `: 
  (     |(   )|    ∬ ∬ ∬ ∬ ∬ ∬     )
   :.   \ `-' /   ∬ ∬ ∬ ∬ ∬ ∬    ,;
    `.`--._'_   ∬ ∬ ∬   ___.--','
      `.     ``-------''     ,'
         -.               ,-
            `-._______.-'


      """


# instrunctions
# print("Instructions: To chop, type '/'. Every '/' counts as one chop.")
# print("Instructions: To boil, type '^'. Each '^' increases fire power.")
# print("Instructions: To stir, type '@'. Each '@' counts as one stir.")

# input("\n[Press ENTER to continue]") # show next line when pressed ENTER

# step one def
def toppingChop():
    spingOnionChop = input("Chop your spring onions: ")

    if (spingOnionChop == "/" or spingOnionChop == "//" or spingOnionChop == "///" or spingOnionChop == "////"):
        print("That's slice is too big. Try again.")
        toppingChop()
    elif(spingOnionChop == "/////"):
        print("\nPerfect! Now prep the rest as well. \n(˵ •̀ ᴗ - ˵)✧")
        print("\nchop... chop...")
        input("\n[Press ENTER to continue]") # proceed step two
    else:
        print("Interesting choice... Try again.")
        toppingChop()

# step one
def topping():
    print("\nYou are going to prep the spring onions.")
    print("\nSpring onions are very important.")
    print("It not only makes the ramen taste better, but also look better. (^ᴗ ̫ ᴗ^)")

    input("\n[Press ENTER to see how to prep spring onions]") # show next line when pressed ENTER
    print("\n* Instructions: \nTo chop, type '/'. \nEvery '/' counts as one chop.")
    print("\n* Hint: \nSpring onions should be thinly chopped.\nTry to find the best cut amount!")
    
    input("\n[Press ENTER to start chopping]") # show next line when pressed ENTER
    toppingChop()


# step two def
def noodleBoiling():
    noodleFirePower = input("Set your fire power: ")

    if (noodleFirePower == "^" or noodleFirePower == "^^"):
        print("You're almost there... Try again.")
        noodleBoiling()
    elif(noodleFirePower == "^^^"):
        print("\nAmazing! \nNow wait for the water to boil so that we can add noodles.")
        print("\nboil... boil...")
        input("\n[Press ENTER to add noodles]") # proceed to stir
        noodle2()
    elif(noodleFirePower == "^^^^" or noodleFirePower == "^^^^^" or noodleFirePower == "^^^^^^" or noodleFirePower == "^^^^^^^"):
        print("Easy with the heat," + playerName + "..!")
        print("We're not trying to burn down the stall.")
        noodleBoiling()
    else:
        print("(ఠ ̥̆ ఠ)")
        print("Hmm, that's a unique choice. Give it another shot!")
        noodleBoiling()

# step two
def noodle1():
    print("\nWe should boil the water first.")
    print("The trick is to find the perfect fire power.")

    input("\n[Press ENTER to see how to boil water]") # show next line when pressed ENTER
    print("\n* Instructions: \nTo boil, type '^'. \nEach '^' increases fire power.")
    
    input("\n[Press ENTER to start boiling water]") # show next line when pressed ENTER
    noodleBoiling()
  

# step three def
def noodleStir():
    noodleStirCount = input("Stir your pot: ")
    
    if (noodleStirCount == "@" or noodleStirCount == "@@" or noodleStirCount == "@@@" or noodleStirCount == "@@@@" or noodleStirCount == "@@@@@" or noodleStirCount == "@@@@@@" or noodleStirCount == 
    "@@@@@@@"):
        print("You need some more stir-stir.")
        noodleStir()
    elif(noodleStirCount == "@@@@@@@@"):
        print("\nYou're a natural! (灬^▽^灬ʃƪ）")
        print("Stir a few more minutes. \nThen, place it in a bowl.")
        print("\nstir...stir...")
        input("\n[Press ENTER to place it in a bowl]") # proceed to serve
    else:
        print("Uh...Wanna retry?")
        noodleStir()


# step three
def noodle2():
    print("\nDon't forget to give it a good stir.")
    print("The noodles might stick to the pot if you don't stir it enough.")

    input("\n[Press ENTER to see how to stir]") # show next line when pressed ENTER
    print("\n* Instructions: \nTo stir, type '@'. \nEach '@' counts as one stir.")
    
    input("\n[Press ENTER to start stirring]") # show next line when pressed ENTER
    noodleStir()



# intro def
def consent1():
    answer1 = input("\n( ᖛ ̫ ᖛ ) ◦oO(Say 'Sure'...): ")
    if (answer1 == "Sure"):
        print("\nThat's the spirit!")
        topping()
    else:
        print("\nΣ(； ･`д･´)")
        print("Come again?")
        consent1()

# intro
print(ramenVendor)

print("Welcome! You must be our new assistant.")
playerName = input("What should I call you?: ")
print("\nNice to meet you, " + playerName)

print("\n\nI know you just got here, but...")
print("I'm quite busy opening the shop right now.")
print("\nLook at all the customers waiting!")
print(customerWaiting)

input("\n[Press ENTER to continue]") # show next line when pressed ENTER
print("\nLet's catch up later!")
print("Can you help me with the toppings prep first?")
consent1()


# after spring onion def
def consent2():
    answer2 = input("\n( ˶ˆ꒳ˆ˵ ) ◦oO(Say 'Okay'...): ")
    if (answer2 == "Okay"):
        print("\nThanks a lot!")
        noodle1()
    else:
        print("\nΣ(； ･`д･´)")
        print("Come again?")
        consent2()

# after spring onion
print("Oh! Prepping is done? Let me see.")
input("\n[Press ENTER to show off your work]") # show next line when pressed ENTER
print(springOnion)

print("*⁂((✪⥎✪))⁂*")
print("Nice job, " + playerName + "!")

input("\n[Press ENTER to continue]")
print("\nCan I trust you with cooking the noodles as well?")
consent2()

# after noodle: assemble and serve
print(boiledNoodles)
print("Looks so yummy! \nIt's perfection.")
print("\nPlace all the toppings on top, and we're ready to serve!")

input("\n[Press ENTER to place toppings]") 
print("\nsprinkle...sprinkle...")

input("\n[Press ENTER to see end result]") 
print(ramenFinished)
print("It looks fire!")