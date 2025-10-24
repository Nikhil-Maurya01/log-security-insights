import re
import csv
from collections import defaultdict

# Input and output file paths
log_file_path = 'access.log'  # Replace with your actual log file path
output_csv_path = 'security_report.csv'

# Regex pattern to extract IP and status code
log_pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+).+" (\d{3}) ')

# Dictionary to count failed attempts
failed_attempts = defaultdict(int)

# Extract and Transform
with open(log_file_path, 'r', encoding='utf-8') as file:
    for line in file:
        match = log_pattern.search(line)
        if match:
            ip, status = match.groups()
            if status in ['401', '403']:
                failed_attempts[ip] += 1

# Load to CSV
with open(output_csv_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['IP Address', 'Failed Attempts'])
    for ip, count in failed_attempts.items():
        writer.writerow([ip, count])

print(f"Security report saved to {output_csv_path}")
