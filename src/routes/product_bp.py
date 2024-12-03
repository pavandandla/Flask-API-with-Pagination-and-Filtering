from flask import Blueprint
from controllers.product_controller import create_product, get_products

product_bp = Blueprint('product_bp', __name__)

product_bp.route('/create-products', methods=['POST'])(create_product)
product_bp.route('/get-products', methods=['GET'])(get_products)