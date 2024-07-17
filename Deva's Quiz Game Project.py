print("Welcome to Devarajan's quiz")

playing = input("Do you want to play the quiz ? ")

if (playing.lower() != "yes" ):
    quit()

print("Great! Lets begin the quiz :)")

score=0
 
#1 question

ans=input("What does IPL stands for ? ")

if (ans.lower()=="indian premier league"):
    print("Bravo! That is the right answer")
    print("Excellent lets move to next question ")
    score=score+1
else:
    print("Sorry, that's a wrong answer ")
    print("Its ok we can do better in the next one ")

#2 question
    
ans=input("What does RAM stand for ?  ")

if (ans.lower()=="random access memory"):
    print("Bravo! That is the right answer")
    score=score+1

else:
    print("That's a wrong answer ")

#3 question

ans=input("What does ROM stand for ?  ")

if (ans.lower()=="read only memory"):
    print("Bravo! That is the right answer")
    print("That is awesome")
    score=score+1

else:
    print("Its a wrong answer ")
    
#4 quesion

ans=input("What does CPU stand for? ")

if (ans.lower()=="central processing unit"):
    print("That is correct answer ")
    score=score+1

else:
    print("That is Incorrect answer ")
    
#5 question

ans=input("What does BBC stand for? ")

if (ans.lower()=="british broadcasting corporation"):
    print("Very well that is a Correct answer ")
    score=score+1

else:
    print("That is a Incorrect answer ")


print("You got", str(score), "Questions correct out of 5 Qestions")

