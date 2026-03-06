from pydantic import BaseModel

class InputData(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: int
    total_rooms: int
    total_bedrooms:float
    population:int
    households: int
    median_income:float
    ocean_proximity:object

class PredResponse(BaseModel):
    Price: float

    