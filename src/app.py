from config.config import create_app
from config.database import init_db
from routes.user_bp import user_bp
from routes.product_bp import product_bp
from routes.category_bp import category_bp

app = create_app()
init_db(app)

app.register_blueprint(product_bp)
app.register_blueprint(user_bp)
app.register_blueprint(category_bp)

if __name__ == '__main__':
    app.run(debug=True)