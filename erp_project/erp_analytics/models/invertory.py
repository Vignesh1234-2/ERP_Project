inventory = []

@app.route('/api/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory)

@app.route('/api/inventory/add', methods=['POST'])
def add_inventory():
    data = request.json
    inventory.append(data)
    return jsonify({"message": "Inventory item added"})
