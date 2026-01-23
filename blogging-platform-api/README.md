# Blogging Platform API

A RESTful API for a personal blogging platform with full CRUD operations, search functionality, and proper validation. Built with FastAPI, SQLAlchemy, and PostgreSQL.

**Project URL:** https://roadmap.sh/projects/blogging-platform-api

## Features

- ✅ Create, read, update, and delete blog posts
- ✅ Search posts by title, content, or category
- ✅ Comprehensive input validation with Pydantic
- ✅ PostgreSQL database with SQLAlchemy ORM
- ✅ UUID-based post identification
- ✅ Automatic timestamp management (created_at, updated_at)
- ✅ Tag system with validation (min 2, max 50 characters)
- ✅ RESTful API design with proper HTTP status codes
- ✅ Interactive API documentation (Swagger UI)
- ✅ Type hints throughout the codebase

## Requirements

- Python 3.10 or higher
- PostgreSQL database (cloud or local)
- Neon account (for cloud PostgreSQL - free tier available)

### Python Dependencies
- fastapi
- uvicorn
- sqlalchemy
- psycopg2-binary
- pydantic-settings
- python-dotenv

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/jurabek-abd/python-backend-fundamentals.git
cd python-backend-fundamentals/blogging-platform-api
```

### 2. Create and activate a virtual environment
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic-settings python-dotenv
```

### 4. Set up PostgreSQL Database (Neon)

1. Sign up at https://neon.tech
2. Create a new project
3. Select **AWS** as cloud provider
4. Choose **Europe (Frankfurt)** region (closest to Central Asia)
5. Copy the connection string from the dashboard

### 5. Create `.env` file

Create a `.env` file in the project root:
```bash
DATABASE_URL=postgresql://username:password@ep-xxxxx.region.aws.neon.tech/dbname?sslmode=require
```

Replace the connection string with your actual Neon database URL.

## Project Structure

```
blogging-platform-api/
├── app/
│   ├── main.py                # Application entry point
│   ├── config.py              # Configuration management
│   ├── dependencies.py        # Dependency injection (DB session)
│   ├── database/
│   │   └── db.py             # Database connection and session
│   ├── models/
│   │   └── post.py           # SQLAlchemy Post model
│   ├── schemas/
│   │   └── post.py           # Pydantic schemas (validation)
│   └── routes/
│       └── posts.py          # API endpoints
├── .env                       # Environment variables (create this)
├── requirements.txt
└── README.md
```

## Usage

### Start the Application

```bash
# Make sure you're in the project directory with activated venv
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

### Interactive API Documentation

FastAPI automatically generates interactive documentation:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## API Endpoints

### Create a Blog Post
```bash
POST /api/v1/posts/
```

**Request Body:**
```json
{
  "title": "My First Blog Post",
  "content": "This is the content of my first blog post.",
  "category": "Technology",
  "tags": ["Tech", "Programming"]
}
```

**Response (201 Created):**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "title": "My First Blog Post",
  "content": "This is the content of my first blog post.",
  "category": "Technology",
  "tags": ["Tech", "Programming"],
  "created_at": "2026-01-23T12:00:00",
  "updated_at": null
}
```

**Example with curl:**
```bash
curl -X POST "http://127.0.0.1:8000/api/v1/posts/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Getting Started with FastAPI",
    "content": "FastAPI is a modern, fast web framework for building APIs with Python.",
    "category": "Tutorial",
    "tags": ["Python", "FastAPI", "API"]
  }'
```

### Get All Posts
```bash
GET /api/v1/posts/
```

**Response (200 OK):**
```json
[
  {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "title": "My First Blog Post",
    "content": "This is the content of my first blog post.",
    "category": "Technology",
    "tags": ["Tech", "Programming"],
    "created_at": "2026-01-23T12:00:00",
    "updated_at": null
  }
]
```

**Example:**
```bash
curl http://127.0.0.1:8000/api/v1/posts/
```

### Search Posts by Term
```bash
GET /api/v1/posts/?term=fastapi
```

Searches across title, content, and category fields (case-insensitive).

**Example:**
```bash
curl "http://127.0.0.1:8000/api/v1/posts/?term=python"
```

**Response (200 OK):**
Returns all posts containing "python" in title, content, or category.

### Get Single Post
```bash
GET /api/v1/posts/{post_id}
```

**Example:**
```bash
curl http://127.0.0.1:8000/api/v1/posts/550e8400-e29b-41d4-a716-446655440000
```

**Response (200 OK):**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "title": "My First Blog Post",
  "content": "This is the content of my first blog post.",
  "category": "Technology",
  "tags": ["Tech", "Programming"],
  "created_at": "2026-01-23T12:00:00",
  "updated_at": null
}
```

### Update a Post (Partial Update)
```bash
PATCH /api/v1/posts/{post_id}
```

**Request Body (all fields optional, but at least one required):**
```json
{
  "title": "My Updated Blog Post",
  "content": "Updated content here."
}
```

**Example:**
```bash
curl -X PATCH "http://127.0.0.1:8000/api/v1/posts/550e8400-e29b-41d4-a716-446655440000" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Updated Title"
  }'
```

**Response (200 OK):**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "title": "Updated Title",
  "content": "This is the content of my first blog post.",
  "category": "Technology",
  "tags": ["Tech", "Programming"],
  "created_at": "2026-01-23T12:00:00",
  "updated_at": "2026-01-23T12:30:00"
}
```

### Delete a Post
```bash
DELETE /api/v1/posts/{post_id}
```

