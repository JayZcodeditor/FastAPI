# FastAPI Project

![FastAPI](https://fastapi.tiangolo.com/img/logo/logo.svg)

This is a simple FastAPI project that demonstrates the use of FastAPI for building a RESTful API.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn (ASGI server)
- MongoDB (or any other database you want to integrate)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To start the application, use Uvicorn as the ASGI server:

```bash
uvicorn main:app --reload
```

- `main:app` refers to the `app` instance in the `main.py` file.
- The `--reload` flag allows the server to automatically reload when code changes are made.

The application will be accessible at:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc UI**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Endpoints

### GET /tasks

Fetch all tasks from the database.

**Query Parameters:**

- `search` (optional): Search for tasks by title.

**Response:**

- Returns a list of tasks.

### POST /tasks

Create a new task.

**Request Body:**

```json
{
  "title": "Task Title",
  "description": "Task Description",
  "due_date": "2025-12-31T23:59:59"
}
```

**Response:**

- Returns the ID of the created task.

### PUT /tasks/{task_id}

Update an existing task by task ID.

**Request Body:**

```json
{
  "title": "Updated Task Title",
  "description": "Updated Task Description",
  "due_date": "2025-12-31T23:59:59"
}
```

**Response:**

- Returns a success message if the task was updated.

### DELETE /tasks/{task_id}

Delete a task by task ID.

**Response:**

- Returns a success message if the task was deleted.

## Database

This project uses MongoDB for storing tasks. You can configure the database connection in the `database/config.py` file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
