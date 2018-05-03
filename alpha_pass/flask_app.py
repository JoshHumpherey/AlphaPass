from flask import Flask, render_template
import wtforms
import password_gen

app = Flask(__name__)

class PasswordForm(wtforms.Form):
    service_name = wtforms.TextField('Service Name')
    master_key = wtforms.TextField('Master Key')
    submit_button = wtforms.SubmitField(label='Submit Test')
    new_password = wtforms.TextField('New Password')

@app.route("/")
def password_form():
    form = PasswordForm()
    return render_template('index.html',form = form)




if __name__ == "__main__":
    app.run()
