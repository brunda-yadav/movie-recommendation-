<<<<<<< HEAD
let recommendations = {};

// Load the JSON file
async function loadRecommendations() {
    const response = await fetch('recommendations.json');
    recommendations = await response.json();
}

loadRecommendations();

// Show recommendations based on input
function showRecommendations() {
    const movie = document.getElementById('movieInput').value;
    const list = document.getElementById('results');
=======
>>>>>>> cc0fb9e78d96c96c3b12e6485a8b5fed70c20e3a
    list.innerHTML = '';

    if (recommendations[movie]) {
        recommendations[movie].forEach(title => {
            const li = document.createElement('li');
            li.textContent = title;
            list.appendChild(li);
        });
    } else {
        const li = document.createElement('li');
        li.textContent = 'No recommendations found';
        list.appendChild(li);
    }
}
