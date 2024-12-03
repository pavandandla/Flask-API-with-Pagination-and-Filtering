from models.all_models import Category
from config.database import db

def create_category_service(data):
    existing_category = Category.query.filter_by(name = data['name']).first()
    if existing_category:
        return {"status": "success", "statusCode": 200, "message": "Category already exists"},200
    new_category = Category(name=data['name'])
    db.session.add(new_category)
    db.session.commit()
    
    return {
        "status": "success", 
        "statusCode": 201, 
        "message": "Category created successfully", 
        "data": new_category.category_to_dict()
        },201
    
def get_categories_service(page, per_page):
    categories = Category.query.paginate(page=page, per_page=per_page, error_out=False)
    if not categories.items:
        return {"status": "success", "statusCode": 200, "message": "No categories found"},200
    return {
        "status": "success",
        "statusCode": 200,
        "data": [category.category_to_dict() for category in categories.items]
    },200
