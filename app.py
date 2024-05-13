from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy instance
db = SQLAlchemy()

# Define a function to create the Flask app
def create_app():
    # Create the Flask app instance
    app = Flask(__name__)
    
    # Configure the SQLAlchemy settings
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///income_expense_tracker.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize the SQLAlchemy instance with the app
    db.init_app(app)

    # Import and register blueprints
    from routes import categories, budgets, expenses, reports
    
    app.register_blueprint(categories.categories_blueprint)
    app.register_blueprint(budgets.budgets_blueprint)
    app.register_blueprint(expenses.expenses_blueprint)
    app.register_blueprint(reports.reports_blueprint)

    return app

# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app = create_app()
    
    # Create database tables if they do not exist
    with app.app_context():
        db.create_all()
    
    # Run the Flask app in debug mode
    app.run(debug=True)
