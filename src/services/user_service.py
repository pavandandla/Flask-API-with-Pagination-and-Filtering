from models.all_models import User
from config.database import db
import jwt
import os

def create_user_service(form_data):
    existing_user = User.query.filter_by(username=form_data["username"]).first()
    if existing_user:
        return {"status": "success", "statusCode": 200, "message": "User already exists"}, 200  # Return tuple (response, status)
    
    new_user = User(
        username=form_data['username'],
        email=form_data['email'],
        password=form_data['password']
    )
    db.session.add(new_user)
    db.session.commit()

    return {
        "status": "success", 
        "statusCode": 201, 
        "message": "User created successfully", 
        "data": new_user.user_to_dict()
    },201  

def login_user_service(data):
    try:
        if "email" in data and "password" in data:
            user = User.query.filter_by(email=data["email"]).first()
            if user and  (user.password==data["password"]):
                # Include role and username in the token
                token_Data = {
                    'username': user.username,
                    'id': user.id
                }
                token = jwt.encode(token_Data, str(os.getenv('SECRET_KEY')) , algorithm='HS256')
               
                return {'message':f"Login Successful.Welcome,{user.username}!", 'status': "success", "statusCode": 200, "token": token}, 200
            else:
                return {'status': "success", "statusCode": 200, "message": "Invalid credentials!"}, 200
        else:
            return {'status': "failed", "statusCode": 400, "message": "Email and password are required"}, 400
    except Exception as e:
        return {'status': "failed", "statusCode": 500, "message": "Error occurred", "error": str(e)}, 500



def get_users_service(page, per_page):
    users = User.query.paginate(page=page, per_page=per_page, error_out=False).items
    if not users:
        return {"status": "success", "statusCode": 200, "message": "No users found"}
    
    return {
        "status": "success",
        "statusCode": 200,
        "message": "Users found are",
        "data": [user.user_to_dict() for user in users]
    },200