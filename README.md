# AirBnB Clone - Version 2

## Overview
This project is the second version of the AirBnB Clone. It introduces database storage using SQLAlchemy as an Object-Relational Mapper (ORM) and enhances the application by implementing relationships and advanced features such as Many-to-Many associations. The goal is to manage persistent data and utilize database storage effectively.

## Key Features
- Storage management using a database (MySQL) with SQLAlchemy.
- Implementation of relationships among models (One-to-Many, Many-to-Many).
- Use of environment variables to switch between database and file storage.
- Full support for Python and SQL database interaction.

## Environment
- **OS:** Ubuntu 20.04 LTS
- **Python:** 3.8.5
- **MySQL:** 8.0
- **SQLAlchemy:** 1.4.x
- **MySQLdb:** 2.0.x

## Repository
- **GitHub:** [AirBnB_clone_v2](https://github.com/username/AirBnB_clone_v2)

## Project Structure
```
AirBnB_clone_v2/
|│
|├── models/
|│   |│
|│   |├── base_model.py
|│   |├── user.py
|│   |├── place.py
|│   |├── city.py
|│   |├── state.py
|│   |├── amenity.py
|│   |├── review.py
|│   |└── __init__.py
|│
|├── console.py
|└── README.md
```

## Models
Each model inherits from `BaseModel` and includes SQLAlchemy attributes for database integration.

### User Model (`models/user.py`)
- **Table Name:** `users`
- Attributes:
  - `email`: String (128), Not Null
  - `password`: String (128), Not Null
  - `first_name`: String (128), Nullable
  - `last_name`: String (128), Nullable
- Relationships:
  - `places`: One-to-Many with `Place`
  - `reviews`: One-to-Many with `Review`

### Place Model (`models/place.py`)
- **Table Name:** `places`
- Attributes:
  - `city_id`: String (60), Not Null (Foreign Key: `cities.id`)
  - `user_id`: String (60), Not Null (Foreign Key: `users.id`)
  - `name`: String (128), Not Null
  - `description`: String (1024), Nullable
  - `number_rooms`: Integer, Not Null, Default 0
  - `number_bathrooms`: Integer, Not Null, Default 0
  - `max_guest`: Integer, Not Null, Default 0
  - `price_by_night`: Integer, Not Null, Default 0
  - `latitude`: Float, Nullable
  - `longitude`: Float, Nullable
- Relationships:
  - `reviews`: One-to-Many with `Review`
  - `amenities`: Many-to-Many with `Amenity`

### City Model (`models/city.py`)
- **Table Name:** `cities`
- Attributes:
  - `state_id`: String (60), Not Null (Foreign Key: `states.id`)
  - `name`: String (128), Not Null
- Relationships:
  - `places`: One-to-Many with `Place`

### State Model (`models/state.py`)
- **Table Name:** `states`
- Attributes:
  - `name`: String (128), Not Null
- Relationships:
  - `cities`: One-to-Many with `City`

### Amenity Model (`models/amenity.py`)
- **Table Name:** `amenities`
- Attributes:
  - `name`: String (128), Not Null
- Relationships:
  - `place_amenities`: Many-to-Many with `Place`

### Review Model (`models/review.py`)
- **Table Name:** `reviews`
- Attributes:
  - `text`: String (1024), Not Null
  - `place_id`: String (60), Not Null (Foreign Key: `places.id`)
  - `user_id`: String (60), Not Null (Foreign Key: `users.id`)

## Storage
The application supports two types of storage engines:

1. **FileStorage:** Serializes instances to a JSON file and deserializes them back.
2. **DBStorage:** Utilizes MySQL for database management and SQLAlchemy ORM.

Switch between storage engines by setting the environment variable `HBNB_TYPE_STORAGE` to either `file` or `db`.

## Relationships
- **User - Place:** One-to-Many
- **Place - Review:** One-to-Many
- **Place - Amenity:** Many-to-Many (through `place_amenity` table)

## Example Usage
### Creating a User
```bash
echo 'create User email="gui@hbtn.io" password="guipwd" first_name="Guillaume" last_name="Snow"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```

### Querying the Database
```sql
SELECT * FROM users\G;
SELECT * FROM places\G;
SELECT * FROM reviews\G;
```

## Testing
Run unit tests using the command:
```bash
python3 -m unittest discover tests
```

## Author
## Contributors

- Original Authors:
  - Jane Doe
  - John Smith
- Updates by:
  - Dzeble kwame (GitHub: DzeBakuEso)

---
End of `README.md`
