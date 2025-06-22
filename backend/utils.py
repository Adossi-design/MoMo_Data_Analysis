
import re
from datetime import datetime

def normalize_amount(text):
    amount = re.findall(r"[\d,]+", text)
    if not amount:
        return None
    return int(amount[0].replace(",", ""))

def extract_date(text):
    try:
        match = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", text)
        if match:
            return datetime.strptime(match.group(1), "%Y-%m-%d %H:%M:%S")
    except:
        return None

def categorize_sms(body):
    body_lower = body.lower()
    if "you have received" in body_lower:
        return "Incoming Money"
    elif "your payment of" in body_lower and "completed" in body_lower:
        return "Payment"
    elif "withdrawn" in body_lower:
        return "Agent Withdrawal"
    elif "transferred" in body_lower:
        return "P2P Transfer"
    elif "bank deposit" in body_lower:
        return "Bank Deposit"
    elif "airtime" in body_lower:
        return "Airtime Purchase"
    elif "bundle" in body_lower:
        return "Bundle Purchase"
    elif "cash power" in body_lower:
        return "Cash Power Payment"
    else:
        return "Unknown"
