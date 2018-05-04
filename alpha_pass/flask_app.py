from flask import Flask, render_template, request, flash, session
import wtforms
from wtforms import Form
import password_gen

app = Flask(__name__)

class GeneratePasswordForm(wtforms.Form):
    service_name = wtforms.TextField('Service Name')
    master_key = wtforms.TextField('Master Key')
    submit_button = wtforms.SubmitField(label='Submit Test')

@app.route("/", methods=['GET', 'POST'])
def password_form_enter_info():
    enter_form = GeneratePasswordForm(request.form)
    if request.method == 'POST':
        service_name = request.form['service_name']
        master_key = request.form['master_key']
        if(master_key == "" or service_name == ""):
            return render_template('index.html',form = enter_form)
        else:
            generated_password = password_gen.generate_password(master_key,service_name)
            flash(generated_password)
            return render_template('index.html',form = enter_form)

    return render_template('index.html',form = enter_form)


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run()
