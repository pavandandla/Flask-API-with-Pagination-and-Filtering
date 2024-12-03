from flask import request, Response , json
from services.product_service import create_product_service, get_products_service
from middlewares import token_required

def create_product():
    data = request.form
    response , status = create_product_service (data)
    return Response(response=json.dumps(response), status=status, mimetype='application/json')

@token_required
def get_products():
    data = request.form
    page = int(data.get('page', default = 1))
    per_page = int(data.get('per_page', default = 5))
    search = (data.get('search', None))
    if search is not None:
        search = str(search)
    category_id = data.get('category_id', None)
    if category_id is not None:
       category_id = int(category_id)
    min_price = data.get('min_price', 100)  # Default min price is 100
    max_price = data.get('max_price', 1000)  # Default max price is 1000

    # Convert to integers if not None
    min_price = int(min_price) if min_price is not None else 100
    max_price = int(max_price) if max_price is not None else 1000

    # Ensure max_price is greater than min_price
    if max_price < min_price:
        min_price,max_price = max_price,min_price

    response , status = get_products_service (page,per_page,search,category_id,min_price,max_price)
    return Response(response=json.dumps(response), status=status, mimetype='application/json')

