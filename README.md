# Customer Order Management System

## Overview

The Customer Order Management System is a backend application developed using Django and PostgreSQL. This system allows users to manage customer orders effectively while providing an integrated SMS notification feature to inform customers about their order status.

## Features

- **Customer Management**: Create and manage customer profiles.
- **Order Management**: Create and track customer orders.
- **SMS Notifications**: Automatically send SMS notifications to customers upon order creation.
- **RESTful API**:  REST API for all operations.

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
5. Run database migrations:
    python manage.py migrate

6. Start the development server:
    python manage.py runserver

