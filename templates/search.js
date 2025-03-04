document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form.search-container");
    const resultsList = document.getElementById("results-list");

    form.addEventListener("submit", function (e) {
        e.preventDefault(); // Prevent form from submitting the traditional way
        const query = document.querySelector("input[name='q']").value;

        // Send the search query to the server using AJAX (POST method)
        fetch('/search?q=' + encodeURIComponent(query), {
            method: 'GET',  // Use GET to send the query as a URL parameter
        })
        .then(response => response.text())  // Use .text() for HTML content
        .then(data => {
            document.getElementById("loading").style.display = "none"; // Hide the loading text
            resultsList.innerHTML = data; // Insert the HTML response into the page
        })
        .catch(error => console.error("Error fetching search results:", error));
    });
});
