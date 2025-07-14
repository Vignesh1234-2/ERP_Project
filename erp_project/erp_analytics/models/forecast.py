import random
@app.route('/api/forecast/run', methods=['POST'])
def forecast():
    predicted_revenue = random.randint(10000, 50000)
    return jsonify({"predicted_revenue": predicted_revenue})
