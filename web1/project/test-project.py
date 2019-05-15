from flask import *
from foods_db import Users,Foods
from bson.objectid import ObjectId
app = Flask(__name__)

app.config['SECRET_KEY'] = '1$^f3DGDFEAK$#%@afkdfe'

@app.route('/home')
def home():
    return render_template('wellcome.html')
@app.route('/region')
def index():
    return render_template('home.html')
@app.route('/asia/food')
def food():
    if 'logged' in session:
        if session['logged']:

            foods = Foods.find() 
            return render_template('test-project.html', foods = foods)
        else:
            return redirect('/login')
    else:
        return redirect('/login')

@app.route('/food/<id>')
def detail(id):
    food_detail = Foods.find_one({"_id": ObjectId(id)})
    return render_template('food_detail.html', food_detail = food_detail)

@app.route('/asia/food/add_food', methods =['GET', 'POST'])
def add_food():
    if request.method == 'GET':
        return render_template('add_food.html')
    elif request.method == 'POST':
        form = request.form
        new_food = {
            "title" : form['title'],
            "description" : form['description'],
            "link" : form['link'],
            "type" : form['type']
        }
        Foods.insert_one(new_food)
        return redirect('/asia/food')

@app.route('/asia/food/edit/<id>', methods = ['GET', 'POST'])
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
        }}
        Foods.update_one(food, new_value)
        return redirect('/asia/food')
@app.route('/asia/food/delete/<id>')
def delete(id):
    food = Foods.find_one({"_id": ObjectId(id)})
    Foods.delete_one(food)
    return redirect('/asia/food')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if 'logged' in session :
        if session['logged']:
            return redirect('/home')
        else:
            if request.method == 'GET':
                return render_template('login.html')
            elif request.method == 'POST':
                form = request.form
                login_username = form['login_username']
                login_password = form['login_password']
                user = Users.find_one({'username': login_username})
                if user is None:
                    session['logged'] = False
                    return redirect('/login')
                else:
                    if login_password == user['password']:
                        session['logged'] = True
                        return redirect('/home')
                    else:
                        session['logged'] = False
                        return redirect('login')
    else:   
        session['logged'] = False
        return render_template('login.html')

@app.route('/logout')
def logout():
    if 'logged' in session:
        session['logged'] = False
    return redirect('/login')
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        form = request.form
        register_username = form['register_username']
        register_password = form['register_password']
        new_user = {
            'username' : register_username,
            'password' : register_password,
        }
        Users.insert_one(new_user)
        return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
 