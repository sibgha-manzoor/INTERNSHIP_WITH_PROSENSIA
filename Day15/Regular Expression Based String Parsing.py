import re
from datetime import datetime

def extract_dates(text):
    date_pattern = r'\b(\d{4})-(\d{2})-(\d{2})\b'
    matches = re.findall(date_pattern, text)
    
    valid_dates = []
    for match in matches:
        year, month, day = map(int, match)
        try:
            datetime(year, month, day)
            valid_dates.append(f"{year:04d}-{month:02d}-{day:02d}")
        except ValueError:
            continue
    
    return valid_dates

text = "Some important dates are 2024-02-29, 2023-11-01, and 2024-04-31."
print(extract_dates(text))