from flask import Flask, render_template

app = Flask(__name__)

# Define the modifications data
MODIFICATIONS = {
    'security': {
        'Bolt-on Lock Boxes': 85,
        'Latch-on Cargo Door Locks': 228,
        'Roll-up Door Lock Box': 72
    },
    'mobility': {
        'Caster Wheels': 403
    },
    'shelter': {
        'Container Shelter for 20ft Container Single Truss': 9490,
        'Container Shelter for 40ft Container Single Truss': 11700
    },
    'windows': {
        'Double Pane Picture Window Kit - 36in x 36in': 507,
        'Double Pane Picture Window With Security Bars Kit - 36in x 36in': 430
    },
    'doors': {
        'Roll-Up Door 6ft x 6ft 8in': 845,
        'Roll-Up Door 7ft x 6ft 8in': 910,
        'Roll-Up Door 8ft x 6ft 8in': 1031,
        'Steel Man Door (Left Hand In-swing)': 618,
        'Steel Man Door (Left Hand Out-swing)': 618,
        'Steel Man Door (Right Hand In-swing)': 618,
        'Steel Man Door (Right Hand Out-swing)': 618
    },
    'ventilation': {
        'Louvered Vent Kit': 46,
        'Wind Turbine Vent Kit': 104
    },
    'shelving': {
        'Hang On Shelf Bracket: 1 Rack': 156,
        'Hang On Shelf Bracket: 2 Racks': 312
    }
}

@app.route('/')
def index():
    return render_template('order_form.html', modifications=MODIFICATIONS)

@app.route('/test')
def test():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)