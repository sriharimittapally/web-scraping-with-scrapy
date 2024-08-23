

# Nobero Product Scraper and API

This project is a web application that scrapes product data from the Nobero website, stores it in a Django-based backend, and displays it using a React frontend. The project consists of three main components:

# *1. Django Backend*

- *Overview*: The backend is built using Django, a powerful Python web framework. It serves as the core of the application, providing a RESTful API that allows the frontend to interact with the scraped product data.
- *Django REST Framework (DRF)*: The API is developed using Django REST Framework, which simplifies the creation of RESTful APIs in Django. DRF provides features like serializers, viewsets, and routers, making it easy to build and manage the API endpoints.
- *Database*: The backend uses a relational database (SQLite for development) to store the product data. Each product scraped from the Nobero website is saved in the database with fields such as name, price, description, image URL, and more.
- *Admin Interface*: Django’s built-in admin interface is used to manage the product data. Administrators can view, add, update, and delete products directly through this interface.

# *2. Scrapy Spider*

- *Overview*: The Scrapy spider is a Python-based web crawler specifically designed to scrape product data from the Nobero website. Scrapy is a versatile and efficient web scraping framework that makes it easy to extract data from websites.
- *Data Extraction*: The spider navigates through the product listings on the Nobero website, extracting relevant information such as product names, prices, descriptions, images, and other details. The extracted data is then processed and stored directly in the Django backend database.
- *Scheduling*: The spider can be scheduled to run at specific intervals, ensuring that the product data remains up-to-date. This can be done using a task scheduler like Celery in Django or a cron job on the server.
- *Integration*: The spider is tightly integrated with the Django backend. Once the spider scrapes the data, it uses Django’s ORM to save the products in the database, making them instantly available through the API.

# *3. React Frontend*

- *Overview*: The frontend of the application is built using React, a popular JavaScript library for building user interfaces. React enables the creation of a dynamic and responsive user experience.
- *Product Listing*: The frontend fetches data from the Django REST API and displays a list of products. Each product in the list shows a summary view, including the product name, price, and a thumbnail image.
- *Product Details*: Clicking on a product from the list navigates to a detailed view page. This page provides more comprehensive information about the product, such as a larger image, detailed description, and other relevant details.
- *User Experience*: The React app is designed to be fast and responsive, providing a smooth user experience. React Router is used to handle navigation between different pages (e.g., product list, product details).
- *State Management*: State in the React app is managed using React’s built-in state management tools, ensuring that the UI updates efficiently in response to user actions and data changes.
