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


@app.route('/user')
def user():
    return render_template('user.html', users = users )

@app.route('/user/<username>')
def user_name(username):
    return render_template('info.html',users = users, username= username)     
if __name__ == '__main__':
    app.run(debug=True)