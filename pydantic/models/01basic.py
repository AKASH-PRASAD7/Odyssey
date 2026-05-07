from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    age: int

user = User(id = 1,name = "Akash",age = 18)

# Product model

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True # Default value


product = Product(id = 1, name = "Phone", price = "1000.0")

print(product)
