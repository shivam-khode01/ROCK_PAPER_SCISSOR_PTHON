import random
from getpass import getpass
user_win=0
computer_win=0
oponent_win=0
stone="🪨"
paper="📄"
scissor="✂️"
game_image=[scissor,paper,stone]
chances=int(input("How many round you want to play (n) : "))
user_input=int(input("Tell your choice\n 1) multiplayer=1 \n 2)computer=2 \n Enter = "))
if user_input==1:
   name=input("Enter 2rd preson's name : ")
for i in range(chances):
      # if user_input==1:
      #     name=input("Enter 2rd preson's name : ")
      if user_input==1:
          user_choice=int(getpass(f"choose one :\n 1){game_image[0]} = 0 \n 2){game_image[1]} = 1 \n 3){game_image[2]}  = 2 \n Enter = "))
          oponent_choice=int(getpass(f"choose one for {name} :\n 1.{game_image[0]}  = 0 \n 2.{game_image[1]} = 1 \n 3.{game_image[2]}  = 2 \n Enter = "))
          print("user choice is = ",game_image[user_choice])
          print("opponent choice is = ",game_image[oponent_choice])
          
          if user_choice==0 and oponent_choice==1:
              user_win=+1
        # print("You win")
          elif user_choice==1 and oponent_choice==1:
            pass
        # user_win +=0 and computer_win+=0
          #print("It's a draw")
          elif user_choice==2 and oponent_choice==1:
           oponent_win+=1
        # print("computer wins")
          elif user_choice==0 and oponent_choice==2:
           oponent_win+=1
        # print("computer wins")
          elif user_choice==1 and oponent_choice==2:
                user_win+=1 
        # print("You wins")
          elif user_choice==2 and oponent_choice==2:
            pass
          # print("It's a draw")
          elif user_choice==0 and oponent_choice==0:
            pass
          # print("It's a draw")
          elif user_choice==1 and oponent_choice==0:
           oponent_win+=1
          #print("Computer wins")
          elif user_choice==2 and oponent_choice==0:
           user_win+=1
        # print("You wins")
          else:
           print("invalid command")
# if user_input==1:
#         print(f"Your score is = {user_win}")
#         print(f"oponent score is = {oponent_win}")
#         if user_win>oponent_win:
#               print(f"CONGRATULATION!!! YOU WON by {name} ")
#         elif oponent_win>user_win:
#               print(f"{name} YOU WON THE GAME")
        # else:
        #  print('DRAW')
      if user_input==2:
              user_choice=int(input(f"choose one :\n 1){game_image[0]}  = 0 \n 2){game_image[1]} = 1 \n 3){game_image[2]}  = 2 \n Enter = "))
              computer_choice=random.randint(0,2)
              print("user choice is = ",game_image[user_choice])
              print("computer choice is = ",game_image[computer_choice])
          # print(game_image[user_choice])
          # print("computer chooses : ",computer_choice)
              if user_choice==0 and computer_choice==1:
                user_win=+1
          # print("You win")
              elif user_choice==1 and computer_choice==1:
               pass
          # user_win +=0 and computer_win+=0
            #print("It's a draw")
              elif user_choice==2 and computer_choice==1:
               computer_win+=1
          # print("computer wins")
              elif user_choice==0 and computer_choice==2:
               computer_win+=1
          # print("computer wins")
              elif user_choice==1 and computer_choice==2:
               user_win+=1 
          # pr int("You wins")
              elif user_choice==2 and computer_choice==2:
               pass
            # print("It's a draw")
              elif user_choice==0 and computer_choice==0:
               pass
            # print("It's a draw")
              elif user_choice==1 and computer_choice==0:
               computer_win+=1
            #print("Computer wins")
              elif user_choice==2 and computer_choice==0:
               user_win+=1
          # print("You wins")
              else:
                print("invalid command")
      # if user_win>computer_win:
      #         print("CONGRATULATION!!! YOU WON ")
      # else:
      #         print("SORRY!! YOU LOST BY COMPUTER  ")
      # for i in range(chances):
      # else:
      #     print("invalid command")
if user_input==2:
        print("Your score is = ",user_win)
        print("coputer score is =  ",computer_win)

        if user_win>computer_win:
                print("CONGRATULATION!!! YOU WON ")
        else:
                print("SORRY!! YOU LOST BY COMPUTER  ")
if user_input==1:
        print(f"Your score is = {user_win}")
        print(f"oponent score is = {oponent_win}")
        if user_win>oponent_win:
              print(f"CONGRATULATION!!! YOU WON by {name} ")
        elif oponent_win>user_win:
              print(f"{name} YOU WON THE GAME")
        else:
             print('DRAW')
