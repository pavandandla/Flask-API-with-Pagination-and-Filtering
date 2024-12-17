# Flask API with Pagination and Filtering

## Description

This project implements a **Flask REST API** that efficiently handles large datasets by providing **pagination**, **search**, and **filtering** capabilities. The API is designed with scalability, modularity, and ease of integration in mind, making it ideal for managing resources such as **products** or **users**.

## **Features**

- **Secure Authentication and Authorization**  
  Ensures protected access to API endpoints using secure methods.

- **Efficient Database Operations**  
  Leveraging **Flask-SQLAlchemy** with **MySQL/SQLite** for optimized database interactions.

- **Pagination and Filtering**  
  Supports dynamic pagination, search, and filtering based on specific criteria such as category.

- **Environment Configuration**  
  Streamlined configurations for development and production environments.

- **Modular Code Organization**  
  Follows a clean, modular structure for maintainability and scalability.

- **Standardized API Responses**  
  Provides well-structured and standardized responses (JSON format) for all endpoints.

- **Comprehensive Error Handling**  
  Graceful error handling ensures proper communication of errors to API consumers.

## **Libraries Used**

- **Flask**
- **Flask-SQLAlchemy**
- **MySQL/SQLite**

## **Installation and Setup**

### **1. Clone the repository**

```bash
git clone https://github.com/pavandandla/Flask-API-with-Pagination-and-Filtering.git
cd Flask-API-with-Pagination-and-Filtering
```

### **2. Create a virtual environment**

```bash
python -m venv venv
venv\Scripts\activate  # For Windows
```

### **3. Install dependencies**

```bash
pip install uv
uv pip install -r requirements.txt
```

### **4. Set up the database**

- Update your **config.py** file with your database credentials.
- Run the following command to create database tables:

```bash
python src/app.py
```

### **5. Run the application**

```bash
flask run
```

The API will be available at: `http://127.0.0.1:5000`

## **Environment Configuration**

Use the `.env` file to configure environment variables such as:
- **SECRET_KEY**: Secret key for JWT or secure sessions

Example `.env`:

```plaintext
SECRET_KEY=your_secret_key
```

## **Contact**

For questions, suggestions, or issues, contact:

- Email: `dandlapavankumar@gmail.com`
- GitHub: [pavandandla](https://github.com/pavandandla)
