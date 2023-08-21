from flask import  render_template,  jsonify,request
# from flask_sqlalchemy import SQLAlchemy
import requests
from config import app
from model import Payment,db
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:clovertt@localhost/showup'  # Replace with your PostgreSQL database URI
# db = SQLAlchemy(app)

# Define the Payment model


@app.route('/')
def index():
    return render_template('/forms/payment.html')

@app.route('/paystack/initialize', methods=['POST'])
def initialize_payment():
    # Retrieve payment details from the client-side
    amount = request.form['amount']
    email = request.form['email']
    address = request.form['address']
    phone = request.form['phone']
    # country = request.form['country']
    full_name = request.form['full_name']

    # Set up Paystack API endpoint
    paystack_url = 'https://api.paystack.co/transaction/initialize'
    headers = {
        'Authorization': 'Bearer sk_test_5d6c23aa99f0f9db79dcad23b148fc88d5326e31',
        'Content-Type': 'application/json',
    }

    # Prepare data for initializing the payment
    data = {
        'amount': amount,
        'email': email,
        'full_name': full_name,
        'metadata': {
            'phone': phone,
            'address': address
        },
        'channels': ['mobile_money', 'card'],  # Include both mobile money and card channels
        'callback_url': 'https://your-callback-url.com/paystack/callback'
    }

    # Make a POST request to initialize the payment
    response = requests.post(paystack_url, headers=headers, json=data)
    payment_data = response.json()

    # Check if the response contains the 'data' key
    if 'data' in payment_data:
        authorization_url = payment_data['data']['authorization_url']

        # Create a new Payment object and store it in the database
        payment = Payment(amount=amount, email=email, phone=phone, address=address, full_name=full_name)
        db.session.add(payment)
        db.session.commit()

        return jsonify({'authorization_url': authorization_url})
    else:
        return jsonify({'error': 'Payment initialization failed'})

@app.route('/paystack/callback', methods=['POST'])
def payment_callback():
    # Retrieve payment callback data from Paystack
    payment_data = request.get_json()

    # Process the payment data as needed
    # Example: Store user information in your server/database

    # Return a success response to Paystack
    print(payment_data)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)