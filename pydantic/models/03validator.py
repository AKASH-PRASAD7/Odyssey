from pydantic import BaseModel, field_validator, model_validator, computed_field, Field

class User(BaseModel):
    username: str

    @field_validator('username') # runs before, while getting values
    def username_len(cls, value):

        if(len(value) < 3):
            raise ValueError("username length should be greater than 3 chars")
        return value

class SignUpData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode = 'after') # runs after getting all values
    def password_match(cls, value):

        if(value.password != value.confirm_password):
            raise Exception("Password not matching")
        return value

class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity

# Booking model

class Booking(BaseModel):
    user_id: int
    room_id: int
    night: int = Field(..., ge = 1)
    rate_per_night: float

    @computed_field
    @property
    def total_price(self) -> float:
        return self.night * self.rate_per_night


