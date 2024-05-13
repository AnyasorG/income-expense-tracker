from flask import Blueprint, request, jsonify
from models import db, Budget, Category

budgets_blueprint = Blueprint('budgets', __name__)

@budgets_blueprint.route('/budgets', methods=['GET'])
def get_budgets():
    budgets = Budget.query.all()
    return jsonify([{'category': budget.category.name, 'amount': budget.amount} for budget in budgets])

@budgets_blueprint.route('/budgets', methods=['POST'])
def set_budget():
    data = request.json
    category_name = data.get('category')
    amount = data.get('amount')
    
    category = Category.query.filter_by(name=category_name).first()
    if category:
        new_budget = Budget(category_id=category.id, amount=amount)
        db.session.add(new_budget)
        db.session.commit()
        return jsonify({'message': 'Budget set successfully', 'category': category.name, 'amount': new_budget.amount}), 201
    else:
        return jsonify({'error': 'Category not found'}), 404
