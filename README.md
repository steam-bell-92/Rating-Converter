## 🔁 Rating Converter: CodeChef ↔ Codeforces

A simple and intuitive rating converter that translates competitive programming ratings between CodeChef and Codeforces platforms.<br>
The project uses a ***univariate linear regression model*** trained via gradient descent to estimate equivalent ratings, providing platform-specific interpretations like titles (for CodeChef) and stars (for Codeforces).

---

## 📌 Features

- 🔄 Convert ratings from **CodeChef to Codeforces** and vice versa.
- 📊 Displays **titles** for CodeChef and **star levels** for Codeforces.
- ⚙️ Simple linear model with minimal input requirement.
- 🌈 Web interface styled with `HTML` and `CSS`, powered by `JavaScript`.

---

## 💻 Tech Stack

- **`Python` (`Google Colab`)** – for training the ML model using gradient descent.
- **`HTML & CSS`** – for structuring and styling the frontend.
- **`JavaScript`** – for integrating model predictions and DOM interaction.

---

## 🧠 Model Details

- Type: Univariate Linear Regression
- Algorithm: Gradient Descent
- Performance: `R² Score`: 0.39146998581676273
- Note: Due to limited dataset diversity, feature engineering was intentionally avoided.

---

## 🌐 Live Website
<p>Try the rating converter here: <a href='https://steam-bell-92.github.io/Rating-Converter/'>WEB</a></p>

---

## 🚀 Usage

1. Choose the source platform: **CodeChef** or **Codeforces**
2. Enter your rating (as an integer)
3. View your predicted equivalent rating on the other platform:
   - CodeChef ➝ Codeforces: Output includes predicted rating **+ Star Level**
   - Codeforces ➝ CodeChef: Output includes predicted rating **+ Title**
4. If want to use again try refreshing site

---

## 📁 File Structure:
```
Rating-Converter/
├── index.html         🔹 Main HTML file containing UI layout
├── style.css          🔹 CSS for styling the converter interface
├── javascript.js      🔹 JavaScript for handling logic and model prediction
├── final_cccf.csv     🔹 Dataset for model prediction
├── CC_CF.ipynb        🔹 Colab notebook for EDA, training a univariate linear regression model, and exporting model parameters
└── README.md          🔹 Project documentation
```

---

## 👤 Author
Anuj Kulkarni - aka - steam-bell-92

Also this project was part of Summer-of-ML by BSoC
