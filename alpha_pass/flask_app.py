from flask import Flask, render_template
import password_gen

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/generate_password',methods=['GET'])
def handle_data():
    #master_password = request.form['master_password']
    #service_name = requeswt.form['service_name']
    print(password_gen.generate_password('ABC','DEF'))

if __name__ == "__main__":
    app.run()
