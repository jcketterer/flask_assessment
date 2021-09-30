from flask import Flask, redirect, request, render_template, flash
from helper import final_amount, correct_curr_code, valid_number
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config["SECRET_KEY"] = "donttellmom"


@app.route("/")
def home():
    """Route to the home page"""

    return render_template("base.html")


@app.route("/", methods=["POST"])
def form():
    """handles post request for user submission"""

    from_currency = request.form.get("from-currency").upper()

    if not correct_curr_code(from_currency) or not from_currency:
        flash("Starting currency not a valid currency code.")
        return redirect("/")

    to_currency = request.form.get("to-currency").upper()

    if not correct_curr_code(to_currency) or not to_currency:
        flash("Ending currency not a valid currency code.")
        return redirect("/")

    amount = request.form.get("amount")
    if not valid_number(amount):
        flash("Did not enter a valid number")
        return redirect("/")

    output_data = final_amount(from_currency, to_currency, amount)

    return render_template("base.html", output_data=output_data)
