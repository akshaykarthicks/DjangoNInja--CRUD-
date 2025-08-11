# Django CRUD API with Django Ninja

This is a simple CRUD (Create, Read, Update, Delete) API for managing items, built with Django and Django Ninja.

## Features

*   Create, Read, Update, and Delete operations for items.
*   Authentication required for creating, updating, and deleting items.
*   Pagination for listing items.
*   Validation for item data.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the database migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser to access the admin and for authentication:**

    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

The API will be available at `http://127.0.0.1:8000/api/`.

## API Endpoints

All endpoints are relative to `/api/`.

| Method | Endpoint | Description | Authentication |
| --- | --- | --- | --- |
| POST | `/items` | Create a new item. | Required |
| GET | `/items` | Get a list of all items. | Not Required |
| GET | `/items/{item_id}` | Get a single item by its ID. | Not Required |
| PUT | `/items/{item_id}` | Update an item by its ID. | Required |
| DELETE | `/items/{item_id}` | Delete an item by its ID. | Required |

### Payloads

**Create Item (`POST /items`)**

```json
{
  "name": "string",
  "description": "string",
  "price": "number"
}
```

**Update Item (`PUT /items/{item_id}`)**

```json
{
  "name": "string",
  "description": "string",
  "price": "number"
}
```

## Database Schema

The `Item` model has the following fields:

*   `name`: `CharField` (max_length=50, min_length=3)
*   `description`: `TextField` (optional)
*   `price`: `FloatField`
*   `created_at`: `DateTimeField` (auto-generated)
*   `updated_at`: `DateTimeField` (auto-generated)

## Dependencies

*   [Django](https://www.djangoproject.com/)
*   [Django Ninja](https://django-ninja.rest-framework.com/)
