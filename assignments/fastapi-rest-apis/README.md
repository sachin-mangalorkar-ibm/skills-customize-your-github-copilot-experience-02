# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using FastAPI and Python. By completing this assignment, you will practice defining endpoints, validating request data with Pydantic, and returning proper HTTP responses.

## 📝 Tasks

### 🛠️ Create Core API Endpoints

#### Description
Use the starter code to build a simple Book API with in-memory storage.

#### Requirements
Completed program should:

- Add a `GET /` endpoint that returns a short welcome message.
- Add a `GET /books` endpoint that returns all books as a JSON list.
- Add a `GET /books/{book_id}` endpoint that returns one book by id.
- Return a `404` error when a requested `book_id` does not exist.

### 🛠️ Add Data Validation and Create Operation

#### Description
Add an endpoint to create new books and validate incoming request data.

#### Requirements
Completed program should:

- Define a Pydantic model for input with fields for `title`, `author`, and `year`.
- Add a `POST /books` endpoint that accepts JSON input and appends a new book.
- Auto-assign a unique integer `id` for each new book.
- Return the newly created book object as JSON.

### 🛠️ Test the API with Interactive Docs

#### Description
Run the app with Uvicorn and verify all endpoints from FastAPI's built-in docs.

#### Requirements
Completed program should:

- Start successfully with `uvicorn starter-code:app --reload`.
- Make successful test calls from `/docs` for all implemented endpoints.
- Show at least one successful book creation request in `/docs`.
- Keep the application free of runtime errors during manual testing.