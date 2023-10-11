# Python JSON Server

This is a simple JSON Server implemented in Python using Flask to serve as a fake API. It allows you to create, read, update, and delete resources, with data stored in a JSON file. It's inspired by [Node JSON-Server](https://github.com/typicode/json-server), but implemented in Python.

## Features

- Supports multiple resource endpoints.
- Performs basic CRUD operations (Create, Read, Update, Delete).
- Stores data in a JSON file.
- Easy setup and usage.

## Getting Started

1. Clone this repository or download the source code.

2. Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
3. Create a db.json file with your sample data. Example data structure:
```json
{
  "posts": [
    { "id": 1, "title": "json-server", "author": "typicode" }
  ],
  "comments": [
    { "id": 1, "body": "some comment", "postId": 1 }
  ],
  "profile": { "name": "typicode" }
}
```
4. Run the server:
```bash
python server.py
```
Your server will be running at `http://localhost:<PORT>` where <PORT> is the port specified in your .env file.

5. Access your data using HTTP requests. Example:

    - GET: http://localhost:<PORT>/posts
    - POST: http://localhost:<PORT>/posts (with a JSON payload)
    - PUT: http://localhost:<PORT>/posts/1 (with a JSON payload)
    - PATCH: http://localhost:<PORT>/posts/1 (with a JSON payload)
    - DELETE: http://localhost:<PORT>/posts/1