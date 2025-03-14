from flask import Flask, render_template, redirect, url_for, request, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'tajny_klic'  # Tajný klíč pro session

# Globální proměnná pro ukládání zpráv
zpravy = []

@app.route('/')
def index():
    jmeno = session.get('jmeno', '')
    text = session.get('text', '')
    return render_template('chat.html', zpravy=zpravy, jmeno=jmeno, text=text)

@app.route('/odeslat', methods=['POST'])
def odeslat():
    jmeno = request.form.get('jmeno')
    text = request.form.get('text')

    session['jmeno'] = jmeno
    session['text'] = text

    if jmeno and text:
        zpravy.append({'jmeno': jmeno, 'text': text, 'cas': datetime.now().strftime("%H:%M:%S")})
        session['text'] = ''

    return redirect(url_for('index'))

@app.route('/edit', methods=['POST'])
def edit_message():
    index = int(request.form.get('index', -1))
    field = request.form.get('field')
    new_value = request.form.get('new_value')

    if 0 <= index < len(zpravy):
        if field == 'jmeno':
            zpravy[index]['jmeno'] = new_value
        elif field == 'text':
            zpravy[index]['text'] = new_value
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    global zpravy
    zpravy = []
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=8080)
