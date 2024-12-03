from flask import Blueprint
from controllers.user_controller import create_user, get_users, login

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/create-user', methods=['POST'])(create_user)
user_bp.route('/get-users', methods=['GET'])(get_users)
user_bp.route('/login', methods=['POST'])(login)
