from flask import Flask, request, jsonify
import openpyxl
import os
from datetime import datetime

app = Flask(__name__)

# Path to the Excel file
EXCEL_FILE = "exam_data.xlsx"

# Function to initialize Excel file if it doesn't exist
def initialize_excel_file():
    if not os.path.exists(EXCEL_FILE):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.append(["Timestamp", "Question 1", "Question 2", "Question 3"])
        workbook.save(EXCEL_FILE)

initialize_excel_file()

# Route to serve the HTML file
@app.route('/')
def index():
    return app.send_static_file('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    
    # Save data to Excel file
    workbook = openpyxl.load_workbook(EXCEL_FILE)
    sheet = workbook.active
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append([timestamp, data['q1'], data['q2'], data['q3']])
    workbook.save(EXCEL_FILE)

    return jsonify({"message": "Your answers have been submitted successfully!"})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
