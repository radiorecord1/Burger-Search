
    // Array of popular burger items
    const popularBurgers = [
        { name: "Black Label Burger", restaurant: "Minetta Tavern", img: "https://minettatavernny.com/content/home/slideshow/km_02.jpg", 
        description: "Minetta Tavern is an iconic NYC steakhouse that serves one of the best burgers in town: the Black Label Burger. Made with dry-aged beef and topped with caramelized onions, it’s a must-try for burger aficionados looking for a high-end experience.", 
        link: "/view/3" },
        { name: "Emmy Burger", restaurant: "Emily Square Pizzeria", img: "https://offloadmedia.feverup.com/secretnyc.co/wp-content/uploads/2023/11/13115608/fi-burger-1024x683.jpg", 
        description: "Emily is a well-known pizzeria, but its Emmy Burger has reached legendary status. Made with dry-aged beef, special sauce, caramelized onions, and Grafton cheddar, this burger is a perfect blend of umami and indulgence.", 
        link: "/view/4" },
        { name: "Cheeseburger", restaurant: "J.G. Melon", img: "https://images.squarespace-cdn.com/content/v1/5984a08e414fb5bec62a1680/1502204674696-RWM0TG5OP6ZD88EXZEVX/Burger.jpg?format=1500w", 
            description: "J.G. Melon is a classic New York institution serving simple yet legendary cheeseburgers. The burgers are juicy, the bun is soft, and the pickles provide just the right amount of tang. A true Upper East Side staple.", 
            link: "/view/6" }
    ];

    function loadPopularItems() {
        const container = document.getElementById("popular-items");

        popularBurgers.forEach(burger => {
            const burgerCard = `
                <div class="col-md-4">
                    <div class="card mb-4 shadow-sm">
                        <img src=${burger.img} class="card-img-top" alt="${burger.name}">
                        <div class="card-body">
                            <h5 class="card-title">${burger.name}</h5>
                            <h5 class="card-title">${burger.restaurant}</h5>
                            <p class="card-text">${burger.description}</p>
                            <a href="${burger.link}" class="btn btn-primary">View More</a>
                        </div>
                    </div>
                </div>
            `;
            container.innerHTML += burgerCard;
        });
    }

    document.addEventListener("DOMContentLoaded", loadPopularItems);
