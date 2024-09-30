# Customer Order Management System

## Overview

The Customer Order Management System is a backend application developed using Django and PostgreSQL. This system allows users to manage customer orders effectively while providing an integrated SMS notification feature to inform customers about their order status.

## Features

**Customer Management**: Create and manage customer profiles.
- **Order Management**: Create and track customer orders.
- **SMS Notifications**: Trigger SMS notifications upon order creation using Africa’s Talking API.
- **Authentication**: OpenID Connect  via Django Allauth and Google authentication.
- **RESTful API**: Provides REST API endpoints for all operations.

## Technologies Used

- **Backend**: Django
- **Database**: PostgreSQL
- **SMS Service**: Africa's Talking API
- **Environment Variables**: Managed using `python-dotenv`
- **Version Control**: Git

## Installation

### Prerequisites

- Python 3.x
- PostgreSQL
- Git

### Steps

1. Clone the repository:
   
   git clone https://github.com/sathagesey33/customer_order_project.git
   cd customer_order_project

2. Create a virtual environment
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the dependencies:
    pip install -r requirements.txt

4. Set up the environment variables:
    Create a .env file in the root of your project for your credentials
    `    DATABASES :
        'ENGINE': 'django.db.backends.postgresql',
        'NAME=POSTGRES_DB
        'USER'=POSTGRES_USER
        'PASSWORD='POSTGRES_PASSWORD
        'HOST'=POSTGRES_HOST', localhost
        'PORT'=POSTGRES_PORT, 5432


    client_id=google_client_id
   secret=google_client_secret
    AFRICASTALKING_USERNAME=sandbox
    AFRICASTALKING_API_KEY=your_api_key




5. Run database migrations:
    python manage.py migrate

6. Start the development server:
    python manage.py runserver


## Authentication
This project uses OpenID Connect (OIDC) via Django Allauth, with Google as an external authentication provider.

- **Login with Google**: Redirects users to Google for authentication and then redirects back to the app.

### Known Issues with Authentication
- **Redirection Issue**: After successfully logging in via Google, users are authenticated but are not redirected to the intended customer page. This is an ongoing issue, and a proper redirection mechanism is still in development.


## SMS Notifications (Africa's Talking)
SMS notifications are triggered upon order creation using Africa's Talking API.

### Known Issues with SMS
- The SMS feature was developed and tested in the **sandbox** environment of Africa's Talking. The API is triggered when a new order is created, but SMS messages are not being delivered consistently in the sandbox environment. This issue might be related to limitations of the sandbox mode, and further testing in the production environment might help



## Testing in the Browser
Testing for this project was done using the browser:
1. **Authentication Flow**: 
   - Access the login page via (`/accounts/) to authenticate using Google aas an option.
   - After authentication, the user should be redirected to their profile page, but there is currently a redirection issue.


2. **Order Creation**:
   - Create an order by navigating to the appropriate endpoint in the browser (`/api/orders/`).
   - After an order is created, the system should trigger an SMS notification using Africa’s Talking API.

