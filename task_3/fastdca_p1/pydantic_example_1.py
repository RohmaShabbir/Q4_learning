from pydantic import BaseModel, ValidationError

# Define a simple model
class User(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None #Optional field with deafault None

# Valid data
user_data = {"id": 1, "name": "Rohma", "email": "rohma@example.com", "age": 21}
user = User(**user_data)
print(user) # id=1 name='Rohma' email='rohma@example.com' age=21
print(user.model_dump()) # {'id': 1, 'name': 'Rohma', 'email': 'rohma@example.com', 'age': 21}

# Invalid data (will raise an error)
try:
    invalid_user = User(id="not_an_int", name="Bob", email="bob@example.com")
except ValidationError as e:
    print(e)