import random

all_questions = {
    "General Knowledge": {
        "Easy": [
            {"question": "What is the capital of India?", "answer": "New Delhi"},
            {"question": "What does www stand for?", "answer": "World wide web"},
            {"question": "Who wrote 'Romeo and Juliet'?", "answer": "William Shakespeare"}
        ],
        "Medium": [
            {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
            {"question": "What is the currency of Japan?", "answer": "Yen"},
            {"question": "What is the chemical symbol for water?", "answer": "H2O"}
        ],
        "Hard": [
            {"question": "Grand Central Terminal, Park Avenue, New York is the world's", "answer": "largest railway station"},
            {"question": "Garampani sanctuary is located at ", "answer": "Diphu, Assam"},
            {"question": "What is the tallest mammal in the world?", "answer": "Giraffe"}
        ]
    },
    "Sports": {
        "Easy": [
            {"question": "Which sport is played at Wimbledon?", "answer": "Tennis"},
            {"question": "How many players are there in a basketball team?", "answer": "5"},
            {"question": "Which country won the FIFA World Cup in 2018?", "answer": "France"}
        ],
        "Medium": [
            {"question": "Which sport uses a shuttlecock?", "answer": "Badminton"},
            {"question": "Who holds the record for the most Olympic gold medals?", "answer": "Michael Phelps"},
            {"question": "In which year did Usain Bolt set the 100m world record?", "answer": "2009"}
        ],
        "Hard": [
            {"question": "Which country has won the most Rugby World Cups?", "answer": "New Zealand"},
            {"question": "Who is the only boxer to win the heavyweight title 3 times?", "answer": "Muhammad Ali"},
            {"question": "In which sport might you perform a 'salchow'?", "answer": "Figure Skating"}
        ]
    }
}

rewards = {
    10: "Congratulations!... You've earned a 10 points.",
    20: "Congratulations!... You've earned a 20 points.",
    30: "Congratulations!... You've earned a 30 points."
}

def register():
    name = input("Enter your name: ")
    email = input("Enter your email_id")
    print("Welcome,", name, "to the Quiz Game!")

def choose_topic():
    print("Choose a topic:")
    for i, topic in enumerate(all_questions.keys(), 1):
        print(i, "-", topic)
    choice = int(input("Enter the number to choose your choice: "))
    topic = list(all_questions.keys())[choice - 1]
    return topic

def choose_difficulty():
    print("Choose a difficulty level:")
    difficulties = ["Easy", "Medium", "Hard"]
    for i, diff in enumerate(difficulties, 1):
        print(i, "-", diff)
    choice = int(input("Enter the number to your choose choice: "))
    difficulty = difficulties[choice - 1]
    return difficulty

def ask_question(topic, difficulty):
    question = random.choice(all_questions[topic][difficulty])
    print(question["question"])
    answer = input("Your answer: ")
    if answer.lower() == question["answer"].lower():
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        return 0

def play_quiz():
    register()
    topic = choose_topic()
    difficulty = choose_difficulty()
    score = 0
    for _ in range(3):  # Ask 3 questions
        score += ask_question(topic, difficulty)
    print("Your final score is:", score)
    # Check for rewards
    for threshold, reward in rewards.items():
        if score >= threshold:
            print(reward)

play_quiz()
