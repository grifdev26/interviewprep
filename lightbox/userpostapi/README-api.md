# LightBox UserPosts API

The LightBox UserPosts API is designed to manage User and Post


## User
The `User` object represents a person that can create posts

### Attributes

#### `id`
- **Type**: Auto-generated identifier
- **Description**: The `id` attribute is an auto-generated identifier for the user. It represents the primary key for locating a user object.

#### `name` (required)
- **Type**: String
- **Description**: The `name` attribute is a simplified attribute that represents the user's name (e.g., "Joe Smith").

#### `email` (required)
- **Type**: String
- **Description**: The `email` attribute represents the email address associated with the user (e.g., "joe.smith@company.com").

### Endpoints

### `GET /users/`

Retrieves a list of all users.

#### Parameters
- **None**: This endpoint does not require any query parameters.

#### Possible Responses
- **HTTP 200 OK**: The request was successful, and the server returns the list of users.
  
    **Response**: A JSON array containing user objects. Each object represents a user with the following attributes: `id`, `name`, and `email`.

    **Example Response:**
    ```json
    [
        {
          "id": 1,
          "name": "Jill Jackson",
          "email": "jill.jackson@email.com"
        },
        {
          "id": 2,
          "name": "Joe Smith",
          "email": "joe.smith@company.com"
        }
    ]
    ```

#### Notes
- This endpoint returns all users in the system.
- If no users exist, the response will return a `200` status with an empty list of users.


### `POST /users/`

Creates a new user.

#### Request Body

- **Content-Type**: `application/json`
- **Required Fields**: `name`, `email` (both must be non-empty strings)
- **Optional Fields**: Any additional fields as required by the user creation process.

#### Example Request Body
```json
{
    "name": "Bob Johnson",
    "email": "bob.johnson@company.com"
}
```

#### Possible Responses 

- **HTTP 201 CREATED**: The request was successful, and the server returns the list of users.
  
    **Response**: A JSON object representing the newly created user with an auto-generated id.

    **Example Response:**
    ```json
    {
        "id": 3,
        "name": "Bob Johnson",
        "email": "bob.johnson@company.com"
    }
    ```

- **HTTP 400 BAD_REQUEST**: The request body is malformed, or required fields are missing or invalid.
    **Response**: A JSON object with error messages indicating which fields are problematic.

    **Example Response:**
    ```json
    {
        "name": ["This field is required."],
        "email": ["Enter a valid email address."]
    }
    ```


### `GET /users/{user_id}/`
Retrieves the details of a specific user by their `user_id`.

#### Path Parameters
- `user_id` (required): The unique identifier of the user you want to retrieve. It must be a valid integer corresponding to an existing user in the system.

#### Example Request

```http
GET /users/3/
```
#### Possible Responses
- **HTTP 200 OK**: The request was successful, and the server returns specified user object.
  
    **Response**: A JSON object representing the user with the following attributes: `id`, `name`, and `email`.

    **Example Response:**
    ```json
        {
            "id": 3,
            "name": "Bob Johnson",
            "email": "bob.johnson@company.com"
        }
    ```
- **HTTP 404 NOT_FOUND**: No user with the specified `user_id` exists.
    **Response**: A JSON object indicating that the user was not found.

    **Example Response:**
    ```json
    {
         "detail": "User with id=22 not found."
    }
    ```
#### Notes
- The `user_id` must be a valid integer and must exist in the system to return user details.
- If the `user_id` does not exist, a `404 Not Found` response will be returned with a message indicating the user was not found.



### `PUT /users/{user_id}/`
Retrieves the details of a specific user by their `user_id`.

#### Path Parameters
- `user_id` (required): The unique identifier of the user you want to retrieve. It must be a valid integer corresponding to an existing user in the system.

#### Request Body
The request must contain a JSON body with the attributes to be updated. The following fields are required:
- `name`: The new name of the user.
- `email`: The new email of the user.

All fields must be valid and meet the necessary format requirements. If a field is not provided, it will not be updated.

#### Example Request Body
```json
{
    "name": "Joe Smith",
    "email": "joe.smith@company.com"
}
```

#### Example Request

```http
PUT /users/1/
```
#### Possible Responses
- **HTTP 200 OK**: The request was successful, and the server returns specified user object.
  
    **Response**: A JSON object representing the user with the following attributes: `id`, `name`, and `email`.

    **Example Response:**
    ```json
        {
            "id": 3,
            "name": "Bob Johnson",
            "email": "bob.johnson@company.com"
        }
    ```
