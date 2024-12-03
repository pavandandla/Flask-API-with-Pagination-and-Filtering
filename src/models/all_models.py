from sqlalchemy import Column, Integer, String, Float, ForeignKey
from config.database import db
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = "users_data"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(50), nullable=False)  # Store hashed passwords

    def user_to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
        }


class Category(db.Model):
    __tablename__ = "categories_data"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True, nullable=False)

    # One-to-many relationship with Product
    products = relationship("Product", back_populates="category", cascade="all, delete-orphan", lazy="joined")

    def category_to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "products": [product.product_to_dict() for product in self.products]
        }


class Product(db.Model):
    __tablename__ = "products_data"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True, nullable=False)
    description = Column(String(100))
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)  # Inventory count
    category_id = Column(Integer, ForeignKey("categories_data.id", ondelete="CASCADE"), nullable=False)

    # Many-to-one relationship with Category
    category = relationship("Category", back_populates="products")

    def product_to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock": self.stock,
            "category_id": self.category_id,
        }