**Example:**
```bash
curl -X DELETE http://127.0.0.1:8000/api/v1/posts/550e8400-e29b-41d4-a716-446655440000
```

**Response (204 No Content):**
No body returned on successful deletion.

## Validation Rules

### Post Title
- Minimum length: 5 characters
- Maximum length: 255 characters
- Required for creation

### Post Content
- Minimum length: 5 characters
- Maximum length: 50,000 characters
- Required for creation

### Category
- Optional field
- Maximum length: 100 characters

### Tags
- Optional field (defaults to empty list)
- Each tag must be a string
- Tag length: minimum 2 characters, maximum 50 characters
- Tags are stored as JSON array

### Search Term
- Maximum length: 100 characters
- Searches are case-insensitive
- Matches partial text in title, content, or category

## Error Handling

The API returns appropriate HTTP status codes and error messages:

| Status Code | Error Type | Description |
|-------------|------------|-------------|
| 200 | Success | Request completed successfully |
| 201 | Created | Post created successfully |
| 204 | No Content | Post deleted successfully |
| 400 | Bad Request | Invalid data provided or validation error |
| 404 | Not Found | Post with given ID not found |
| 422 | Unprocessable Entity | No fields provided for update or validation error |
| 500 | Internal Server Error | Database error or unexpected error |

**Error Response Format:**
```json
{
  "detail": "Post not found"
}
```

**Validation Error Example:**
```json
{
  "detail": [
    {
      "type": "string_too_short",
      "loc": ["body", "title"],
      "msg": "String should have at least 5 characters",
      "input": "Hi",
      "ctx": {
        "min_length": 5
      }
    }
  ]
}
```

## Database Schema

### Posts Table

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | VARCHAR(36) | PRIMARY KEY | UUID v4 identifier |
| title | VARCHAR(255) | NOT NULL | Post title |
| content | TEXT | NOT NULL | Post content |
| category | VARCHAR(100) | NULLABLE | Post category |
| tags | JSON | DEFAULT [] | Array of tags |
| created_at | TIMESTAMP | DEFAULT NOW() | Creation timestamp |
| updated_at | TIMESTAMP | NULLABLE | Last update timestamp |

### Automatic Behaviors
- `id`: Auto-generated UUID v4 on creation
- `created_at`: Auto-set to current timestamp on creation
- `updated_at`: Auto-updated to current timestamp on modification

## Development

### Running in Development Mode
```bash
uvicorn app.main:app --reload
```

The `--reload` flag enables hot-reloading during development.

### Testing with Swagger UI

1. Navigate to http://127.0.0.1:8000/docs
2. Click on any endpoint to expand it
3. Click "Try it out"
4. Fill in the request parameters/body
5. Click "Execute"
6. View the response

### Code Organization

- **main.py**: FastAPI application setup and router registration
- **config.py**: Environment variable management with Pydantic Settings
- **dependencies.py**: Database session dependency for dependency injection
- **database/db.py**: SQLAlchemy engine and session configuration
- **models/post.py**: SQLAlchemy ORM model with validation
- **schemas/post.py**: Pydantic schemas for request/response validation
- **routes/posts.py**: API endpoint handlers with business logic

### Best Practices Implemented

- ✅ Separation of concerns (models, schemas, routes)
- ✅ Dependency injection for database sessions
- ✅ Environment variables for configuration
- ✅ Type hints throughout the codebase
- ✅ Pydantic validation for request/response
- ✅ SQLAlchemy ORM for database operations
- ✅ Proper HTTP status codes
- ✅ RESTful API design
- ✅ UUID for post identification (avoids enumeration attacks)
- ✅ Automatic timestamp management
- ✅ Specific exception handling for database errors

## Common Issues and Solutions

### Database Connection Error
```
sqlalchemy.exc.OperationalError: could not connect to server
```

**Solution:**
- Verify your `DATABASE_URL` in `.env` is correct
- Check that Neon database is running
- Ensure your IP is allowed in Neon dashboard (usually allowed by default)

### Module Not Found Error
```
ModuleNotFoundError: No module named 'psycopg2'
```

**Solution:**
```bash
pip install psycopg2-binary
```

### Schema Mismatch Error
```
psycopg2.errors.StringDataRightTruncation: value too long for type character varying
```

**Solution:**
- Drop and recreate the table in Neon SQL Editor:
```sql
DROP TABLE posts;
```
- Restart the application to recreate tables with correct schema

### Port Already in Use
```
ERROR: [Errno 48] Address already in use
```

**Solution:**
```bash
# Use a different port
uvicorn app.main:app --reload --port 8001
```

## Security Considerations

**Current Implementation:**
- ✅ SQL injection protected (SQLAlchemy ORM parameterizes queries)
- ✅ Input validation (Pydantic schemas)
- ✅ UUID identifiers (prevents enumeration)

## Contributing

This is a learning project built as part of the roadmap.sh backend project series. Suggestions and improvements are welcome!

## License

This project is open source and available for educational purposes.

## Acknowledgments

Built as part of the [roadmap.sh Blogging Platform API project](https://roadmap.sh/projects/blogging-platform-api/solutions?u=692db4d2a17ff74763dc81f1).

- **FastAPI**: https://fastapi.tiangolo.com/
- **SQLAlchemy**: https://www.sqlalchemy.org/
- **PostgreSQL**: https://www.postgresql.org/
- **Neon**: https://neon.tech/

---

**Project URL:** https://roadmap.sh/projects/blogging-platform-api/solutions?u=692db4d2a17ff74763dc81f1
