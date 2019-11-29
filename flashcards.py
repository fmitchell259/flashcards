
from tkinter import *
from PIL import ImageTk, Image

from data_questions import data_questions, data_answers
from quant_questions import quant_questions, quant_answers


class Flashcards:

    def __init__(self, master):

        path = 'bg.jpg'
        img1 = Image.open(path)
        data_image = ImageTk.PhotoImage(img1)

        self.background_label = Label(master, image=data_image)
        self.background_label.stick_img = data_image
        self.background_label.place(x=-350, y=-70)

        # Means we can loop back to the start when questions are finished.

        self.question_limit = len(data_questions)

        self.subjects = ["Data", "Quant"]

        # This works in conjunction with the question counter.

        self.question_count = 0

        self.question_pack = {"data": (data_questions, data_answers),
                              "quant": (quant_questions, quant_answers)}

        data_pack = self.question_pack['data']
        self.questions = data_pack[0]
        self.answers = data_pack[1]

        self.text = StringVar()
        self.text_box = Label(master, height=10, width=40, textvariable=self.text, fg='white', bg='black', font=("Courier", 21))
        self.text_box.place(x=36, y=75)

        self.master = master

        self.label = Label(master, text=f"Welcome to Frank's {self.subjects[0]} flashcards", fg='white', bg='black', font=("Courier", 16))
        self.label.place(x=130, y=0)

        self.question_number = StringVar()
        self.number_box = Label(master, height=2, width=4, textvariable=self.question_number, fg='white', bg='black', font=("Courier", 21))
        self.number_box.place(x=36, y=30)

        # Initialise both the buttons.

        self.answer_button = Button(master, text="Reveal Answer.", command=self.reveal_answer, fg='black') # command=.....
        self.answer_button.place(x=30, y=350)

        self.change_ques_button = Button(master, text="Change the question.", command=self.change_question, fg='black')  # command=.....
        self.change_ques_button.place(x=400, y=350)

        self.change_options = Button(master, text="Subjects", command=self.change_topics, font=("Courier", 10, 'bold italic'))
        self.change_options.place(x=506, y=55)

        # Start the flashcard application, this function initialises the data cards first.

        self.start_flash_cards()

    def start_flash_cards(self):

        # Start on the data cards.

        self.text.set(self.questions[self.question_count])

        # # Set up the question counter.
        #
        # self.question_number.set(self.question_count + 1)
        # self.text.set(self.questions[self.question_count])

    def reveal_answer(self):

        self.text.set(self.answers[self.question_count])

    def change_question(self):

        # Increment the question counter

        self.question_count += 1

        # If we reach the limit go back to the start.

        if self.question_count == self.question_limit:
            self.question_count = 0

        # Finally update the question and the display number.

        self.question_number.set(self.question_count + 1)
        self.text.set(self.questions[self.question_count])

    def change_to_quant(self):

        path = 'math.jpg'
        img1 = Image.open(path)
        math_image = ImageTk.PhotoImage(img1)
        self.background_label.config(image=math_image)
        self.background_label.stick_img = math_image
        self.background_label.place(x=-100, y=-450)

        self.master.update()
        quant_pack = self.question_pack['quant']
        self.questions = quant_pack[0]
        self.question_limit = len(self.questions)
        self.question_count = 0
        self.text.set(self.questions[self.question_count])
        self.answers = quant_pack[1]
        self.label.config(text=f"Welcome to Frank's {self.subjects[1]} flashcards.")
        self.label.place(x=110, y=0)
        self.master.title("Quant F/Cards")
        self.question_number.set(self.question_count + 1)
        self.text.set(self.questions[self.question_count])


    def change_to_data(self):

        path = 'bg.jpg'
        img3 = Image.open(path)
        data_image = ImageTk.PhotoImage(img3)
        self.background_label.config(image=data_image)
        self.background_label.stick_img = data_image
        self.background_label.place(x=-350, y=-70)


        data_pack = self.question_pack['data']
        self.questions = data_pack[0]
        self.question_limit = len(self.questions)
        self.question_count = 0
        self.text.set(self.questions[self.question_count])
        self.questions = data_pack[0]
        self.answers = data_pack[1]
        self.label.config(text=f"Welcome to Frank's {self.subjects[0]} flashcards.")
        self.label.place(x=130, y=0)
        self.master.title("Data Flashcards")
        self.question_number.set(self.question_count + 1)
        self.text.set(self.questions[self.question_count])

    def change_topics(self):

        top = Toplevel()
        top.minsize(500, 200)
        top.title("Change Subjects.")

        path = 'pillars.jpg'
        img1 = Image.open(path)
        data_image = ImageTk.PhotoImage(img1)

        background_label = Label(top, image=data_image)
        background_label.stick_img = data_image
        background_label.place(x=-350, y=-500)

        message = Label(top, text="Change subjects here.", fg='white', bg='black', font=("Courier", 16))
        message.place(x=150, y=20)

        data_button = Button(top, height=2, width=20, command=self.change_to_data, text="Data Flashcards", fg='grey', bg='black', font=("Courier", 16))
        data_button.place(x=20, y=140)

        quant_button = Button(top, height=2, width=20, command=self.change_to_quant, text="Quant Flashcards", fg='grey', bg='black', font=("Courier", 16))
        quant_button.place(x=280, y=140)


def main():

    root = Tk()
    root.minsize(600, 400)
    game_board = Flashcards(root)
    root.mainloop()

main()
