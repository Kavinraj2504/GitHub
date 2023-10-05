import random
while True:
 print("welcome to play blackjack !")
 cards=[2,3,4,5,6,7,8,9,10,11,10,10]
 def one_card():
    return random.choice(cards)
 a=one_card()
 b=one_card()
 #n=0
 card_list=[a,b]
 print("your cards:" )
 print(card_list)
 #computer_choice=[x]
 x=one_card()
 y=one_card()
 z=one_card()
 computer_choice=[x,y]
 print(f'my card {z}')
 ask_user=str(input("do you want to hit or stand ?(h or s):"))
 if ask_user=="h":
    c=one_card()
    card_list.append(c)
    z=one_card()
    computer_choice.append(z)
    print("after hit:"  )
    print(card_list)
    total_sum_user=sum(card_list)
    print(f"total value of your cards:{total_sum_user}")
    print(" my choice:")
    print(computer_choice)
    total_cc=sum(computer_choice)
    print(f"total value my of choice:{total_cc}")
 else:
    n=random.randint(0,1)
    if n==0:
        computer_choice.append(z)
    print("after stand")
    print(card_list)
    total_sum_user=sum(card_list)
    print(f"total value of your cards: {total_sum_user}")
    print(" my choice:")
    print(computer_choice)
    total_cc=sum(computer_choice)
    print(f"total value of my choice: {total_cc}")
 if total_sum_user==total_cc:
    print("GAME DRAW")
 elif total_cc>21 and total_sum_user<21:
    print("YOU WIN !")
 elif total_sum_user>21 and total_cc<21:
    print("YOU LOSE") 
 elif total_sum_user<21 and total_cc<21:
    if total_sum_user>total_cc:
        print("YOU WIN")
    elif total_sum_user<total_cc:
        print("YOU LOSE") 
 user_input=input("do you want to play again?(y or n):")
 if user_input=="n" :
       break 

