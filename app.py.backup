from flask import Flask, render_template, request, redirect, url_for, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Container modification options with prices
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

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')
VENDOR_EMAIL = os.getenv('VENDOR_EMAIL')

def format_order_details(data):
    """Format the order details for email"""
    order_text = f"""
Order Details:
-------------
Customer Information:
Name: {data.get('name')}
Email: {data.get('email')}
Phone: {data.get('phone')}
Shipping Address: {data.get('shipping_address')}

Selected Modifications:
"""
    total = 0
    for category, mods in MODIFICATIONS.items():
        for mod_name, price in mods.items():
            quantity = int(data.get(f"{mod_name.lower().replace(' ', '_')}", 0))
            if quantity > 0:
                subtotal = price * quantity
                total += subtotal
                order_text += f"\n{mod_name} x{quantity}: ${subtotal:,.2f}"
    
    order_text += f"\n\nTotal Amount: ${total:,.2f}"
    
    if data.get('notes'):
        order_text += f"\n\nAdditional Notes:\n{data.get('notes')}"
    
    return order_text

@app.route('/')
def index():
    return render_template('order_form.html', modifications=MODIFICATIONS)

@app.route('/submit-order', methods=['POST'])
def submit_order():
    try:
        data = request.form.to_dict()
        order_text = format_order_details(data)
        
        # Send email to vendor
        vendor_msg = MIMEMultipart()
        vendor_msg['Subject'] = 'New Container Modification Order'
        vendor_msg['From'] = SENDER_EMAIL
        vendor_msg['To'] = VENDOR_EMAIL
        vendor_msg.attach(MIMEText(order_text))
        
        # Send confirmation to customer
        customer_msg = MIMEMultipart()
        customer_msg['Subject'] = 'Your Container Modification Order Confirmation'
        customer_msg['From'] = SENDER_EMAIL
        customer_msg['To'] = data['email']
        
        confirmation_text = f"""
Thank you for your order!

Below are your order details for your records:

{order_text}

We will process your order and contact you if we need any additional information.

Best regards,
Box Hub Team
"""
        customer_msg.attach(MIMEText(confirmation_text))
        
        # Send emails
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(vendor_msg)
            server.send_message(customer_msg)
        
        return jsonify({
            'status': 'success',
            'message': 'Order submitted successfully'
        }), 200
        
    except Exception as e:
        print(f"Error processing order: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': 'Failed to process order'
        }), 500

if __name__ == '__main__':
    app.run(debug=True)