# Carlifornia House Price API

### This is a Simple api to predict carlifornia House Price

## Usage

Go to your command line and type
```bash
git clone https://github.com/emxelux/Simple-House-Price-API.git
```
## Then Run

``` bash
pip install -r requirements.txt
cd Simple-House-Price-API
```
### Run the app on localhost
```bash
uvicorn app.main:app --reload
```
### The following is the input schema
```text
    longitude: float
    latitude: float
    housing_median_age: int
    total_rooms: int
    total_bedrooms:float
    population:int
    households: int
    median_income:float
    ocean_proximity:object
```