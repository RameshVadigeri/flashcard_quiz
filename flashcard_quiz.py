import random

def show_menu():
    print("\n--- Flashcard Quiz App ---")
    print("1. Add Flashcard")
    print("2. Take Quiz")
    print("3. Exit")

def load_flashcards():
    try:
        with open("flashcards.txt", "r") as file:
            return [line.strip().split("::") for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_flashcard(question, answer):
    with open("flashcards.txt", "a") as file:
        file.write(f"{question}::{answer}\n")

def take_quiz(flashcards):
    if not flashcards:
        print("No flashcards found. Add some first.")
        return

    random.shuffle(flashcards)
    score = 0

    for q, a in flashcards:
        user_answer = input(f"\nQuestion: {q}\nYour answer: ")
        if user_answer.strip().lower() == a.strip().lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer: {a}")

    print(f"\nQuiz finished! Your score: {score}/{len(flashcards)}")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1–3): ")

        if choice == "1":
            question = input("Enter the question: ")
            answer = input("Enter the answer: ")
            save_flashcard(question, answer)
            print("Flashcard saved.")

        elif choice == "2":
            flashcards = load_flashcards()
            take_quiz(flashcards)

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
