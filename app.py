from flask import Flask, render_template, request

app = Flask(__name__)

# Tourism dataset
destinations = [
    {
        "name": "Goa",
        "type": "Beach",
        "budget": "Medium",
        "season": "Winter",
        "activity": "Adventure",
        "description": "Beautiful beaches, water sports and nightlife."
    },
    {
        "name": "Manali",
        "type": "Mountain",
        "budget": "Medium",
        "season": "Winter",
        "activity": "Adventure",
        "description": "Mountains, snow, trekking and adventure activities."
    },
    {
        "name": "Jaipur",
        "type": "Historical",
        "budget": "Low",
        "season": "Winter",
        "activity": "Culture",
        "description": "Forts, palaces and rich Rajasthani culture."
    },
    {
        "name": "Kerala",
        "type": "Nature",
        "budget": "Medium",
        "season": "Monsoon",
        "activity": "Relaxation",
        "description": "Backwaters, greenery and peaceful natural beauty."
    },
    {
        "name": "Mumbai",
        "type": "City",
        "budget": "Medium",
        "season": "Winter",
        "activity": "Entertainment",
        "description": "Marine Drive, Gateway of India and city attractions."
    },
    {
        "name": "Ladakh",
        "type": "Mountain",
        "budget": "High",
        "season": "Summer",
        "activity": "Adventure",
        "description": "High mountains, lakes and thrilling road trips."
    },
    {
        "name": "Agra",
        "type": "Historical",
        "budget": "Low",
        "season": "Winter",
        "activity": "Culture",
        "description": "Home of the Taj Mahal and Mughal heritage."
    },
    {
        "name": "Andaman",
        "type": "Beach",
        "budget": "High",
        "season": "Winter",
        "activity": "Relaxation",
        "description": "Tropical beaches, islands and water activities."
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    budget = request.form.get("budget")
    season = request.form.get("season")
    activity = request.form.get("activity")

    recommendations = []

    for place in destinations:
        score = 0

        if place["budget"] == budget:
            score += 3

        if place["season"] == season:
            score += 2

        if place["activity"] == activity:
            score += 3

        if score >= 5:
            recommendations.append(place)

    # If no exact match is found
    if not recommendations:
        recommendations = destinations[:3]

    return render_template(
        "index.html",
        recommendations=recommendations
    )


if __name__ == "__main__":
    app.run(debug=True)
