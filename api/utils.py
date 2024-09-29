import africastalking
from django.conf import settings
from dotenv import load_dotenv
import os

load_dotenv()

def send_sms(customer_phone, message):
    # Initialize Africa's Talking with  credentials
    africastalking.initialize(os.getenv('AFRICASTALKING_USERNAME'), os.getenv('AFRICASTALKING_API_KEY'))

    
    # Get the SMS service
    sms = africastalking.SMS

    try:
        # Send the SMS
        response = sms.send(message, [customer_phone])
        return response
    except Exception as e:
        # Handle exceptions
        print(f"Error sending SMS: {e}")
        return None
