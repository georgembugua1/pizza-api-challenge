# RestaurantPizza controller
from flask import Blueprint, jsonify, request
from models.restaurant_pizza import RestaurantPizza
from models.pizza import Pizza
from models.restaurant import Restaurant
from app import db

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__, url_prefix='/restaurant_pizzas')

@restaurant_pizza_bp.route('', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')
    try:
        rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(rp)
        db.session.commit()
    except Exception as e:
        return jsonify({'errors': [str(e)]}), 400
    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)
    return jsonify({
        'id': rp.id,
        'price': rp.price,
        'pizza_id': rp.pizza_id,
        'restaurant_id': rp.restaurant_id,
        'pizza': {'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients},
        'restaurant': {'id': restaurant.id, 'name': restaurant.name, 'address': restaurant.address}
    }), 201
