# Marketplace

## Project Title
**Marketplace** – A Full-Stack E-commerce Platform built with Django

## Short Description
Marketplace is a Django-based e-commerce web application where users can browse products, filter and search items, add them to the cart, and manage their accounts. Admins can approve products and manage categories, while sellers can track their products and orders. The project utilizes Django’s MVT architecture and includes features like product variations, pagination, and image uploads.

### User Features
- **User Authentication**
  - Register, login, logout
  - Email verification for account activation
  - Password change
  - Profile edit
- **Dashboard**
  - View products posted by the user
  - Track product status (approved, pending, inactive)
- **Products**
  - View all approved products
  - Product detail page with images, stock info, and owner info
  - Search products by name or description
  - Filter products by categories
  - Paginated product listings
- **Cart & Checkout**
  - Add/remove products to cart
  - Handle product variations (size, color)
  - Checkout with tax calculation
  - Place orders
- **Seller Interaction**
  - View seller profiles and products
- **Blog**
  - Read latest blogs
  - View individual blog posts
- **Banners**
  - Display banners on the home page for promotions

### Admin Features
- Manage products, categories, and orders
- Approve or reject user-submitted products
- View user activity and statistics

## Setup Instructions (Local Server with Pipenv)

### Prerequisites
- Python 3.10+
- Pipenv
- Git

### Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/marketplace.git
   cd marketplace
   ```
2. **Activate the Pipenv shell**
   ```bash
   pipenv shell
   ```
   
3. **Install dependencies with Pip**
   ```bash
    pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the development server**
   ```bash
   python manage.py runserver
   ```
7. **Open in browser**
   Access the application at [http://127.0.0.1:8000/]