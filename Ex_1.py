from flask import Flask, render_template
app = Flask(__name__)


@app.route ('/bmi/<int:w>/<int:h>/')
def bmi(w, h):
    height = h/100
    bmi = int (w/(height*height))
    list = [
        'Severely Underweight',
        'Underweight',
        'Normal',
        'Overweight',
        'Obese'
    ]
    if bmi < 16:
        conditional = list[0]
    
    elif bmi < 18.5:
        conditional = list[1]
    
    elif bmi < 25:
        conditional = list[2]
    
    elif bmi < 30:
        conditional = list[3]
    
    else:
        conditional = list[4]
    
    return render_template('ex1.html', conditional=conditional)

    

if __name__ == '__main__':
  app.run(debug=True)