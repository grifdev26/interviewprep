# UserPosts API Server

The following are instructions for deploying and running the UserPosts API server

The UserPosts API Server can be setup and run in the following ways

- From a local development environment
- In a local Docker environment user docker-compose

Details for each setup will be given below


## Running from a local development environment

This section will outline how to run the API server locally in a development environment.

### PostgresSQL Database

The UserPosts API Server utilizes a PostgresSQL Server for its backend storage.

The PostgresSQL Database can be run in a local Docker environment

- Pull the latest PostgresSQL database image
```bash
docker pull postgres
```

- Pull the latest PostgresSQL database image
```bash
docker run --name postgres_local -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword -e POSTGRES_DB=mydatabase -p 5432:5432 -v pgdata:/var/lib/postgresql/data -d postgres
```
- --name postgres_local → Assigns the container a name.
- -e POSTGRES_USER=myuser → Sets the PostgreSQL username.
- -e POSTGRES_PASSWORD=mypassword → Sets the PostgreSQL password.
- -e POSTGRES_DB=mydatabase → Creates a default database.
- -p 5432:5432 → Maps PostgreSQL’s port 5432 to your local machine.
- -v pgdata:/var/lib/postgresql/data → creates a volume named pgdata
- -d postgres → Runs the container in the background.

Once the container has been created it can be stopped and started

To start the container (start the database)
```bash
docker start postgres_local
```

To stop the container (stop the database)
```bash
docker stop postgres_local
```

To remove the container

```bash
docker rm -f postgres_local
```

When stopping and starting the database the data will be persisted in the
volume (pgdata) created when using the docker run command.

If at anypoint you would like to start with fresh data.
You can stop and remove the postgres_local container.
Remove the volume pgdata by running 
```bash
docker volume rm pgdata
```
And then re-run the docker run to recreate the PostgresSQL Server container


### Setup the local environment to run API Server

The following steps assume that you have downloaded the code associated with the API Server

#### 1. Create a Virtual Environment

It's recommended to use a virtual environment to isolate the dependencies for this project. To create a virtual environment, follow these steps:

- Navigate to the project directory:
  ```bash
  cd /path/to/project
  
- Create a virtual environment (you can name it .venv or any name you prefer):
  ```bash
  python3 -m venv .venv
  ```
  This will create a .venv folder containing the isolated Python environment.

#### 2. Activate the Virtual Environment
Once the virtual environment is created, you need to activate it.
- For macOS/Linux:
   ```bash
  source .venv/bin/activate
- For Windows:
   ```bash
  .venv\Scripts\activate
  ```
  After activation, your terminal prompt should show the name of your virtual environment (e.g., (venv)), indicating that it's active.

#### 3. Install the required packages
```bash
pip install -r requirements.txt
```

#### 4. Run migrations to ensure the database is properly configured
From the root directory of the project run the following command
```bash
python manage.py migrate
```

#### 5. Run the Server
From the root directory of the project run the following command
```bash
python manage.py runserver
```

## Running in a local Docker environment
A second option for running the API server allows you 
to create and run both the API server and PostgresSQL in a local 
Docker container using docker-compose

### Startup the API server and Database
From the root directory of the project run the following command 
```bash
docker-compose up --build -d
```
This command will rebuild the API server docker image (if necessary).
And then start both the API server and PostgresSQL database.

The docker-compose configuration is setup to run the migrations to
ensure the database is properly setup.

The database is configured with a data volume to ensure persistence of data
if the database is restarted.

### Shutdown the API server and Database
In order to shutdown both the API Server and PostgresSQL database run the following command
```bash
docker-compose down
```

### Database Persistence
When using docker-compose to run the API Server and PostgresSQL database a volume named lightbox_pgdata
gets created within your Docker container.  This allows the PostgresSQL database to restart without losing data.

If at anypoint you would like to start with fresh data.
You can remove the volume and re-run the docker-compose up command.


## Testing
Unit and integration tests are included with the project

Test can be found in the **tests/** subdirectory from the root of the project

To run all the unit and integration tests run the following command
```bash
python manage.py test
```


