from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home(): 
    array = [1, 2, 3, 4, 5]
    return render_template('index.html', text='Hello, Flask!', array=array)

@app.route('/other')
def other():
    sometext='hi'
    return render_template('other.html', sometext=sometext)

@app.template_filter('reverse')
def reverse_string(s):
    return s[::-1]

@app.template_filter('repeat')
def repeat_string(s, times):
    return s * times

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return str(a + b)


@app.route('/handle_url_params')
def handle_url_params():
    if 'greeting' in request.args and 'name' in request.args:
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f'{greeting} {name}!1!11!!1'
    return 'Something or all is not provided.'

if __name__ == '__main__':
    app.run(debug=True)