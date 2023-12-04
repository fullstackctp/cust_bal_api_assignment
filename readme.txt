
----------------------------------------------------------Question-------------------------------------------------------------------------------

DB:
1. Account_customer: Config - UID (Name, email_id, Male, registration_date, Age,
location, birthday, phone_no, primary_address)
2. TS_Customer: Time Series - UID (Cart History),
3. Role_Mapping: user, role
GET API
Use Case: Get all the customer Names with their latest cart history, birthday for a given age
group and location
Filter: age group and location as Request Body/ query param
Use manager role as role-based access control - there is a table of user and role mapping
ORMS and decorators


------------------------------------------------------INFO---------------------------------------------------------------------------------

Flask Customer Management API

Overview
This Flask application serves as a basic API for managing customers and their related information. It includes models for User, TSCustomer, and Role, with corresponding routes for retrieving customer data based on specific criteria.

Setup
Clone the repository:
git clone https://github.com/yourusername/your-repository.git
cd your-repository

Install dependencies:
pip install -r requirements.txt

Configure the database URI in config.py:
SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

Run the application:
python run.py

Routes
GET /customers
Retrieves customers based on the specified age group and provides information such as name, birthday, and the timestamp of their latest cart.

curl http://localhost:5000/customers