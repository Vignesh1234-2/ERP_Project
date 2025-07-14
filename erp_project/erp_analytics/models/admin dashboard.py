@app.route('/api/admin/summary', methods=['GET'])
def admin_summary():
    return jsonify({
        "total_revenue": sum([x.get("price", 0) * x.get("quantity", 0) for x in sales_records]),
        "best_customers": sorted(customers, key=lambda x: x.get("lifetime_value", 0), reverse=True)[:5],
        "lowest_inventory": sorted(inventory, key=lambda x: x.get("stock_qty", 0))[:5]
    })