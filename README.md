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

## Future Plans / Roadmap

This section outlines the upcoming features and improvements planned for this project. Feel free to contribute, suggest ideas, or work on any of these tasks. Check the boxes as items are completed.

- [ ] **Finding Records by Specific Field Value**: Implement the ability to find records by a specific field value.

- [ ] **Limit and Skip**: Add support for limiting and skipping records for paginated results.

- [ ] **Sorting**: Enable the sorting of records based on specific fields.

- [ ] **Group By**: Implement grouping of records based on a particular field.

### How to Contribute

If you're interested in working on any of the above tasks or have your ideas to add to the roadmap, please follow these steps:

1. Fork the repository.
2. Create a new branch for your work: `git checkout -b feature/your-feature-name`.
3. Implement your changes.
4. Test thoroughly and ensure that the code meets our coding standards.
5. Submit a pull request for review.
