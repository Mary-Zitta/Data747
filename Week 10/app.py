from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    header1 = "Hello, World!"
    header2 = "Welcome to My Flask Page"
    paragraph = "This is a simple Flask web page for data 747 coursework"
    return render_template('index.html', header1=header1, header2=header2, paragraph=paragraph)

if __name__ == "__main__":
    app.run(debug=True)
    