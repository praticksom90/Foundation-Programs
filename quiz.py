import time


quizzes = [
    {
        "title": "General Knowledge",
        "questions": [
            {"question": "What is the capital of France?",
             "options": ["A) London", "B) Berlin", "C) Paris", "D) Rome"],
             "answer": "C"},
            {"question": "Which planet is known as the Red Planet?",
             "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
             "answer": "B"},
            {"question": "Who wrote 'Hamlet'?",
             "options": ["A) Charles Dickens", "B) William Shakespeare", "C) JK Rowling", "D) Tolkien"],
             "answer": "B"},
            {"question": "How many continents are there?",
             "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
             "answer": "C"},
            {"question": "Which is the longest river in the world?",
             "options": ["A) Amazon", "B) Nile", "C) Yangtze", "D) Mississippi"],
             "answer": "B"}
        ]
    },
    {
        "title": "Math Quiz",
        "questions": [
            {"question": "What is 7 + 8?",
             "options": ["A) 14", "B) 15", "C) 16", "D) 17"],
             "answer": "B"},
            {"question": "What is 12 x 12?",
             "options": ["A) 124", "B) 144", "C) 154", "D) 164"],
             "answer": "B"},
            {"question": "What is the square root of 81?",
             "options": ["A) 7", "B) 8", "C) 9", "D) 10"],
             "answer": "C"},
            {"question": "What is 100 ÷ 4?",
             "options": ["A) 20", "B) 25", "C) 30", "D) 40"],
             "answer": "B"},
            {"question": "What is 15% of 200?",
             "options": ["A) 20", "B) 25", "C) 30", "D) 35"],
             "answer": "C"}
        ]
    },
    {
        "title": "Science Quiz",
        "questions": [
            {"question": "What gas do plants breathe in?",
             "options": ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen"],
             "answer": "B"},
            {"question": "Water boils at what temperature (°C)?",
             "options": ["A) 90", "B) 100", "C) 110", "D) 120"],
             "answer": "B"},
            {"question": "Which organ pumps blood?",
             "options": ["A) Brain", "B) Lungs", "C) Heart", "D) Kidney"],
             "answer": "C"},
            {"question": "Which planet is closest to the Sun?",
             "options": ["A) Earth", "B) Venus", "C) Mercury", "D) Mars"],
             "answer": "C"},
            {"question": "What force pulls objects to Earth?",
             "options": ["A) Magnetism", "B) Gravity", "C) Friction", "D) Pressure"],
             "answer": "B"}
        ]
    },
    {
        "title": "History Quiz",
        "questions": [
            {"question": "Who was the first US President?",
             "options": ["A) Lincoln", "B) Jefferson", "C) Washington", "D) Adams"],
             "answer": "C"},
            {"question": "When did World War II end?",
             "options": ["A) 1942", "B) 1945", "C) 1948", "D) 1950"],
             "answer": "B"},
            {"question": "Who discovered America?",
             "options": ["A) Columbus", "B) Cook", "C) Magellan", "D) Vasco"],
             "answer": "A"},
            {"question": "Who built the Taj Mahal?",
             "options": ["A) Akbar", "B) Shah Jahan", "C) Babur", "D) Aurangzeb"],
             "answer": "B"},
            {"question": "Which empire built the Colosseum?",
             "options": ["A) Greek", "B) Roman", "C) Persian", "D) Ottoman"],
             "answer": "B"}
        ]
    },
    {
        "title": "Geography Quiz",
        "questions": [
            {"question": "Largest ocean on Earth?",
             "options": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
             "answer": "D"},
            {"question": "Mount Everest is in which country?",
             "options": ["A) Nepal", "B) India", "C) China", "D) Bhutan"],
             "answer": "A"},
            {"question": "Most populated country?",
             "options": ["A) USA", "B) India", "C) China", "D) Russia"],
             "answer": "B"},
            {"question": "Largest desert?",
             "options": ["A) Sahara", "B) Gobi", "C) Thar", "D) Kalahari"],
             "answer": "A"},
            {"question": "Which continent is Antarctica?",
             "options": ["A) Europe", "B) Asia", "C) Antarctica", "D) Africa"],
             "answer": "C"}
        ]
    },
    {
        "title": "Entertainment Quiz",
        "questions": [
            {"question": "Movie with Jack Sparrow?",
             "options": ["A) Pirates", "B) LOTR", "C) HP", "D) Star Wars"],
             "answer": "A"},
            {"question": "King of Pop?",
             "options": ["A) Elvis", "B) Michael Jackson", "C) Prince", "D) Drake"],
             "answer": "B"},
            {"question": "Dark Knight superhero?",
             "options": ["A) Superman", "B) Batman", "C) Iron Man", "D) Thor"],
             "answer": "B"},
            {"question": "Dinosaur movie?",
             "options": ["A) Avatar", "B) Jurassic Park", "C) Titanic", "D) Inception"],
             "answer": "B"},
            {"question": "Actor who played Iron Man?",
             "options": ["A) Evans", "B) Downey Jr.", "C) Holland", "D) Hemsworth"],
             "answer": "B"}
        ]
    }
]


def run_quiz(quiz):
    print(f"\n🎯 {quiz['title']} STARTED\n")
    score = 0

    for i, q in enumerate(quiz["questions"], 1):
        print(f"Q{i}. {q['question']}")
        for opt in q["options"]:
            print(opt)

        ans = input("Your answer (A/B/C/D): ").upper().strip()

        if ans == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct: {q['answer']}\n")

        time.sleep(0.4)

    print(f"🏆 Score: {score}/{len(quiz['questions'])}")
    print(f"📊 Percentage: {(score/len(quiz['questions']))*100:.2f}%\n")


def main():
    print("🎓 PYTHON QUIZ PLATFORM 🎓")

    while True:
        print("\nChoose a quiz:")
        for i, quiz in enumerate(quizzes, 1):
            print(f"{i}) {quiz['title']}")
        print("0) Exit")

        choice = input("Enter choice: ").strip()

        if choice == "0":
            print("👋 Thanks for playing!")
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(quizzes):
            run_quiz(quizzes[int(choice) - 1])
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
