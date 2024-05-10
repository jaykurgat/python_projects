print("Welcome to the exam test!") 
question = input("Do you want to play? ")

if question.lower() == "yes":
    print("Let's do this!" )
else:
    print("Thanks for passing by!")
    quit()
score = 0

quiz = input("What is the first name of the president of Kenya? ")
if quiz.lower() == "william":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")
    
quiz = input("What is the first name of the president of Uganda? ")
if quiz.lower() == "yoweri":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")
    
quiz = input("What is the first name of the president of Rwanda? ")
if quiz.lower() == "paul":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")
    
print("Your points are", score, "out of 4")
print("Your prcentage score is", (score/3)*100,"%.")