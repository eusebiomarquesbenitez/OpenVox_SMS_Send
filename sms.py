from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import requests
 
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    num = TextField('Num:', validators=[validators.required()])
    message_text = TextField('Text:', validators=[validators.required()])
    port = TextField('Port:', validators=[validators.required()])
 
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
    print form.errors
    if request.method == 'POST':
        num=request.form['num']
        message_text=request.form['message_text']
        port='gsm-'+request.form['port']
        print num, " ", message_text
 
	params = (
	    ('username', 'user'),
	    ('password', 'password'),
	    ('phonenumber', num),
	    ('message', message_text),
	    ('port', port),
	)

	response = requests.get('http://192.168.1.2:80/sendsms', params=params)
        if form.validate():
            # Save the comment here.
            flash('Res' + num)
        else:
            flash('Error: All the form fields are required. ')
 
    return render_template('hello.html', form=form)
 
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=8080)



