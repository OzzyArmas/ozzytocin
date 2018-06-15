from flask import Flask, render_template, request, jsonify
import os
import planner
import pandas as pd
import json
'''
leave room for other imports
'''

app = Flask(__name__)

@app.route("/")
def landing():
  return render_template("stylish/index.html")
@app.route("/planner", methods=["GET", "POST"])
def repayment():
    if request.method == 'GET':
        return(render_template("planner/form.html"))
    elif request.method == 'POST':
        form = None
        for k in request.form.keys():
            form = json.loads(k)
        loan_data = planner.loan_handler(form['loans'])
        asset_data = planner.asset_handler(form['assets'])
        expense_data = planner.expense_handler(form['expenses'])
        income_data = planner.income_handler(form['incomes'])
        norm_df, ira_df = planner.plan(loan_data, asset_data,\
                                       income_data, expense_data)
        print(norm_df)
        print(ira_df)
        os.chdir("/var/www/ozzytocin/ozzytocin")
        f = open("static/temp/savings.csv", 'w+')
        f2 = open("static/temp/ira_option.csv", 'w+')
        norm_df.to_csv(f)
        ira_df.to_csv(f2)
        return ''
@app.route("/plan")
def sample_plan():
    return render_template("planner/plan.html")
    # Here's Your Plan



if __name__ == "__main__":
    app.run()
