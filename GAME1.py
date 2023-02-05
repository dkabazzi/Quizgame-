from typing import NoReturn


print("Welcome to EasyQuiz Game USA! ")
print("You will have 5 questions to answer.If you get all  answers correct, you win an i-phone 14")
#answer = input("Are you ready?")
#answer = input("Who is the president of the United States of America?")
#rich1 = "Jeff Bizoes" 
#rich2 = "Elon Musk"
total_questions = 5
score = 0
richest_people = ["Elon Musk","Jeff Besoz","Mack Zukaberg","Dominic"] 

while True:
    answer = input("Are you ready?")
    answer = input("Who is the president of the United States of America?")
    if answer == "yes":
        print("Lets begin!")
        if answer == "No":
            print("goodbye!")
    break 
if answer  == "Joe Biden":
    score+=1
    print("correct!")
else:
    score +=0
    print("Wrong answer")
    print("The correct is Joe Biden")

answer=input("When did the United States get its independence?")
if answer =="July 4 1776":
        score+=1
        print("good job")
else:
    score+=0
    print("incorrect!")
    print("The correct answer is July 4 1776")

answer = input("Who freed the Slaves in the United Staes?")
if answer == "Abraham Lincoln":
    score+=1
    print("Correct")
else:
    score+=0
    print("wrong")
    print("The correct answer id Abraham Lincoln")

answer = input("Who is the governor of  Massachusetes?")
if answer == "Charlie Baker":
    score+=1
    print("correct")
else:
    print("Incorrect")
    print("The correct answer is Charlie Baker")  
    score+=0    
answer=input("Name one of the top rich  people  in the United States?")
while True:
    if answer == richest_people[0] or answer == richest_people[1]:
        score+=1
        print("fantastic,high five")
    else:
        score+=0
        print("incorrect")
        print(f"{richest_people[0]},is one of them")
    break       
marks = (score/total_questions)*100
print(f"your score is:{marks}")
if marks == 100:
    print("You have worn a brand new i-phone 14")
else:
    print("thank you for playing, try next time")             
