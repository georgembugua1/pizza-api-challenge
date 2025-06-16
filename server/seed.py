# Seed data for the database
from app import db, create_app
from models.restaurant import Restaurant
from models.pizza import Pizza
from models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    r1 = Restaurant(name="Kiki's Pizza", address="address3")
    r2 = Restaurant(name="Mario's Pizza", address="address1")
    p1 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    rp1 = RestaurantPizza(price=5, pizza_id=p1.id, restaurant_id=r1.id)
    rp2 = RestaurantPizza(price=10, pizza_id=p2.id, restaurant_id=r2.id)
    db.session.add_all([rp1, rp2])
    db.session.commit()

    print('Database seeded!')
