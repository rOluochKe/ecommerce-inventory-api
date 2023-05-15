# eCommerce Inventory API

Building, testing and documenting an eCommerce inventory RESTful API with DRF (Django Rest Framework).

<p align="center">
  <img src="screenshots/Capture1.PNG" width="800" />
</p>

## Technologies

- Python
- Django
- Django Rest Framework
- Swagger
- PostgreSQL

## Setup

- Clone the project: `git@github.com:rOluochKe/ecommerce-inventory-api.git`
- Change directory into : `cd /eCommerceInventory`
- Create your environment and install dependencies: `pip install -r requirements.txt`
- Run migrations: `python manage.py makemigrations && python manage.py makemigrations product`
- Create super user: `python manage.py createsuperuser`
- Navigation to admin dashboard: `http://localhost:8000/admin` login and create products
- Run tests: `pytest` and test coverage: `pytest --cov`
- View api documentation: `http://localhost:8000/api/schema/docs/#/api`
