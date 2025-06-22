# TEST LOG & COMMAND OUTPUT GUIDE

This file provides a guide to running each part of the project and what output to expect.

---

## 1. Setup Backend Dependencies
```bash
cd backend
pip install -r requirements.txt
```
**Expected Output:**  
Successfully installs Flask.

---

## 2. Create Database
```bash
cd ../database
python insert_data.py
```
**Expected Output:**  
- "Database created successfully."
- "Data inserted: [count] transactions"

---

## 3. Run Flask API
```bash
cd ../backend
python api.py
```
**Expected Output:**  
Flask server running on http://127.0.0.1:5000

Test endpoints:
- `/api/transactions`
- `/api/summary`

---

## 4. Open Frontend Dashboard
```bash
Open frontend/index.html in your browser
```
**Expected Output:**  
- Dashboard UI appears
- Bar and pie charts load
- Transactions table is populated

---

This file is helpful for verifying everything works as expected during setup.