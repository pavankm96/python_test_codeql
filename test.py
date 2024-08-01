from flask import Flask, request, render_template_string
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
csrf = CSRFProtect(app)

class MyForm(FlaskForm):
    data = StringField('Data', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        data = form.data.data
        return f"Data received: {data}"
    return render_template_string('''
        <form method="post">
            {{ form.hidden_tag() }}
            {{ form.data.label }} {{ form.data(size=20) }}
            {{ form.submit() }}
        </form>
    ''', form=form)

if __name__ == '__main__':
    app.run(debug=True)
