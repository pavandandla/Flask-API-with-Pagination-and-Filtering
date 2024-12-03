from models.all_models import Product
from config.database import db

def create_product_service(data):
    new_product = Product(
        name=data['name'],
        description=data['description'],
        price=data['price'],
        stock=data['stock'],
        category_id=data['category_id']
    )
    db.session.add(new_product)
    db.session.commit()
    return {"status": "success", "statusCode": 201, "message": "Product created successfully", "data": new_product.product_to_dict()},201

def get_products_service(page, per_page, search, category_id,min_price,max_price):
    query = Product.query
    if search:
        query = query.filter(Product.name.ilike(f'%{search}%'))
    if category_id:
        query = query.filter(Product.category_id == category_id)

    if min_price is not None and max_price is not None:
        query = query.filter(Product.price >= min_price, Product.price <= max_price)  # Filter products with price range

    query = query.order_by(Product.price)
    products = query.paginate(page=page, per_page=per_page, error_out=False).items
    if not products:
        return {"status": "success", "statusCode": 200, "message": "No products found"}
    
    return {
        "status": "success",
        "statusCode": 200,
        "message": "Products found are",
        "data": [product.product_to_dict() for product in products]
    },200

