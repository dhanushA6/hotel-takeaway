# Hotel Takeaway

This is a simple Flask application designed to serve as a hotel takeaway service. It utilizes the Flask framework to create a web-based platform for ordering food items. Data storage is implemented using Python's `pickle` module.

## Features

- **User-Friendly Interface:** A straightforward design for easy navigation.
- **Product Management:** Browse and view details of available products.
- **Shopping Cart:** Add products, review, and complete orders effortlessly.
- **Admin Dashboard:** Manage menu items, add/remove items, and configure daily menu options.
- **User Order Placement:** Allows users to order from various categories, select quantities, and proceed to checkout.
- **Email Notifications:** Sends billing information to users upon checkout and delivery confirmation after orders are completed.
- **Data Management:** Utilizes `pickle` for storing and retrieving order information securely.

## Getting Started

### Installation

1. Clone the repository

   ```bash
   git clone https://github.com/henry-jacq/hotel-takeaway.git
   cd hotel-takeaway
   ```

2. Create a Virtual Environment

    ```bash
    python -m venv env
    ```

3. Install project dependencies

    ```bash
    pip install -r requirements.txt
    ```

4. Setup the application

    ```bash
    python setup.py
    ```

5. Run the application

    ```bash
    python app.py
    ```
