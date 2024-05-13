from flask import Blueprint, jsonify, request
from app import db
from models import Category

# Create a blueprint instance
categories_blueprint = Blueprint('categories', __name__)

# Root route
@categories_blueprint.route('/')
def index():
    return 'Welcome to the Income-Expense Tracker!'

# Route to get all categories
@categories_blueprint.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([category.name for category in categories])

# Route to add a new category
@categories_blueprint.route('/categories', methods=['POST'])
def add_category():
    data = request.json
    new_category = Category(name=data['name'])
    db.session.add(new_category)
    db.session.commit()
    return jsonify({'message': 'Category added successfully', 'category': new_category.name}), 201
