# __init__ คือ constructor
# self อ้างอิง objectที่จะให้ทำงาน
# text คือ parameter ที่ส่งเข้ามา

# โจทย์ปัญหา 10 ข้อ = class 10 ข้อ


class Question:
    def __init__(self, text, answer):
        # attribute ที่ส่งเข้ามา
        self.text = text
        self.answer = answer
