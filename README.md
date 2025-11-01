
# Movie Recommendation System

A simple **Movie Recommendation System** built using **Python** for backend recommendations and **JavaScript/HTML** for the frontend interface. This system suggests movies similar to a given movie based on genres.

---

## Table of Contents

- [Demo](#demo)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Files in the Repository](#files-in-the-repository)
- [Contributing](#contributing)
- [License](#license)

---

## Demo

1. Open `index.html` in your browser.  
2. Type a movie name in the input box.  
3. Click the **Recommend** button to see similar movie recommendations.

---

## Features

- Suggests movies similar to the input movie based on genre similarity.  
- Uses **cosine similarity** on genre vectors to find similar movies.  
- Interactive web interface using **HTML** and **JavaScript**.  
- Supports JSON-based recommendations.

---

## Technologies Used

- **Python 3** — for computing movie similarity (`recommendation.py`)  
- **Pandas** — for data handling  
- **scikit-learn** — for `MultiLabelBinarizer` and `cosine_similarity`  
- **HTML/CSS/JavaScript** — frontend interface  
- **JSON** — for storing movie recommendations  

---

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/brunda-yadav/movie-recommendation-.git
cd movie-recommendation-
