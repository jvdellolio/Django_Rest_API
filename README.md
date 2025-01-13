Django REST API - Documentation
Description
This is a project aimed at creating a RESTful API using Django and Django REST Framework. It serves as a backend for managing data in a Django application, providing endpoints for client applications to interact with the data.

Project Setup
1. Clone the Repository
bash
Copiar código
git clone https://github.com/jvdellolio/Django_Rest_API.git
2. Install Dependencies
Make sure you have Python 3.x installed. Create and activate a virtual environment:

bash
Copiar código
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
Then, install the required dependencies:

bash
Copiar código
pip install -r requirements.txt
Running the Project
1. Apply Migrations
Run the following command to apply migrations to your database:

bash
Copiar código
python manage.py migrate
2. Run the Development Server
Start the Django development server:

bash
Copiar código
python manage.py runserver
Once the server is running, you can access the API at:

arduino
Copiar código
http://127.0.0.1:8000/api/
Endpoints
Available API Endpoints
GET /api/: Get a list of all resources.
POST /api/: Create a new resource.
GET /api/{id}/: Retrieve a specific resource by ID.
PUT /api/{id}/: Update a resource by ID.
DELETE /api/{id}/: Delete a resource by ID.
Testing the API
You can test the API using tools like Postman or cURL. For example, to list all resources, you can use the following cURL command:

bash
Copiar código
curl http://127.0.0.1:8000/api/
Contributing
Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them.
Push to your forked repository and create a pull request.
License
This project is open-source and available under the MIT License.
