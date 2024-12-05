print("Note: Don't make spelling mistake.")
print ("1. Level Peaceful")
print ("2. Level Medium")
print ("3. Level Hard")

choice = input("choose your level as (1/2/3):")
if choice in ("1", "2", "3"):
    try:
        pass
    except ValueError:
        pass
    

if choice == '1':
    while True:
        question = ("What is the capital of India? ")
        answer = ("New Delhi")
        user_input = input (f"{question}")
        if user_input.strip().lower() == answer.lower():
            print("your answer is correct")
            score1 = int(1)
            print(score1)
        else:
            print("Wrong, answer is New Delhi.")
            score1 = int(0)

        question2= ("What is the color of the sky on a clear day? ")
        answer2 = ("blue")
        user_input = input (f"{question2}")
        if user_input.strip().lower() == answer2.lower():
            print("your answer is correct")
            score2 = int(1)
            print(score2)
        else:
            print("wrong answer is blue.")
            score2 = int(0)

        question3= ("Who is known as the Father of the Nation in India? ")
        answer3 = ("Mahatma Gandhi")
        user_input = input (f"{question3}")
        if user_input.strip().lower() == answer3.lower():
            print("your answer is correct")
            score3 = int(1)
            print(score3)
        else:
            print("wrong answer is Mahatma Gandhi.")
            score3 = int(0)

        question4= ("Which planet is known as the Red Planet? ")
        answer4 = ("Mars")
        user_input = input (f"{question4}")
        if user_input.strip().lower() == answer4.lower():
            print("your answer is correct")
            score4 = int(1)
            print(score4)
        else:
            print("wrong answer is Mars.")
            score4 = int(0)
        print("Total Score:" , score1 + score2 + score3 + score4)
        if (score1 + score2 + score3 + score4 == 4):
            print ("Excellent")
        elif(score1 + score2 + score3 + score4 == 3):
            print("Very good")
        else: 
            print("Too bad")
        break


if choice == "2":
    while True:
        question1 = ("What is the capital of America? ")
        answer1 = ("Washington DC")
        user_input = input (f"{question1}")
        if user_input.strip().lower() == answer1.lower():
            print("your answer is correct")
            score1 = int(1)
            print(score1)
        else:
            print("wrong answer is Washington DC.")
            score1 = int(0)

        question2 = ("Who was the first person to walk on the moon? ")
        answer2 = ("Neil Armstrong")
        user_input = input (f"{question2}")
        if user_input.strip().lower() == answer2.lower():
            print("your answer is correct")
            score2 = int(1)
            print(score2)
        else:
            print("wrong answer is Neil Armstrong.")
            score2 = int(0)

        question3 = ("What is the capital of France? ")
        answer3 = ("paris")
        user_input = input (f"{question3}")
        if user_input.strip().lower() == answer3.lower():
            print("your answer is correct")
            score3 = int(1)
            print(score3)
        else:
            print("wrong answer is paris.")
            score3 = int(0)

        question4 = ("Which element has the chemical symbol O? ")
        answer4 = ("Oxygen")
        user_input = input (f"{question4}")
        if user_input.strip().lower() == answer4.lower():
            print("your answer is correct")
            score4 = int(1)
            print(score4)
        else:
            print("wrong answer is Oxygen.")
            score4 = int(0)
        
        print("Total Score:" , score1 + score2 + score3 + score4)
        if (score1 + score2 + score3 + score4 == 4):
            print ("Excellent")
        elif(score1 + score2 + score3 + score4 == 3):
            print("Very good")
        else: 
            print("Too bad")
        break


if choice == "3":
    while True:
        
        question1 = (" In which year did the Titanic sink? ")
        answer1 = ("1912")
        user_input = input (f"{question1}")
        if user_input.strip().lower() == answer1.lower():
            print("your answer is correct")
            score1 = int(1)
            print(score1)
        else:
            print("wrong answer is 1912.")
            score1 = int(0)

        question2 = ("Who painted the Mona Lisa? ")
        answer2 = ("Leonardo da Vinci")
        user_input = input (f"{question2}")
        if user_input.strip().lower() == answer2.lower():
            print("your answer is correct")
            score2 = int(1)
            print(score2)
        else:
            print("wrong answer is Leonardo da Vinci.")
            score2 = int(0)

        question3 = ("In which continent is Egypt located? ")
        answer3 = ("Africa")
        user_input = input (f"{question3}")
        if user_input.strip().lower() == answer3.lower():
            print("your answer is correct")
            score3 = int(1)
            print(score3)
        else:
            print("wrong answer is Africa.")
            score3 = int(0)

        question4 = ("What is the largest desert in the world? ")
        answer4 = ("Sahara Desert")
        user_input = input (f"{question4}")
        if user_input.strip().lower() == answer4.lower():
            print("your answer is correct")
            score4 = int(1)
            print(score4)
        else:
            print("wrong answer is Sahara Desert.")
            score4 = int(0)

        question5 = (" Which famous scientist developed the theory of relativity? ")
        answer5 = ("Albert Einstein")
        user_input = input (f"{question5}")
        if user_input.strip().lower() == answer5.lower():
            print("your answer is correct")
            score5 = int(1)
            print(score5)
        else:
            print("wrong answer is Albert Einstein.")
            score5 = int(0)
        
        print("Total Score:" , score1 + score2 + score3 + score4 + score5)
        if (score1 + score2 + score3 + score4 + score5 == 5):
            print ("Excellent")
        elif(score1 + score2 + score3 + score4 + score5 == 4):
            print("Very good")
        else: 
            print("Too bad")
        break

