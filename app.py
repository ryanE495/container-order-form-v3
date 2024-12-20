from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Import the product catalog
from products import PRODUCT_CATALOG

@app.route('/')
def index():
    return render_template('order_form.html', catalog=PRODUCT_CATALOG)

@app.route('/generate-quote', methods=['POST'])
def generate_quote():
    data = request.json
    
    # Save order to JSON file
    order_id = save_order(data)
    
    return jsonify({
        'success': True,
        'order_id': order_id
    })

def save_order(order_data):
    timestamp = datetime.now().isoformat()
    order_id = f"ORD-{timestamp.replace(':', '').replace('.', '')}"
    
    order_record = {
        'order_id': order_id,
        'timestamp': timestamp,
        'data': order_data
    }
    
    # Save to JSON file
    try:
        with open('orders.json', 'r') as f:
            orders = json.load(f)
    except FileNotFoundError:
        orders = []
    
    orders.append(order_record)
    
    with open('orders.json', 'w') as f:
        json.dump(orders, f, indent=2)
    
    return order_id

if __name__ == '__main__':
    app.run(debug=True)