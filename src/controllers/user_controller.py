from flask import request, Response, json
from services.user_service import create_user_service, get_users_service,login_user_service

def create_user():
    form_data = request.form
    response,status = create_user_service(form_data)
    return Response(response=json.dumps(response), status=status, mimetype='application/json') #mimetype='application/json'

def login():
    data = request.form
    response,status = login_user_service(data)
    return Response(response=json.dumps(response), status=status, mimetype='application/json')


def get_users():
    data = request.form
    page = int(data.get('page', default=1) )
    per_page = int(data.get('per_page', default=5))
    response,status = get_users_service(page,per_page)
    return Response(response=json.dumps(response), status=status, mimetype='application/json')

