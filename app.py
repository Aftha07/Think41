from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Order

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:afha333@localhost:5432/ecommerce'
db.init_app(app)

@app.route('/customers')
def list_customers():
    users = User.query.all()
    result = [{'id': u.id, 'name': u.name} for u in users]
    return jsonify(result)

@app.route('/customers/<int:id>')
def get_customer(id):
    user = User.query.get(id)
    if user is None:
        return jsonify({'error': 'Customer not found'}), 404
    order_count = Order.query.filter_by(user_id=id).count()
    return jsonify({'id': user.id, 'name': user.name, 'order_count': order_count})
