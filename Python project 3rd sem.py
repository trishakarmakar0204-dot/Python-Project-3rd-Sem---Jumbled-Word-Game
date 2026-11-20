import random as r
p1=input("Enter the 1st player name: ")
p2=input("Enter the 2nd player name: ")
print("Maximum number of rounds is 5.")
count=int(input("Enter the number of rounds you want to play: "))
print("\nWelcome,",p1,"and",p2,"to the jumbled word game\n***RULES***\n1.Enter your guess\n2.If it's correct then you get +1 point\n3.If your guess is wrong then you receive no point.\n4.If you end/Stop the game simply type Quit")
correct= ["FLOWER","RABBIT", "SCHOOL", "UMBRELLA", "DOG","MECHANIC","LEVEL","SCRIPT","PHYSICS","ANIMATION"]
jumbled= ["WOFELR","TRIBAB", "LOCHOS", "ALLUMBRE", "OGD","MCEHINAC","LLVEE","ICPSTR","IHPYCSS","AMAINTNIO"]
score1 = 0
score2 = 0
current_player="Player1"
print("\n==========Let's Play the Jumbled Word Game==========")
flag=0
while True:
        index=r.randint(0,9)
        if flag==count:
            break
        if current_player=="Player1":
            print(f"{p1}'s turn")
        else:
            print(f"{p2}'s turn")
        print("The jumbled word is: ",jumbled[index])
        a=input("Enter your guess or quit..: ").upper()
        if a=="QUIT":
          break
        if current_player=="Player1" and a==correct[index]:
            score1+=1
        '''elif current_player=="Player1" and a!=correct[index]:
            continue'''
        if current_player=="Player2" and a==correct[index]:
            score2+=1
        '''elif current_player=="Player2" and a!=correct[index]:
            continue'''
        if a==correct[index]:
            print("Excellent!🎉You got +1 point\n")
        else:
          print("Wrong guess❌\n")
        if current_player=="Player1":
            current_player="Player2"
        else:
            current_player="Player1"
        print("**Score Board**")
        print(p1,":",score1,"*")
        print(p2,":",score2,"*\n")
        flag+=0.5
print("\n====== ☠️ Game Over ☠️ ======")
print(p1,"Score is: ",score1)
print(p2,"Score is: ",score2)
if score1 > score2:
    print("\nCongratulations🎉👏",p1,"you are the winner!\nWell played🙂",p1)
elif score2 > score1:
    print("\nCongratulations🎉👏",p2,"you are the winner!\nWell played🙂",p2)
else:
    print(f"\nIt's a Tie 🙌☠️️️\n""Well Played",p1,"and",p2)
print("\nDr. B.c. Roy Engineering College(Durgapur)")
print("===Python Mini project===")
print(f"1.TRISHA KARMAKAR-120016254053\n2.RITTIK BANERJEE-2507175\n3.SOURAV DEY-2507177\n4.NISHANT KUMAR-2507178\n5.LUCKY RAJ-2507179\n6.ATUL KUMAR SINHA-2507180")
