from flask import Flask,render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET']) 
def show_form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.form.get('message') #accessing form data with the name 'messgae'
    print(f"Received message: {data}")
    return render_template('message.html')

if __name__ == '__main__':
    app.run(debug=True) # run the Flask app