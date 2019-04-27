from flask import Flask, render_template , request , redirect
app = Flask(__name__)

# Study (17/4/19)
@app.route('/')
def index():
   return "Homework"

@app.route('/about-me')
def about_me():
   return render_template('about_me.html')

@app.route('/school')
def school():
   return redirect("http://techkids.vn", code= 302)

# Serious exercise 1 (17/4/19)
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

# Serious exercise 2 (17/4/19)

users = {
	"hoanganh" :         {
			"name" : "Ta Hoang Anh",
			"age" : 22,
            "university" : "WRU"
       },
    "tuananh" : {
			"name" : "Huynh Tuan Anh",
			"age" : 22,
            "university" : "unknown"
       },
    "ngocquynh" : {
        "name" : "Nguyen Ngoc Quynh",
        "age" : 20,
        "university" :"HUST"
    },
    "khanhnam" : {
        "name" : "Nguyen Khanh Nam",
        "age" : 19,
        "university" : "HUST"
    }

}


@app.route('/user')
def user():
   return render_template('user.html', users = users )

@app.route('/user/<username>')
def user_name(username):
   return render_template('info.html',users = users, username= username)

# Serious Excercise 2 (Sat 20/4/2019)
bikes = []
@app.route('/new_bike', methods = ['GET', 'POST'])
def new_bike():
   if request.method == 'GET':
      return render_template('new_bike.html' )
   elif request.method == 'POST':
      form = request.form
      new_bike = {
         "name" : form['name'],
         "price" : form['price'],
         "link" : form['link'],
         "year" : form['year']
      }
      bikes.append(new_bike)
      print(bikes)
      return redirect('/bike_rental_service')
@app.route('/bike_rental_service')
def bike_rental_service():
   return render_template('bike_rental_service.html', bikes = bikes)

# Homework 24/4/2019

# Serious exercise 1 




if __name__ == '__main__':
    app.run(debug=True)