from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
        <form action="/submit" method="post">
            <input type="text" name="data">
            <input type="submit" value="Submit">
        </form>
    ''')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form['data']
    return f"Data received: {data}"

if __name__ == '__main__':
    app.run(debug=True)
