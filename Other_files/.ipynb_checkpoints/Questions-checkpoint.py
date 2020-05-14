class FillQuestion:
    qtype = '0'
    def __init__(self, prompt, text, answer):
        self.prompt = prompt
        self.text = text
        self.answer = answer
        
class MultQuestion:
    qtype='1'
    def __init__(self, prompt, answer, right ='Correct!', wrong='Incorrect.'):
        self.prompt = prompt
        self.answer = answer
        self.right = right
        self.wrong = wrong
        
class Solution:
    qtype= '2'
    def __init__(self, answer):
        self.answer = answer

def question(question):
    if question.qtype == '0':
        
        solution = input(question.prompt +"\n" + question.text)
        # If an assertion fails, the message will be displayed
        print(question.answer)
        
    elif question.qtype == '1':
        solution = input(question.prompt)
        if solution ==question.answer:
            print("Correct!")
        else:
            print(question.wrong + "\n\nThe right answer is " +question.answer)
            
    elif question.qtype=='2':
        print(question.answer)