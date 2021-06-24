"""
staysafe prediction page view.
Mainly developed by QX; Partially adapted by JD
URLs include:
/predict/
"""
import os
import flask
import staysafe
import sys

@staysafe.app.route('/predict', methods=['GET', 'POST'])
def show_prediction():
    connection = staysafe.model.get_db()
    if flask.request.method == 'POST':
        # Invalid input: too long
        if flask.request.form["building"] == "Corgi":
            return flask.render_template("corgi.html")
        else: 
            return flask.render_template("Ragdoll.html")

        
