from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

data = {
    "1": {
        "id": "1",
        "name": "Burger Joint",
        "address": "119 W 56th St, New York, NY 10019",
        "media": "https://static.wixstatic.com/media/6818fc_bfbd12b39efe4f3fa67fca7922b9b42a~mv2.jpg",
        "description": "Burger Joint is a hidden gem tucked inside the Thompson Central Park Hotel. Known for its no-frills atmosphere and classic American cheeseburgers, this spot offers an authentic, old-school burger experience. The restaurant has a cult following due to its simple yet delicious menu and relaxed, graffiti-covered walls. The small venue can get crowded, but the quality of the burgers and fries makes it well worth the wait.",
        "average price": "15",
        "rating": "4.5",
        "popular dishes": ["Classic Cheeseburger", "Double Cheeseburger", "Plant-Based Burger"]
    },
    "2": {
        "id": "2",
        "name": "Shake Shack",
        "address": "Madison Square Park, New York, NY 10010",
        "media": "https://d2luv1saso99wi.cloudfront.net/Product_Burgers_ShackBurger-Single_2024_1500x920_lg1733148521.jpeg",
        "description": "Shake Shack started as a humble food cart in Madison Square Park and has grown into a national phenomenon. The ShackBurger, made with 100% Angus beef, is a favorite among locals and tourists alike. Their crinkle-cut fries and hand-spun shakes complete the ultimate fast-casual burger experience.",
        "average price": "12",
        "rating": "4.7",
        "popular dishes": ["ShackBurger", "SmokeShack", "Shroom Burger"]
    },
    "3": {
        "id": "3",
        "name": "Minetta Tavern",
        "address": "113 MacDougal St, New York, NY 10012",
        "media": "https://minettatavernny.com/content/home/slideshow/km_02.jpg",
        "description": "Minetta Tavern is an iconic NYC steakhouse that serves one of the best burgers in town: the Black Label Burger. Made with dry-aged beef and topped with caramelized onions, it’s a must-try for burger aficionados looking for a high-end experience.",
        "average price": "30",
        "rating": "4.8",
        "popular dishes": ["Black Label Burger", "Minetta Burger", "Bone Marrow"]
    },
    "4": {
        "id": "4",
        "name": "Emily",
        "address": "35 Downing St, New York, NY 10014",
        "media": "https://offloadmedia.feverup.com/secretnyc.co/wp-content/uploads/2023/11/13115608/fi-burger-1024x683.jpg",
        "description": "Emily is a well-known pizzeria, but its Emmy Burger has reached legendary status. Made with dry-aged beef, special sauce, caramelized onions, and Grafton cheddar, this burger is a perfect blend of umami and indulgence.",
        "average price": "28",
        "rating": "4.6",
        "popular dishes": ["Emmy Burger", "Colony Pizza", "Spicy Chicken Sandwich"]
    },
    "5": {
        "id": "5",
        "name": "Peter Luger Steak House",
        "address": "178 Broadway, Brooklyn, NY 11211",
        "media": "https://www.bing.com/th?id=OLC.%2fzC8oKOXqlqF1Q480x360&w=205&h=180&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=3.1&rm=2",
        "description": "Peter Luger is famous for its steaks, but their burger—made with the same dry-aged beef—is an underrated gem. Served only at lunch, it’s a thick, juicy patty with simple toppings that let the meat shine.",
        "average price": "25",
        "rating": "4.7",
        "popular dishes": ["Luger Burger", "Steak for Two", "Creamed Spinach"]
    },
    "6": {
        "id": "6",
        "name": "J.G. Melon",
        "address": "1291 3rd Ave, New York, NY 10021",
        "media": "https://images.squarespace-cdn.com/content/v1/5984a08e414fb5bec62a1680/1502204674696-RWM0TG5OP6ZD88EXZEVX/Burger.jpg?format=1500w",
        "description": "J.G. Melon is a classic New York institution serving simple yet legendary cheeseburgers. The burgers are juicy, the bun is soft, and the pickles provide just the right amount of tang. A true Upper East Side staple.",
        "average price": "14",
        "rating": "4.5",
        "popular dishes": ["Cheeseburger", "Cottage Fries", "Chili"]
    },
    "7": {
        "id": "7",
        "name": "Au Cheval",
        "address": "33 Cortlandt Alley, New York, NY 10013",
        "media": "https://images.squarespace-cdn.com/content/v1/66e88482bbf8191c95a0db67/e4e20c8d-092c-4709-8a55-5be829c44bdd/_MG_4330+%281%29.jpg?format=2500w",
        "description": "Au Cheval’s burger is often called the best in America. The griddled patty, perfectly melted cheese, and optional thick-cut bacon create a rich and decadent burger experience.",
        "average price": "22",
        "rating": "4.9",
        "popular dishes": ["Single Cheeseburger", "Double Cheeseburger", "Bacon"]
    },
    "8": {
        "id": "8",
        "name": "5 Napkin Burger",
        "address": "630 9th Ave, New York, NY 10036",
        "media": "https://images.getbento.com/accounts/47f1cb52587bad0f5447bd03679d84a0/media/images/Screenshot_2025-03-03_at_9.58.38AM.png?w=1000&fit=max&auto=compress,format&cs=origin&h=1000",
        "description": "5 Napkin Burger is a gourmet burger spot offering thick, juicy patties with a variety of toppings. Their signature burger, with gruyere cheese and rosemary aioli, is messy in the best way possible.",
        "average price": "20.50",
        "rating": "4.4",
        "popular dishes": ["The Blarney Burger", "Truffle Burger", "Lamb Kofta Burger"]
    },
    "9": {
        "id": "9",
        "name": "Corner Bistro",
        "address": "331 W 4th St, New York, NY 10014",
        "media": "https://www.cornerbistrony.com/wp-content/uploads/2020/05/bistroburger-thumb.png",
        "description": "Corner Bistro is a no-frills bar serving some of the best classic burgers in NYC. The thick, juicy patties are cooked perfectly and served in a laid-back, old-school setting.",
        "average price": "12",
        "rating": "4.3",
        "popular dishes": ["Bistro Burger", "Grilled Chicken Sandwich", "Chili"]
    },
    "10": {
        "id": "10",
        "name": "Harlem Shake",
        "address": "100 W 124th St, New York, NY 10027",
        "media": "https://harlemshake.com/wp-content/uploads/2021/08/Harlem_Classic-removebg-preview.png",
        "description": "Harlem Shake is a retro-style burger joint known for its juicy burgers and classic milkshakes. The Harlem Classic, with special sauce and onions, is a fan favorite.",
        "average price": "11",
        "rating": "4.2",
        "popular dishes": ["Harlem Classic", "Hot Mess Burger", "Sweet Potato Fries"]
    }
}


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.args.get('q', '').lower()  # Extract query from URL parameter
    if query:
        # Filter results based on query
        results = [item for item in data.values() if query in item["name"].lower()]
    else:
        results = []

    if request.method == 'POST':
        return jsonify(results)  # For AJAX request

    # Render the results in the template
    return render_template('results.html', results=results, query=query)

@app.route('/view/<int:item_id>', methods=['GET'])
def view_item(item_id):
    # Find the item by ID
    item = data.get(str(item_id))
    
    if item:
        return render_template('view.html', item=item)
    else:
        return "Item not found", 404



  
