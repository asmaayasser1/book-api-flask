# Book API with Flask

## Project Overview

Book API is an academic Python backend project that demonstrates foundational API development with Flask. It uses JSON request handling, Flask-SQLAlchemy, and SQLite persistence to perform basic operations on book records.

The repository is a small learning project and currently implements a partial CRUD-style API.

## Implemented Functionality

The current API supports:

- Creating a book
- Retrieving one book by its ID
- Deleting one book by its ID
- Creating the required database tables during application initialization

The API does not currently support:

- Listing all books
- Updating an existing book

## Technology Stack

- Python
- Flask
- Flask-SQLAlchemy
- SQLAlchemy
- SQLite

## Data Model

Each book record contains the following fields:

| Field | Description |
|---|---|
| `id` | Integer primary key generated for each book |
| `book_name` | Name of the book |
| `author` | Name of the author |
| `publisher` | Name of the publisher |

## API Endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| `/books` | `POST` | Create a book from a JSON request |
| `/books/<id>` | `GET` | Retrieve one book by its integer ID |
| `/books/<id>` | `DELETE` | Delete one book by its integer ID |

A collection-list endpoint and update endpoint are not currently implemented.

## Request and Response Examples

The examples below assume the Flask development server is available at `http://127.0.0.1:5000`.

### Create a Book

```bash
curl -X POST http://127.0.0.1:5000/books \
  -H "Content-Type: application/json" \
  -d '{
    "book_name": "Example Book",
    "author": "Example Author",
    "publisher": "Example Publisher"
  }'
```

Example response:

```json
{
  "id": 1
}
```

The request must provide `book_name`, `author`, and `publisher` fields in its JSON body.

### Retrieve a Book

```bash
curl http://127.0.0.1:5000/books/1
```

Example response:

```json
{
  "book_name": "Example Book",
  "author": "Example Author",
  "publisher": "Example Publisher"
}
```

If the requested record does not exist, the current implementation uses Flask’s default not-found response.

### Delete a Book

```bash
curl -X DELETE http://127.0.0.1:5000/books/1
```

Example response when the book is deleted:

```json
{
  "message": "Book deleted"
}
```

Current response when the requested book does not exist:

```json
{
  "error": "not found"
}
```

## Project Structure

```text
.
├── app.py
└── hello_world_test.py
```

- `app.py` contains the Flask application, SQLAlchemy model, database initialization, and API routes.
- `hello_world_test.py` is a simple script that prints `Hello World`. Despite its filename, it is not an automated API test suite.

## Getting Started

### Prerequisites

You will need:

- Python 3
- Flask
- Flask-SQLAlchemy

The repository does not currently include a dependency manifest, so the required packages must be installed manually.

### Clone the Repository

```bash
git clone https://github.com/asmaayasser1/book-api-flask.git
cd book-api-flask
```

### Install Dependencies

Using an isolated Python environment is recommended.

```bash
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
python -m pip install Flask Flask-SQLAlchemy
```

### Run the Application

```bash
python app.py
```

The Flask development server is normally available at:

```text
http://127.0.0.1:5000
```

## Storage

The project uses SQLite through Flask-SQLAlchemy.

The application is configured with the relative database URI `sqlite:///books.db`. During application initialization, `db.create_all()` creates the required database table if it does not already exist.

The project does not currently include a database migration workflow.

## Testing Status

The repository does not currently contain an automated API test suite.

The existing `hello_world_test.py` file is only a simple Hello World script. Source comments mention manual endpoint testing with Postman, but no Postman collection is committed to the repository.

## Security and Scope

This repository is an academic and development project intended to demonstrate foundational Flask API and database concepts. It is not prepared for production deployment.

Additional validation, authentication, authorization, configuration management, and automated testing would be required before production use.

## Current Limitations

- Only partial CRUD-style functionality is implemented
- No endpoint exists for listing all books
- No update endpoint is implemented
- Request data does not have explicit application-level validation
- No automated API tests are included
- No dependency manifest is included
- No database migration workflow is configured
- No production deployment configuration is provided

## Project Status

Academic Flask API project being refined for professional portfolio presentation.
