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

<img width="1913" height="940" alt="image" src="https://github.com/user-attachments/assets/3c2228ad-7625-4ba1-bfcd-b0f577d416b7" />

<img width="1813" height="959" alt="image" src="https://github.com/user-attachments/assets/6b269ce7-49e5-4958-80eb-8b0470b26b33" />


<img width="1868" height="964" alt="image" src="https://github.com/user-attachments/assets/b94fc2c2-dbfa-494b-9861-040f33e3fce6" />

<img width="1843" height="815" alt="image" src="https://github.com/user-attachments/assets/c7bc9566-e5a6-4ea5-9f5f-afb496ce96e8" />


