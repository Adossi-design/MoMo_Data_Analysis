
import xml.etree.ElementTree as ET
import json
import os
from utils import normalize_amount, extract_date, categorize_sms

INPUT_XML = "../DataWorld/Data/momo_data.xml"
OUTPUT_JSON = "cleaned_data.json"
LOG_FILE = "logs/ignored_sms.log"

def parse_sms_xml(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    cleaned_messages = []
    ignored_messages = []

    for sms in root.findall("sms"):
        body = sms.attrib.get("body", "")
        category = categorize_sms(body)

        if category == "Unknown":
            ignored_messages.append(body)
            continue

        amount = normalize_amount(body)
        date = extract_date(body)

        cleaned_messages.append({
            "body": body,
            "category": category,
            "amount": amount,
            "date": date.strftime("%Y-%m-%d %H:%M:%S") if date else None
        })

    return cleaned_messages, ignored_messages

def save_output(cleaned, ignored):
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(cleaned, f, indent=4, ensure_ascii=False)

    os.makedirs("logs", exist_ok=True)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        for line in ignored:
            f.write(line + "\n")

if __name__ == "__main__":
    cleaned, ignored = parse_sms_xml(INPUT_XML)
    save_output(cleaned, ignored)
    print(f"✔ Done! Cleaned: {len(cleaned)} | Ignored: {len(ignored)}")