- **HTTP 400 BAD_REQUEST**: The request body is malformed, or required fields are missing or invalid.
    **Response**:  A JSON object with error messages indicating which fields are problematic.

    **Example Response:**
    ```json
    {
        "name": ["This field is required."],
        "email": ["Enter a valid email address."]
    }
    ```
- **HTTP 404 NOT_FOUND**: No user with the specified `user_id` exists.
    **Response**: A JSON object indicating that the user was not found.

    **Example Response:**
    ```json
    {
         "detail": "User with id=22 not found."
    }
    ```

#### Notes
- The user_id must exist in the system for the update to be applied.
- Only the fields provided in the request body will be updated. Other user attributes will remain unchanged.


### `DELETE /users/{user_id}/`
Deletes a specific user identified by `user_id`.

#### Path Parameters
- `user_id` (required): The unique identifier of the user you want to retrieve. It must be a valid integer corresponding to an existing user in the system.

#### Request Body
- None

#### Example Request

```http
DELETE /users/1/
```
#### Possible Responses
- **HTTP 204 NO_CONTENT**: The user was successfully deleted, and no content is returned.
  
    **Response**: No response body is returned, but the status code indicates success.

- **HTTP 404 NOT_FOUND**: No user with the specified `user_id` exists.
    **Response**: A JSON object indicating that the user was not found.

    **Example Response:**
    ```json
    {
         "detail": "User with id=22 not found."
    }
    ```
#### Notes
- Once a user is deleted, all data related to that user will be permanently removed from the system.
- The user_id must exist in the system for the deletion to occur. If the user_id does not exist, a 404 Not Found response will be returned.
- Deletion is irreversible. Ensure the correct user is being targeted before sending the request.
- Deleting a user will also delete all Posts by the given user.

## Post
The `Post` object contains the information pertinent to a post created by a `User`

### Attributes
#### `id`
- **Type**: Auto-generated identifier
- **Description**: The `id` attribute is an auto-generated identifier for the post. It represents the primary key for locating a post object.

#### `title` (required)
- **Type**: String
- **Description**: The `title` attribute represents the title of post.

#### `content` (required)
- **Type**: String
- **Description**: The `content` attribute contains the details of the post 

#### `user_id` (required)
- **Type**: integer
- **Description**: The `user_id` represents the id of the user that created the post.
And is the foreign key that joins user and the post.


### Endpoints

### `GET /posts/`

Retrieves a list of all posts.

#### Parameters
- **None**: This endpoint does not require any query parameters.

#### Possible Responses

- **HTTP 200 OK**: The request was successful, and the server returns the list of posts.
  
    **Response**: A JSON array containing posts objects. Each object represents a post with the following attributes: `id`, `title`, `content` and `user_id`.

    **Example Response:**
    ```json
    [
    {
        "id": 1,
        "title": "Joe's First Post",
        "content": "This is a some long text that is to represent a post.",
        "user_id": 1
    },
    {
        "id": 2,
        "title": "A second post by Joe",
        "content": "Some additional text for the second post. This is a some long text that is to represent a post.",
        "user_id": 1
    },
    {
        "id": 3,
        "title": "Something Something",
        "content": "A first post is always interesting. This is a some long text that is to represent a post.",
        "user_id": 2
    }
   ]
    ```

#### Notes
- This endpoint returns all posts in the system.
- If no posts exist, the response will return a `200` status with an empty list of posts.


### `POST /posts/`
Creates a new post.

#### Request Body
- **Content-Type**: `application/json`
- **Required Fields**: `title`(must non-empty strings), `content` (must non-empty strings), `user_id` (must match id of created user)

#### Example Request Body
```json
{
    "title": "Another good post",
    "content": "Just one more post without a description. This is a some long text that is to represent a post.",
    "user_id": 2
}
```

#### Possible Responses 

- **HTTP 201 CREATED**: The request was successful, and the server returns the list of posts.
  
    **Response**: A JSON object representing the newly created post with an auto-generated id.

    **Example Response:**
    ```json
    {
        "id": 5,
        "title": "Another good post",
        "content": "Just one more post without a description. This is a some long text that is to represent a post.",
        "user_id": 2
    }
    ```
