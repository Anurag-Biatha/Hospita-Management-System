from flask import Flask
from flask import flash
from flask import render_template
from flask import redirect
from flask import request
from joblib import load
from matplotlib import pyplot as plt
from pyrsistent import v
import seaborn as sns
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Heart'


def PIE_CHART(valuess, label):
    plt.pie(valuess, labels=label)
    plt.savefig('static/graphs/pie.png')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        age = request.form['age']
        sex = request.form['sex']
        thal = request.form['thall']
        cp = request.form['cp']
        trestbps = request.form['Trestbps']
        chol = request.form['Chol']
        Fbs = request.form['Fbs']
        Restcg = request.form['Restcg']
        Thalach = request.form['Thalach']
        Exang = request.form['Exang']
        Oldpeak = request.form['Oldpeak']
        Slope = request.form['Slope']
        Ca = request.form['Ca']
        value_list = [age, sex, cp, trestbps, chol, Fbs,
                      Restcg, Thalach, Exang, Oldpeak, Slope, Ca, thal]

        # names = ['age', 'sex', 'cp', 'Trestbps', 'Chol', 'Fbs',
        #          'Restcg', 'Thalach', 'Exang', 'Oldpeak', 'Slope', 'Ca', 'thal']
        # PIE_CHART(value_list, names)

        model = load('Data/heart_model')
        pred = model.predict([value_list])
        # val = {'age': value_list[0], 'sex': value_list[1], 'cp': value_list[2], 'tresh': value_list[3],
        #        'chol': value_list[4], 'fbs': value_list[5], 'restg': value_list[6], 'thalcha': value_list[7], 'exang': value_list[8], 'old': value_list[9], 'slope': value_list[10], 'ca': value_list[11], 'thal': value_list[12]}

        # names = ['age', 'sex', 'cp', 'Trestbps', 'Chol', 'Fbs',
        #          'Restcg', 'Thalach', 'Exang', 'Oldpeak', 'Slope', 'Ca', 'thal']

        if pred[0] == 0:
            flash('Positive', 'danger')
            return redirect('/')
        else:
            flash('Negative', 'success')
            return redirect('/')
    return render_template('heart.html')


if __name__ == "__main__":
    app.run(debug=True)
