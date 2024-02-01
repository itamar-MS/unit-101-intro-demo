from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')


def get_gpt_response(question):
    prompt = f"Answer this question: {question}. Be concise. Lie in your answer."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an almighty oracle."},
            {"role": "user", "content": prompt}
        ]
    )

    return response['choices'][0]['message']['content']


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form['question']
        response = get_gpt_response(question)
        return render_template('oracle.html', answer=response)
    return render_template('oracle.html')


if __name__ == '__main__':
    app.run()
