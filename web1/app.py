from flask import Flask, render_template
app = Flask(__name__)

foods = [
    {
        "title" : "bún riêu",
        "description" : "rất ngon",
        "link" : "https://www.hoidaubepaau.com/wp-content/uploads/2018/08/bun-rieu-cua-dong-mien-bac.jpg",
        "type" : "eat"
    },
    {
        "title" : "bún chả",
        "description" : "rất ngon",
        "link" : "https://beptruong.edu.vn/wp-content/uploads/2018/05/bun-cha.jpg",
        "type" : "eat"
    }, 
    {
        "title" : "phở",
        "description" : "rất ngon",
        "link" : "http://vn.npfamilyrecipes.com/wp-content/uploads/2017/08/ChickenNoodleSoup_PhoGa_thumb.jpg",
        "type" : "eat"
    },
    {
        "title" : "mojito",
        "description" : "rất ngon",
        "link" : "https://www.bbcgoodfood.com/sites/default/files/styles/recipe/public/recipe/recipe-image/2013/11/mojito-cocktails.jpg?itok=7ZS6egg_",
        "type" : "drink"
    },
    {
        "title" : "Trà tranh",
        "description" : "rất ngon",
        "link" : "http://media.bizwebmedia.net/sites/99906/data/Upload/2015/5/cach_pha_tra_chanh_ngon.jpg",
        "type" : "drink"
    },
    {
        "title" : "cà phê nâu",
        "description" : "rất ngon",
        "link" : "https://images.foody.vn/res/g25/249809/prof/s576x330/foody-mobile-hmb-jpg-824-636026213705673815.jpg",
        "type" : "drink"
    }]

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
    return render_template('food.html', foods = foods)

@app.route('/food/<int:index>')
def detail(index):
    food_detail = foods[index]
    return render_template('food_detail.html', food_detail = food_detail)
if __name__ == '__main__':
    app.run(debug=True)
 