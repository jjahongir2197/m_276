from flask import Flask, render_template

app = Flask(__name__)

products = [
    {"name": "Phone", "price": 200},
    {"name": "Laptop", "price": 800},
    {"name": "Headphones", "price": 50}
]

@app.route("/")
def shop():
    return render_template("shop.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)
