from flask import Flask, render_template , request , redirect
from foods_db import Foods
from bson.objectid import ObjectId
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello C4E29"

@app.route('/say-hi')
def say_hi():
    return "Hi everyone!!"

@app.route('/say-hi/<name>')
def say_hi_anyone(name):
    return "Xin chao {}".format(name)

@app.route('/add/<int:x>/<int:y>')
def add(x, y):
    tong = x + y
    return str(tong)

@app.route('/food')
def food():
    foods = Foods.find() 
    return render_template('food.html', foods = foods)

@app.route('/food/<id>')
def detail(id):
    food_detail = Foods.find_one({"_id": ObjectId(id)})
    return render_template('food_detail.html', food_detail = food_detail)

@app.route('/food/add_food', methods =['GET', 'POST'])
def add_food():
    if request.method == 'GET':
        return render_template('add_food.html')
    elif request.method == 'POST':
        form = request.form
        new_food = {
            "title" : form['title'],
            "description" : form['description'],
            "link" : form['link'],
            "type" : form['type'],
        }
        Foods.insert_one(new_food)
        return redirect('/food')

@app.route('/food/edit/<id>', methods = ['GET', 'POST'])
def edit_food(id):
    food = Foods.find_one({"_id": ObjectId(id)})
    if request.method == 'GET':
        return render_template('edit_food.html', food = food)
    elif request.method == 'POST':
        form = request.form
        new_value = { "$set":
        {
            "title" : form['title'],
            "description" : form['description'],
            "link" : form['link'],
            "type" : form['type']
        }}
        Foods.update_one(food, new_value)
        return redirect('/food')
@app.route('/food/delete/<id>')
def delete(id):
    food = Foods.find_one({"_id": ObjectId(id)})
    Foods.delete_one(food)
    return redirect('/food')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        form = request.form
        return "Login page"
        if  form['username'] == "c4e" and form['password'] == "c4e":
            return "Wellcome"
        else:
            return "Forbiden"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form = request.form
        return 'Register page'

if __name__ == '__main__':
    app.run(debug=True)
 