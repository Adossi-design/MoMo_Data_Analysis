# MTN MoMo SMS Analysis Dashboard

This fullstack project processes Mobile Money (MoMo) SMS messages from MTN Rwanda, categorizes the transactions, stores them in a relational database, and provides a web-based dashboard to explore and visualize the data.

---

## 📁 Project Structure

```
project/
├── backend/           # Python scripts (Flask API, config, parser)
├── database/          # SQL schema, insert script, generated DB
├── frontend/          # HTML, CSS, JS dashboard
├── logs/              # Logs of unrecognized SMS messages
├── README.md
├── report.pdf
├── TEST_LOG.md
└── AUTHORS
```

---

## ⚙️ How to Run the Project

### 1. Install Python Requirements
```bash
cd backend
pip install -r requirements.txt
```

### 2. Create and Populate the Database
```bash
cd ../database
python insert_data.py
```

This will:
- Create `momo.db` using `schema.sql`
- Load data from `cleaned_data.json`

### 3. Run the Flask API Server
```bash
cd ../backend
python api.py
```
Your API will be available at: [http://localhost:5000](http://localhost:5000)

### 4. Open the Dashboard
Just open `frontend/index.html` in a web browser.

---

## 🔗 API Endpoints

- `/api/transactions` → Get all transactions  
- `/api/transactions?category=Bank Transfers` → Filter by category  
- `/api/summary` → Summary by type and totals  

---

## 📊 Dashboard Features

- Filter transactions by type
- View all transactions in a table
- Bar chart for transaction counts
- Pie chart for total amounts

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript, Chart.js
- **Backend**: Python Flask
- **Database**: SQLite
- **Parser**: Python XML processing