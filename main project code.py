# Step 1
score = 0

# Step 2-3
geography = {
    "questions": [
        "What is the capital of France?",
        "What is the highest mountain in Africa?",
        "What is the largest desert in the world?",
        "What is the name of the longest river in the world?",
        "What is the name of the smallest country in the world?",
        # more questions here
    ],
    "answers": [
        "Paris",
        "Mount Kilimanjaro",
        "The Sahara Desert",
        "The Nile",
        "Vatican City",
        # more answers here
    ]
}

# Step 4-5
biology = {
    "questions": [
        "What is the scientific name for the common cold?",
        "What is the largest organ in the human body?",
        "What is the smallest bone in the human body?",
        "What is the name of the process that converts glucose into energy?",
        "What is the name of the fluid in the eye that helps maintain its shape?",
        # more questions here
    ],
    "answers": [
        "Rhinovirus",
        "The skin",
        "The stapes bone in the ear",
        "Metabolism",
        "Aqueous humor",
        # more answers here
    ]
}

# Step 6-7
chemistry = {
    "questions": [
        "What is the chemical symbol for gold?",
        "What is the chemical formula for water?",
        "What is the name of the process that converts water into hydrogen and oxygen?",
        "What is the name of the gas that makes up 78% of the Earth's atmosphere?",
        "What is the name of the process that converts carbon dioxide and water into glucose and oxygen?",
        # more questions here
    ],
    "answers": [
        "Au",
        "H2O",
        "Electrolysis",
        "Nitrogen",
        "Photosynthesis",
        # more answers here
    ]
}

# Step 8-9
physics = {
    "questions": [
        "What is the formula for calculating force?",
        "What is the formula for calculating work?",
        "What is the formula for calculating power?",
        "What is the formula for calculating velocity?",
        "What is the formula for calculating acceleration?",
        # more questions here
    ],
    "answers": [
        "F = ma",
        "W = Fd",
        "P = W/t",
        "v = d/t",
        "a = (vf - vi) / t",
        # more answers here
    ]
}

# Step 10-11
computer_science = {
    "questions": [
        "What is the name of the world's first computer?",
        "What is the name of the programming language that was created by Guido van Rossum?",
        "What is the name of the process that converts a program written in a high-level language into machine code?",
        "What is the name of the process that allows a computer to perform multiple tasks simultaneously?",
        "What is the name of the process that allocates memory to different programs?",
        # more questions here
    ],
    "answers": [
    "The Electronic Numerical Integrator and Computer (ENIAC)",
    "Python",
    "Compilation",
    "Multitasking",
    "Memory management",
    # more answers here
]
}
#Step 12
quiz = {
"geography": geography,
"biology": biology,
"chemistry": chemistry,
"physics": physics,
"computer_science": computer_science
}

#Step 13
def ask_question(category):
    import random
    question = random.choice(quiz[category]["questions"])
    answer = input(question + " ")
    correct_answer = quiz[category]["answers"][quiz[category]["questions"].index(question)]
    if answer.lower() == correct_answer.lower():
        print("Correct!")
        global score
        score += 1
    else:
        print("Incorrect. The correct answer is " + correct_answer + ".")

#Step 14
category = input("Which category would you like to be quizzed on? (geography, biology, chemistry, physics, computer_science) ")
ask_question(category)

#Step 15
print("Your current score is " + str(score) + ".")

#Step 16
play_again = input("Would you like to play again? (yes or no) ")
if play_again.lower() == "yes":
    category = input("Which category would you like to be quizzed on? (geography, biology, chemistry, physics, computer_science) ")
    ask_question(category)
    print("Your final score is " + str(score) + ".")
else:
    print("Thank you for playing! Your final score is " + str(score) + ".")
    