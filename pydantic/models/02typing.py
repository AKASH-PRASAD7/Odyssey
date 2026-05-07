from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]

class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None # optional field default val's none

cart = Cart(user_id = 1, items = [], quantities = {})

print(cart)

blog = BlogPost(title = "hello", content = " hello howdy partner !")

print(blog)


# Employee 

class Employee(BaseModel):
    id: int
    name: str = Field(
        ..., # (...) = required
        min_length = 3,
        max_length = 45,
        description = "employee name",
        examples = "Jhon doe"
        ) 
    department: Optional[str] = "General"
    salary: float = Field(..., ge = 10000) # > 100000