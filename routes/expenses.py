from flask import Blueprint, request, jsonify
from models import db, Expense, Category

expenses_blueprint = Blueprint('expenses', __name__)

@expenses_blueprint.route('/expenses', methods=['GET'])
def get_expenses():
    expenses = Expense.query.all()
    return jsonify([{'category': expense.category.name, 'amount': expense.amount, 'description': expense.description} for expense in expenses])

@expenses_blueprint.route('/expenses', methods=['POST'])
def add_expense():
    data = request.json
    category_name = data.get('category')
    amount = data.get('amount')
    description = data.get('description')
    
    category = Category.query.filter_by(name=category_name).first()
    if category:
        new_expense = Expense(category_id=category.id, amount=amount, description=description)
        db.session.add(new_expense)
        db.session.commit()
        return jsonify({'message': 'Expense added successfully', 'category': category.name, 'amount': new_expense.amount, 'description': new_expense.description}), 201
    else:
        return jsonify({'error': 'Category not found'}), 404