- **HTTP 400 BAD_REQUEST**: The request body is malformed, or required fields are missing or invalid.
    **Response**:  A JSON object with error messages indicating which fields are problematic.

    **Example Response:**
    ```json
    {
        "title": ["This field may not be blank."],
        "content": ["Tis field is required."]
    }
    ```

### `GET /posts/{post_id}/`
Retrieves the details of a specific post by their `post_id`.

#### Path Parameters
- `post_id` (required): The unique identifier of the post you want to retrieve. It must be a valid integer corresponding to an existing post in the system.

#### Example Request

```http
GET /posts/6/
```
#### Possible Responses
- **HTTP 200 OK**: The request was successful, and the server returns specified post object.
  
    **Response**: A JSON object representing the user with the following attributes: `id`, `title`, `content` and `user_id`.

    **Example Response:**
    ```json
        {
            "id": 6,
            "title": "One more post",
            "content": "This is an interesting post without a description. This is a some long text that is to represent a post.",
            "user_id": 2
        }
    ```
- **HTTP 404 NOT_FOUND**: No user with the specified `post_id` exists.
    **Response**: A JSON object indicating that the post was not found.

    **Example Response:**
    ```json
    {
         "detail": "Post with id=22 not found."
    }
    ```
#### Notes
- The `post_id` must be a valid integer and must exist in the system to return post details.
- If the `post_id` does not exist, a `404 Not Found` response will be returned with a message indicating the user was not found.


### `PUT /posts/{post_id}/`
Retrieves the details of a specific post by their `post_id`.

#### Path Parameters
- `post_id` (required): The unique identifier of the post you want to retrieve. It must be a valid integer corresponding to an existing post in the system.

#### Request Body
The request must contain a JSON body with the attributes to be updated. The following fields are required:
- `title`: The new title of the post.
- `content`: The new content of the post.
- `user_id`: The new user_id of the post.

All fields must be valid and meet the necessary format requirements. If a field is not provided, it will not be updated.

#### Example Request Body
```json
{
    "title": "Another good post",
    "content": "Just one more post without a description. This is a some long text that is to represent a post.",
    "user_id": 4
}
```

#### Example Request

```http
PUT /users/6/
```
#### Possible Responses
- **HTTP 200 OK**: The request was successful, and the server returns specified post object.
  
    **Response**: A JSON object representing the user with the following attributes: `id`, `title`, ,`conent` and `user_id`.

    **Example Response:**
    ```json
        {
            "id": 6,
            "title": "Another good post",
            "content": "Just one more post without a description. This is a some long text that is to represent a post.",
            "user_id": 4
        }
    ```
- **HTTP 400 BAD_REQUEST**: The request body is malformed, or required fields are missing or invalid.
    **Response**:  A JSON object with error messages indicating which fields are problematic.

    **Example Response:**
    ```json
    {
        "title": ["This field may not be blank."],
        "content": ["Tis field is required."]
    }
    ```
- **HTTP 404 NOT_FOUND**: No user with the specified `post_id` exists.
    **Response**: A JSON object indicating that the post was not found.

    **Example Response:**
    ```json
    {
         "detail": "Post with id=22 not found."
    }
    ```

#### Notes
- The post_id must exist in the system for the update to be applied.
- Only the fields provided in the request body will be updated. Other post attributes will remain unchanged.


### `DELETE /posts/{post_id}/`
Deletes a specific user identified by `post_id`.

#### Path Parameters
- `post_id` (required): The unique identifier of the post you want to retrieve. It must be a valid integer corresponding to an existing post in the system.

#### Request Body
- None

#### Example Request

```http
DELETE /posts/7/
```
#### Possible Responses
- **HTTP 204 NO_CONTENT**: The post was successfully deleted, and no content is returned.
  
    **Response**: No response body is returned, but the status code indicates success.

- **HTTP 404 NOT_FOUND**: No post with the specified `post_id` exists.
    **Response**: A JSON object indicating that the post was not found.

    **Example Response:**
    ```json
    {
         "detail": "Post with id=22 not found."
    }
    ```
#### Notes
- Once a post is deleted, all data related to that user will be permanently removed from the system.
- The post_id must exist in the system for the deletion to occur. If the post_id does not exist, a 404 Not Found response will be returned.
- Deletion is irreversible. Ensure the correct user is being targeted before sending the request.


