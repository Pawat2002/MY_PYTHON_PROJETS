print("Welcome to my computer quiz!")

playing = input("Do you want to play? : ")

if playing.lower() != "yes":
    quit()
    

score = 0
question = input("What module must be imported when creating games with Python? : ").lower()
if question == "pygame":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

question = input("What does CPU stand for? : ").lower()
if question == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

question = input("What does GPU stand for? : ").lower()
if question == "graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

question = input("What does RAM stand for? : ").lower()
if question == "random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

question = input("What does AI stand for? : ").lower()
if question == "artificial intelligence":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

question = input("What does HTML stand for? : ").lower()
if question == "hypertext markup language":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

in_percent = score / 6 * 100
print("Your final score is: " + str(score) + "/" + str(6))

print("You got " + str(round(in_percent, 1)) + "%" + " correct!")
    

