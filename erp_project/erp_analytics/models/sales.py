from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
sales_records = []

@app.route('/api/sales', methods=['GET'])
def get_sales():
    return jsonify(sales_records)

@app.route('/api/sales', methods=['POST'])
def add_sale():
    data = request.json
    sales_records.append(data)
    return jsonify({"message": "Sale record added"})
