# PokemonDB
Stores name, type and image URL of Pokemons from PokeAPI and displas it to the user.

- [Requirements](#requirements)
- [Project Setup](#project-setup)
- [Usage](#usage)
  
## Requirements
1. Python
2. Pip
3. Git
4. PostgresSQL

## Project Setup
1. Clone the repo from github
2. Navigate to project directory using terminal
3. Create a virtual environment using Python
   ```
   python -m venv venv
   ```
4. Activate the virtual environment<br>
   For windows:
   ```
   .\venv\Scripts\Activate.ps1
   ```
   For Linux:
   ```
   source ./venv/bin/activate
   ```
5. Install required python packages from requirements.txt
   ```
   pip install -r requirements.txt
   ```
6. Download and install PostgresSQL. <br> https://www.postgresql.org/download/ 
7. Setup the .env file on the root directory of project.
   ```
   DB_USERNAME = "Postgres Username. 'postgres' by default"
   DB_PASSWORD = "Postgres Password"
   DB_HOST = "Postgres Host. 'localhost' by default"
   DB_DATABASE = "Postgres database name. 'postgres' by default"
   POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/?limit=100"  # The limit can be increased to include more Pokemons but will increase the time taken to fill the db. 
   ```

## Usage
1. Execute the following command to start the application:
   ```
   uvicorn main:app --reoad
   ```
2. Open your browser and go to the below link to fill our database with 100 Pokemons from PokeAPI. <br>
   http://127.0.0.1:8000/v1/update-pokedb/
3. Now, go to the below link to display all the Pokemons present in the database. <br>
   http://127.0.0.1:8000/v1/pokemons/
4. You can also pass query parameters "name" and "type" to filter the pokemons. <br>
   http://127.0.0.1:8000/v1/pokemons/?name=bulbasaur&type=grass
5. You can also use FastAPI's in built API documentation to review both endpoints. <br>
   http://127.0.0.1:8000/docs/
