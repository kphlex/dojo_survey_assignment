from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'key1'

# user = {
#         'Name': 'name', 'Age': 'age', 'Dojo Location':'location',
#         'Favorite Language': 'language', 'Comments': 'comment', 'News': 'news'
# }

@app.route('/')
def index():
    session['user'] 
    return render_template('form.html')

@app.route('/process', methods=['POST'])
def user_process():
    session['name'] = request.form['name']
    session['age'] = request.form['age']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comment']
    print(session['user'])
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)