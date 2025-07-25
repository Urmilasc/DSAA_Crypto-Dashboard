# 📊 Crypto Dashboard - EDA and Streamlit Visualization

This project is part of a data science mini-project assignment. It involves fetching cryptocurrency data using a public API, performing exploratory data analysis (EDA), and building an interactive dashboard using the Streamlit library.

---

## 🔗 API Used

- **CoinGecko API**: Used to fetch real-time cryptocurrency market data.  
  Website: [https://www.coingecko.com/](https://www.coingecko.com/)

---

## 🧠 Features Covered

### 1. Exploratory Data Analysis (EDA)
- Data Cleaning and Inspection
- Statistical Summary
- Visualizations:
  - Bar Charts
  - Correlation Heatmaps
  - Line Graphs
  - Distribution Plots

### 2. Dashboard with Streamlit
- Interactive layout using Streamlit
- Filter options for selecting cryptocurrency
- Dynamic visualization updates
- Real-time rendering of charts with Matplotlib & Seaborn

---

## 📁 Project Structure

crypto_dashboard/
│
├── crypto_EDA.ipynb # Jupyter notebook with data analysis & explanation
├── dashboard.py # Streamlit dashboard code
├── requirements.txt # (Optional) List of required libraries
├── README.md # This file
└── screenshots/ # Folder containing dashboard images
└── dashboard_view.png # Add your screenshot here


## ▶️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/crypto_dashboard.git
cd crypto_dashboard
Step 2: Set Up Virtual Environment (Optional)

python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
Step 3: Install Requirements

pip install -r requirements.txt
If you don’t have a requirements.txt, install manually:


pip install pandas matplotlib seaborn streamlit requests
Step 4: Run the Streamlit App

streamlit run dashboard.py
🖼️ Dashboard Preview

