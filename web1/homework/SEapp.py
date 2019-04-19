from flask import Flask, render_template
app = Flask(__name__)
# Cách 1
# @app.route('/bmi/<int:weight>/<int:height>')
# def bmi(weight, height):
#    height = height /100
#    bmi = weight/(height*height)
#    if bmi < 16 :
#       return 'Your BMI is {} . You are Severely underweight'.format(str(bmi))
#    elif 16 <= bmi < 18.5:
#       return 'Your BMI is {} . You are Underweight'.format(str(bmi))
#    elif 18.5 <= bmi < 25 :
#       return 'Your BMI is {} . You are Normal'.format(str(bmi))
#    elif 25<= bmi < 30 :
#       return 'Your BMI is {} . You are Overweight'.format(str(bmi))   
#    else :
#       return 'Your BMI is {} . You are too fat bro!!'.format(str(bmi))

# Cách 2 
@app.route('/bmi/<int:weight>/<int:height>')
def bmi(weight, height):
    height = height / 100
    bmi = weight/(height*height)
    return render_template('bmi.html', bmi = bmi)
if __name__ == '__main__':
    app.run(debug=True)