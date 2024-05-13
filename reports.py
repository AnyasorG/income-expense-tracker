# routes/reports.py

from flask import Blueprint, jsonify
from app import db  # Import the db instance from your main application file
from models import Expense, Category, Budget
from sqlalchemy import func, extract
from datetime import datetime

reports_blueprint = Blueprint('reports', __name__)

@reports_blueprint.route('/reports/monthly_summary/<int:year>/<int:month>', methods=['GET'])
def monthly_summary(year, month):
    start_date = datetime(year, month, 1)
    end_date = start_date.replace(month=start_date.month % 12 + 1, day=1) if start_date.month < 12 else start_date.replace(year=start_date.year + 1, month=1, day=1)
    
    expenses_by_category = db.session.query(Category.name, func.sum(Expense.amount)).join(Expense).filter(Expense.date >= start_date, Expense.date < end_date).group_by(Category.name).all()
    
    total_expenses = db.session.query(func.sum(Expense.amount)).filter(Expense.date >= start_date, Expense.date < end_date).scalar()
    
    return jsonify({
        'start_date': start_date.strftime('%Y-%m-%d'),
        'end_date': end_date.strftime('%Y-%m-%d'),
        'total_expenses': total_expenses,
        'expenses_by_category': expenses_by_category
    })

@reports_blueprint.route('/reports/expense_breakdown/<int:year>/<int:month>', methods=['GET'])
def expense_breakdown(year, month):
    start_date = datetime(year, month, 1)
    end_date = start_date.replace(month=start_date.month % 12 + 1, day=1) if start_date.month < 12 else start_date.replace(year=start_date.year + 1, month=1, day=1)
    
    expenses = Expense.query.filter(Expense.date >= start_date, Expense.date < end_date).all()
    
    expense_breakdown = {}
    for expense in expenses:
        if expense.category.name not in expense_breakdown:
            expense_breakdown[expense.category.name] = []
        expense_breakdown[expense.category.name].append({
            'description': expense.description,
            'amount': expense.amount,
            'date': expense.date.strftime('%Y-%m-%d')
        })
    
    return jsonify({
        'start_date': start_date.strftime('%Y-%m-%d'),
        'end_date': end_date.strftime('%Y-%m-%d'),
        'expense_breakdown': expense_breakdown
    })
