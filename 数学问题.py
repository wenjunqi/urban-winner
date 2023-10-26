from flask import Flask, render_template, request

app = Flask(__name__)

import re

def answer_math_question(question):
    # 将问题转化为小写字母并去除标点符号
    question = question.lower()
    question = re.sub(r'[^\w\s]', '', question)

    # 检测问题类型并给出答案
    if "加" in question:
        numbers = re.findall(r'\d+', question)
        if len(numbers) == 2:
            result = int(numbers[0]) + int(numbers[1])
            return f"答案是 {result}"
    elif "减" in question:
        numbers = re.findall(r'\d+', question)
        if len(numbers) == 2:
            result = int(numbers[0]) - int(numbers[1])
            return f"答案是 {result}"
    else:
        return "抱歉，我无法回答这个问题。"

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = None
    if request.method == 'POST':
        user_question = request.form['question']
        answer = answer_math_question(user_question)
    return render_template('index.html', answer=answer)

if __name__ == '__main__':
    app.run()
