from flask import request, Response , json
from services.category_service import create_category_service,get_categories_service
from middlewares import token_required

def create_category():
    data = request.form
    response, status = create_category_service(data)
    return Response(response=json.dumps(response), status=status, mimetype='application/json')

@token_required
def get_categories():
    data = request.form
    page = int(data.get('page', default=1) )
    per_page = int(data.get('per_page', default=5))
    response, status = get_categories_service(page,per_page)
    return Response(response=json.dumps(response), status=status, mimetype='application/json')

