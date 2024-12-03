from flask import Blueprint
from controllers.category_controller import create_category, get_categories

category_bp = Blueprint('category_bp', __name__)

category_bp.route('/create-categories', methods=['POST'])(create_category)
category_bp.route('/get-categories', methods=['GET'])(get_categories)