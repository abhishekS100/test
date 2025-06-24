def recommend_plan(data):
    current_plan = data.get("current_plan")
    usage = data.get("usage")
    if current_plan == "150 Mbps":
        return {
            "recommended_plan": "Gigabit Extra (1.25 Gbps)",
            "price": "$89.99/month",
            "bonus": "Includes SecurityEdge™"
        }
    return {"message": "No better plan available."}

def submit_order(data):
    return {
        "status": "Order Submitted",
        "plan": data.get("plan"),
        "confirmation": "You will receive an email shortly."
    }
