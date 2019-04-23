from flask import Flask, render_template
app = Flask(__name__)
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

@app.route('/')
def index():
    return 'Optional'

@app.route('/user/<username>')
def user(username):
    if username in users:
        user = users[username]
        return  render_template('user.html', user = user)
    else :
        return 'User not found'

if __name__ == '__main__':
  app.run(debug=True)
 