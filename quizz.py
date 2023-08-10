import tkinter as tk


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("500x500")
    

        ''' a Label widget is created for displaying the question text. The text attribute is initially set to an empty string'''
        self.question_label = tk.Label(root, 
                                       text="",
                                       font = ("Times new roman",15),
                                       fg = 'white',
                                       bg ='black',
                                       relief="groove",
                                       padx=10,
                                       pady=10)
        self.question_label.place(x = 150,y = 150)
        
        '''This loop creates a list of Button widgets for each of the four answer options. The text attribute is initially set to an empty string. 
        The command attribute is assigned a lambda function that captures the current value of i to call the select_option method with the correct argument'''
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root,
                               text="",
                               command=lambda i=i: self.select_option(i),
                               fg = 'red',
                               bg = 'black',
                               relief="ridge",
                               activebackground='white',
                               activeforeground='red',
                               font = ('times new roman',12),
                               padx=10,
                               pady=5)
            self.option_buttons.append(button)
            
        
        self.result_label = tk.Label(root, 
                                     text="",
                                     font = ("Arial",25,"bold"),
                                     fg = 'white',
                                     bg  ='lightgreen')
        self.result_label.place(x = 150, y = 400)
        
        self.new_game()
    '''new game method initializes the game'''
    def new_game(self):
        self.question_num = 0
        self.correct_ans = 0
        self.guesses = []
        self.next_question()
    
    '''The next_question method updates the question and options on the GUI. If there are still questions left, 
    it sets the text of the question label and iterates through each option button to set its text.'''
    def next_question(self):
        if self.question_num < len(question):
            self.question_label.config(text=list(question.keys())[self.question_num])
            options = option[self.question_num]
            for i in range(4):
                self.option_buttons[i].config(text=options[i])
                self.option_buttons[i].place(x = 200,y = 200 + i*50)
            self.result_label.config(text="")
        else:
            self.display_score()
    

    '''The select_option method is called when an option button is clicked. It processes the user's guess, updates the correct answer count,
      and moves on to the next question.'''
    def select_option(self, option_index):
        guess = chr(ord('A') + option_index)
        self.guesses.append(guess)
        correct = check_answer(question[list(question.keys())[self.question_num]], guess)
        self.correct_ans += correct
        self.question_num += 1
        self.next_question()
    
    def display_score(self):
        score = f"Your Score is: {self.correct_ans}/{len(question)}"
        self.result_label.config(text=score, fg="blue")
        
    
def check_answer(ans, guess):
    return ans == guess


question = {
    "1. Which is the capital of India? ": "A",
    "2. Which is National Bird of India? ": "B",
    "3. Which is National Game of India? ": "C",
    "4. Which is National Flower of India? ": "D"
}

option = [
    ["A. Delhi", "B. Gujarath", "C. Maharashtra", "D. Kerala"],
    ["A. Kingfisher", "B. Peacock", "C. Parrot", "D. Machow"],
    ["A. Boxing", "B. Cricket", "C. Hockey", "D. Fencing"],
    ["A. Jasmine", "B. Rose", "C. Lily", "D. Lotus"]
]

root = tk.Tk()
root.config(background="lightblue")
app = QuizApp(root)
root.mainloop()
