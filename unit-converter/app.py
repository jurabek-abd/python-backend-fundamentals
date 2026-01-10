from flask import Flask, redirect, render_template, request, url_for

LENGTH_TO_METER = {
    "millimeter": 0.001,
    "centimeter": 0.01,
    "meter": 1.0,
    "kilometer": 1000.0,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "mile": 1609.344,
}

WEIGHT_TO_GRAM = {
    "milligram": 0.001,
    "gram": 1.0,
    "kilogram": 1000.0,
    "ounce": 28.3495,
    "pound": 453.592,
}


def convert_length(value, from_unit, to_unit):
    value_in_meters = value * LENGTH_TO_METER[from_unit]
    return value_in_meters / LENGTH_TO_METER[to_unit]


def convert_weight(value, from_unit, to_unit):
    value_in_grams = value * WEIGHT_TO_GRAM[from_unit]
    return value_in_grams / WEIGHT_TO_GRAM[to_unit]


def to_kelvin(value, unit):
    if unit == "celsius":
        return value + 273.15
    elif unit == "fahrenheit":
        return (value - 32) * 5 / 9 + 273.15
    elif unit == "kelvin":
        return value


def from_kelvin(value, unit):
    if unit == "celsius":
        return value - 273.15
    elif unit == "fahrenheit":
        return (value - 273.15) * 9 / 5 + 32
    elif unit == "kelvin":
        return value


def convert_temperature(value, from_unit, to_unit):
    kelvin = to_kelvin(value, from_unit)
    return from_kelvin(kelvin, to_unit)


app = Flask(__name__)


@app.route("/")
def index():
    return redirect(url_for("length"))


@app.route("/length", methods=["GET", "POST"])
def length():
    result = None
    value = float(request.form["value"])
    from_unit = request.form["from_unit"]
    to_unit = request.form["to_unit"]
    if request.method == "POST":
        result = convert_length(value, from_unit, to_unit)

    return render_template(
        "length.html",
        result=result,
        input_value=value,
        from_unit=from_unit,
        to_unit=to_unit,
    )


@app.route("/weight", methods=["GET", "POST"])
def weight():
    result = None
    value = float(request.form["value"])
    from_unit = request.form["from_unit"]
    to_unit = request.form["to_unit"]
    if request.method == "POST":
        result = convert_weight(value, from_unit, to_unit)

    return render_template(
        "weight.html",
        result=result,
        input_value=value,
        from_unit=from_unit,
        to_unit=to_unit,
    )


@app.route("/temperature", methods=["GET", "POST"])
def temperature():
    result = None
    value = float(request.form["value"])
    from_unit = request.form["from_unit"]
    to_unit = request.form["to_unit"]
    if request.method == "POST":
        result = convert_temperature(value, from_unit, to_unit)

    return render_template(
        "temperature.html",
        result=result,
        input_value=value,
        from_unit=from_unit,
        to_unit=to_unit,
    )
