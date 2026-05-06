- HTTP Methods
  - GET - Retrieves data (Fetch a file from S3)
  - POST - Send/create data (Create an EC2 instance)
  - PUT - Place a resource at a specific location you define
    (Upload file to S3, Create S3 bucket)
  - DELETE - Delete data (Delete an S3 object)
  - PATCH - Partial update (Update one field in a record)

- HTTP Status Codes:
  - `200` - Everything Ok
  - `201` - Resource was created successfully
  - `301` - URL has changed, redirecting
  - `400` - Request malformed
  - `401` - Not logged in or no credentials
  - `403` - Logged in but no permission
  - `404` - Resource doesn't exist
  - `500` - Server crashed
  - `502` - Load balancer got bad response from server
  - `503` - Server is overloaded or down

- Curl commands:
  - `curl <URL>`
  - `-v` for verbose output that gives full HTTP req res
  - `-o <filename>` for saving the response on a file
  - `--dump-header` for saving the response header
