import tkinter as tk
from tkinter import messagebox

# Sample flashcards as a list of (question, answer) tuples
flashcards = [
    ("What is the capital of France?", "Paris"),
    ("What is 2 + 2?", "4"),
    ("What color do you get by mixing red and white?", "Pink")
]

class FlashcardApp:
    def __init__(self, master):
        self.master = master
        master.title("Flashcard Quiz")

        self.index = 0

        self.question_label = tk.Label(master, text=flashcards[self.index][0], font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(master, font=("Arial", 14))
        self.answer_entry.pack(pady=10)

        self.check_button = tk.Button(master, text="Check Answer", command=self.check_answer)
        self.check_button.pack(pady=10)

        self.next_button = tk.Button(master, text="Next Question", command=self.next_question)
        self.next_button.pack(pady=10)

    def check_answer(self):
        user_answer = self.answer_entry.get().strip()
        correct_answer = flashcards[self.index][1]
        if user_answer.lower() == correct_answer.lower():
            messagebox.showinfo("Correct!", "You got it right!")
        else:
            messagebox.showerror("Oops!", f"Wrong answer. The correct one is: {correct_answer}")

    def next_question(self):
        self.index = (self.index + 1) % len(flashcards)
        self.question_label.config(text=flashcards[self.index][0])
        self.answer_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
