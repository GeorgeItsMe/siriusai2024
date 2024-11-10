from flask import Flask, render_template, request
from gigachat import GigaChat

app = Flask(__name__)

# Your GigaChat credentials
CREDENTIALS = 'ZDIxNzE5YTgtNGE3My00Y2RmLTg2MDAtYTg0NDEwZWY0YWFiOmFmMWQxNTBjLTIxMzQtNDAxOC1hM2YwLWJkZWUzYjQ5OWI5Ng=='


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # Get the message from the form
        message = request.form['message']

        # Use GigaChat API to process the message
        with GigaChat(credentials=CREDENTIALS, verify_ssl_certs=False) as giga:
            response = giga.chat(message + ' отредактируй описание которое тебе дали до, повысь читабельность')
            result = response.choices[0].message.content

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
