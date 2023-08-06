import tkinter as tk
import random

quiz_questions = [
    {
        "question": "Who is the current Prime Minister of India as of 2021?",
        "options": ["A) Narendra Modi", "B) Rahul Gandhi", "C) Arvind Kejriwal", "D) Amit Shah"],
        "correct_answer": "A"
    },
    {
        "question": "In which year did the Goods and Services Tax (GST) get implemented in India?",
        "options": ["A) 2012", "B) 2014", "C) 2017", "D) 2019"],
        "correct_answer": "C"
    },
    {
        "question": "Which political party won the majority in the 2019 Indian General Elections?",
        "options": ["A) Indian National Congress (INC)", "B) Bharatiya Janata Party (BJP)", "C) Aam Aadmi Party (AAP)", "D) Trinamool Congress (TMC)"],
        "correct_answer": "B"
    },
    {
        "question": "Which Indian state was reorganized into two separate Union Territories in 2019?",
        "options": ["A) Jammu and Kashmir", "B) Punjab", "C) Haryana", "D) Himachal Pradesh"],
        "correct_answer": "A"
    },
    {
        "question": "In which year did the demonetization of ₹500 and ₹1,000 banknotes take place in India?",
        "options": ["A) 2014", "B) 2015", "C) 2016", "D) 2017"],
        "correct_answer": "C"
    },
    {
        "question": "Who is the current Home Minister of India as of 2021?",
        "options": ["A) Rajnath Singh", "B) Amit Shah", "C) Nitin Gadkari", "D) Nirmala Sitharaman"],
        "correct_answer": "B"
    },
    {
        "question": "When was India's economic liberalization initiated to promote economic growth and development?",
        "options": ["A) 1951", "B) 1980", "C) 1991", "D) 2005"],
        "correct_answer": "C"
    },
    {
        "question": "Which Indian state is known for its remarkable progress in the field of information technology and software services, earning it the nickname 'Silicon Valley of India'?",
        "options": ["A) Maharashtra", "B) Tamil Nadu", "C) Karnataka", "D) Gujarat"],
        "correct_answer": "C"
    },
    {
        "question": "The 'Swachh Bharat Abhiyan' (Clean India Mission) is a nationwide cleanliness campaign launched in India in 2014. What is the primary goal of this campaign?",
        "options": ["A) To promote tourism in India", "B) To eradicate poverty", "C) To provide access to clean drinking water", "D) To make India clean and open defecation-free"],
        "correct_answer": "D"
    },
    {
        "question": "Which major infrastructure project, also known as the 'Golden Quadrilateral,' connects the four major metropolitan cities of Delhi, Mumbai, Chennai, and Kolkata, and aims to improve road connectivity and trade across India?",
        "options": ["A) Yamuna Expressway", "B) North-South Corridor", "C) Eastern Peripheral Expressway", "D) National Highway 44"],
        "correct_answer": "D"
    }
]



class QuizGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Indian Politics and Development Quiz Game")
        self.root.geometry("650x450")
        self.root.configure(bg="orange")  # Set the background color to orange

        self.score = 0
        self.current_question = 0

        self.question_label = tk.Label(self.root, text="", font=("Arial", 16, "bold"), wraplength=600, bg="orange", fg="black")
        self.question_label.pack(pady=20)

        self.option_var = tk.StringVar()
        self.option_var.set("-1")  # Set the default value as string
        self.option_buttons = []
        for i in range(4):
            option_button = tk.Radiobutton(self.root, text="", font=("Arial", 12), bg="orange", fg="black", selectcolor="orange",
                                           variable=self.option_var, value=str(i), command=self.evaluate_answer)  # Set the value as string
            option_button.pack(pady=5, padx=20, anchor="w")
            self.option_buttons.append(option_button)

        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 14, "bold"), bg="orange", fg="black")
        self.feedback_label.pack()

        self.next_button = tk.Button(self.root, text="Next Question", font=("Arial", 14), command=self.load_next_question)
        self.quit_button = tk.Button(self.root, text="Quit", font=("Arial", 14), command=root.quit)
        self.next_button.pack(pady=20)
        self.quit_button.pack(pady=10)

        self.load_next_question()

    def load_next_question(self):
        if self.current_question < len(quiz_questions):
            question_info = quiz_questions[self.current_question]
            self.question_label.config(text=question_info["question"])

            options = question_info["options"]
            for i in range(4):
                self.option_buttons[i].config(text=options[i], state=tk.NORMAL)

            self.option_var.set("")  # Deselect all Radiobuttons
            self.feedback_label.config(text="")
        else:
            self.question_label.config(text="Quiz Completed!", fg="black")
            for button in self.option_buttons:
                button.config(state=tk.DISABLED)
            self.next_button.config(state=tk.DISABLED)
            self.show_result()

    def evaluate_answer(self):
        selected_option_index = self.option_var.get()
        if selected_option_index != "-1":
            question_info = quiz_questions[self.current_question]
            selected_option = chr(ord("A") + int(selected_option_index))

            if selected_option == question_info["correct_answer"]:
                self.score += 1
                self.feedback_label.config(text="Correct!", fg="green")
            else:
                self.feedback_label.config(text="Incorrect. The correct answer was: " + question_info["correct_answer"], fg="red")

            for button in self.option_buttons:
                button.config(state=tk.DISABLED)

            self.current_question += 1
            self.next_button.config(state=tk.NORMAL)

    def show_result(self):
        result = f"You scored {self.score} out of {len(quiz_questions)}"
        self.feedback_label.config(text=result, fg="blue")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGameApp(root)
    root.mainloop()
