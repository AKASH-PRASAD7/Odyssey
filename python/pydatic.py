"""
 Pydantic
"""

"""
- Pydantic is a data validation library for Python
- It uses Python type hints to validate data
- It is widely used in FastAPI and other web frameworks
"""

from pydantic import BaseModel, Field, field_validator

class Product(BaseModel):
    name: str
    price: float
    tax: float = 0.05

    @field_validator('price')
    def validate_price(cls, v):
        if v < 0:
            raise ValueError('Price must be positive')
        return v

    @property
    def total_price(self) -> float:
        return self.price * (1 + self.tax)

# Create a product
p1 = Product(name="Laptop", price=1200)
print(f"Name: {p1.name}")
print(f"Price: ${p1.price:.2f}")
print(f"Total Price: ${p1.total_price:.2f}")

# This will raise a ValidationError because price is negative
try:
    p2 = Product(name="Mouse", price=-50)
except Exception as e:
    print(f"\nError creating product: {e}")