print("welcome to treasre island")
print("your mission is to find the treasure")
choice1=input('tell the direction "left" or "right".')
if choice1=="left":
    print("great !")
    choice2=input('tell whether you want to "wait" or "swim".')
    if choice2=="wait":
        print("great !")
        choice3=input('which door you want to enter through "blue","red" or "yellow".')
        if choice3=="yellow":
            print("YAY! YOU WIN")
        elif choice3=="red" or choice3=="blue":
            print("GAME OVER")
    elif choice2=="swim":
        print("GAME OVER")
elif choice1=="right":
    print("GAME OVER")
    


