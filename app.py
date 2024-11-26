from flask import Flask, render_template

app = Flask(__name__)

# Define the kits data
KITS = {
    "Security Kit": {
        "price": 385,
        "description": "Complete security package including locks and safety features"
    },
    "Mobility Kit": {
        "price": 403,
        "description": "Adds mobility features including caster wheels"
    },
    "Window Kit": {
        "price": 507,
        "description": "36x36 inch double pane window installation kit"
    },
    "Door Kit": {
        "price": 845,
        "description": "Standard roll-up door installation package"
    },
    "Ventilation Kit": {
        "price": 150,
        "description": "Basic ventilation package with vents and turbine"
    }
}

@app.route('/')
def index():
    return render_template('order_form.html', kits=KITS)

@app.route('/test')
def test():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)