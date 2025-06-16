git# Pizza App Challenge

## Setup Instructions

1. **Install dependencies**

```
pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell
```

2. **Database setup**

```
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

3. **Seed the database**

```
python server/seed.py
```

---

## Project Structure (MVC)

```
server/
├── app.py
├── config.py
├── models/
│   ├── __init__.py
│   ├── restaurant.py
│   ├── pizza.py
│   └── restaurant_pizza.py
├── controllers/
│   ├── __init__.py
│   ├── restaurant_controller.py
│   ├── pizza_controller.py
│   └── restaurant_pizza_controller.py
├── seed.py
```

---

## Routes

### GET /restaurants
Returns a list of all restaurants.

### GET /restaurants/<id>
Returns details of a single restaurant and its pizzas.
- 404 if not found: `{ "error": "Restaurant not found" }`

### DELETE /restaurants/<id>
Deletes a restaurant and all related RestaurantPizzas.
- 204 No Content if successful
- 404 if not found: `{ "error": "Restaurant not found" }`

### GET /pizzas
Returns a list of pizzas.

### POST /restaurant_pizzas
Creates a new RestaurantPizza.

**Request:**
```
{ "price": 5, "pizza_id": 1, "restaurant_id": 3 }
```

**Success Response:**
```
{
  "id": 4,
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3,
  "pizza": { "id": 1, "name": "Emma", "ingredients": "Dough, Tomato Sauce, Cheese" },
  "restaurant": { "id": 3, "name": "Kiki's Pizza", "address": "address3" }
}
```

**Error Response:**
```
{ "errors": ["Price must be between 1 and 30"] }
```
With 400 Bad Request

---

## Validation Rules
- RestaurantPizza.price must be between 1 and 30 (inclusive)

---

## Postman
- Import `challenge-1-pizzas.postman_collection.json` into Postman to test all routes.

---

## Submission Checklist
- [x] MVC folder structure
- [x] Models with validations and relationships
- [x] All routes implemented
- [x] Postman tests passing
- [x] Well-written README.md
