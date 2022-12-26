#  รันโปรแกรม
from question import Question
from data import question_data
from controller import Controller
from ui import UserInterface

all_question = []


# Question("1+1 = 10 ?", "False")

# กำหนดโจทย์ปัญหา

for item in question_data:
    text = item["text"]
    answer = item["answer"]
    question = Question(text, answer)
    # เอาโจทย์ปัญหาไปยัดลงใน all_question
    all_question.append(question)


# สร้างแผงควบคุม

controller = Controller(all_question)
userInterface = UserInterface(controller)
