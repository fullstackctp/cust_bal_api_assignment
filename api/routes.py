from datetime import date, timedelta
from flask import jsonify,request
from api import app
from api.models import *

app.app_context().push() 

@app.route('/customers', methods=['POST'])
def get_customers():
    start_age = int(request.values['start_age'])
    end_age = int(request.values['end_age'])
    age_group = (start_age, end_age)
    today = date.today()
    birth_date_start = today - timedelta(days=age_group[1]*365)
    birth_date_end = today - timedelta(days=age_group[0]*365)
    customers = User.query.filter(
        User.birthday.between(birth_date_start, birth_date_end)
    ).order_by(User.name).all()
    result = [
        {
            'name': customer.name,
            'birthday': customer.birthday.strftime('%Y-%m-%d'),
            'latest_cart_timestamp': customer.ts_cust[-1].dnt.strftime('%Y-%m-%d %H:%M:%S'),
        }
        for customer in customers
    ]
    return jsonify(result)

