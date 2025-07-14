@app.route('/api/genai/query', methods=['POST'])
def genai_query():
    prompt = request.json.get('prompt')
    # Stub response for demo
    result = f"Summary for prompt: {prompt}"
    return jsonify({"response": result})
