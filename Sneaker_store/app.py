from flask import Flask,render_template,session,redirect,url_for,request

app= Flask(__name__)

app.secret_key="sneaker-hub-secret-key"

@app.route("/")
def home():
    product_name= "Air Runner X1"
    price=12999
    
    return render_template("index.html",product_name=product_name,price=price)

@app.route("/products")
def products():
    sneakers=[{"id":1,"name":"Air Runner X1","price":12999,"image":"shoe1.jpg.jpeg"},{"id":2,"name":"Street Force","price":9999,"image":"shoe2.jpg.jpeg"},{"id":3,"name":"Urbas Boost","price":14999,"image":"shoe3.jpg.jpeg"},{"id":4,"name":"Velocity Pro","price":16999,"image":"shoe4.jpg.jpeg"},{"id":5,"name":"Velocity X2","price":19000,"image":"shoe5.jpg.jpeg"}]
    return render_template("products.html",sneakers=sneakers)


@app.route("/cart")
def cart():
    cart_items=session.get("cart", [])
    
    total = 0
    
    for item in cart_items:
        total +=item["price"] * item["quantity"]
        
    return render_template("cart.html",cart_items=cart_items,total=total)
    
    
@app.route("/add-to-cart/<int:product_id>")
def add_to_cart(product_id):
    

    sneakers = [
        {
            "id": 1,
            "name": "Air Runner X1",
            "price": 12999,
            "image": "shoe1.jpg.jpeg"
        },
        {
            "id": 2,
            "name": "Street Force",
            "price": 9999,
            "image": "shoe2.jpg.jpeg"
        },
        {
            "id": 3,
            "name": "Urban Boost",
            "price": 14999,
            "image": "shoe3.jpg.jpeg"
        },
        {
            "id":4,
            "name":"Velocity Pro",
            "price":16999,
            "image":"shoe4.jpg.jpeg"
        },
        {
            
         "id":5,
         "name":"Velocity X2",
         "price":19000,
         "image":"shoe5.jpg.jpeg"
         
         }
    ]

    product = next(
        (sneaker for sneaker in sneakers if sneaker["id"] == product_id),
        None
    )

    if product:
        cart = session.get("cart", [])

        cart.append({
            "name": product["name"],
            "price": product["price"],
            "image": product["image"],
            "quantity": 1
        })

        session["cart"] = cart

    return redirect(url_for("cart"))

@app.route("/checkout")
def checkout():

    cart_items = session.get("cart", [])

    print("CHECKOUT CART:", cart_items)

    total = 0

    for item in cart_items:
        total += item["price"] * item["quantity"]

    print("CHECKOUT TOTAL:", total)

    return render_template(
        "checkout.html",
        cart_items=cart_items,
        total=total
    )



@app.route("/place-order", methods=["POST"])
def place_order():

    name = request.form.get("name")
    phone = request.form.get("phone")
    address = request.form.get("address")
    city = request.form.get("city")

    cart_items = session.get("cart", [])

    total = 0

    for item in cart_items:
        total += item["price"] * item["quantity"]

    session.pop("cart", None)

    return render_template(
        "success.html",
        name=name,
        phone=phone,
        address=address,
        city=city,
        total=total
    )
    
    
    
@app.route("/clear-cart")
def clear_cart():

    session.pop("cart", None)

    return redirect(url_for("cart"))

@app.route("/about")
def about():
    return render_template("about.html")

  
if __name__ == "__main__":
    app.run(debug=True)