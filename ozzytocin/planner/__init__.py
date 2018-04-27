#! /usr/bin/env python
import pandas as pd
import numpy as np
def loan_handler(loans):
    total_debt = 0
    total_principal = 0
    for loan in loans:
        print(loan)
        total_debt += float(loan['amount'])
        total_principal = float(loan['principal']) * 12
    avg_interest = 0
    for loan in loans:
        avg_interest += (float(loan['amount']) * float(loan['interest']))/total_debt
    avg_interest = avg_interest / 100
    print(avg_interest)
    min_pay = total_principal + (total_debt * avg_interest)
    return {"total_debt" : total_debt,
            "interest" : avg_interest,
            "pi" : min_pay, #principal and Interest
            "loans" : loans}


def asset_handler(assets):
    total_assets = 0
    print(assets)
    for asset in assets:
        total_assets += float(asset['amount'])
    avg_interest = 0
    for asset in assets:
        avg_interest += (float(asset['amount']) * float(asset['interest']))/total_assets
    avg_interest = avg_interest / 100
    return {"total_assets" : total_assets,
            "interest" : avg_interest,
            "assets" : assets}


def income_handler(incomes):
    total_income = 0
    for income in incomes:
        total_income += float(income['amount'])
    return {"total_income" : total_income,
            "incomes" : incomes}


def expense_handler(expenses):
    total_expenses = 0
    for expense in expenses:
        total_expenses += float(expense['amount']) * 12
    return {"total_exp" : total_expenses,
             "expenses" : expenses}


def plan(loans, assets, income, expenses, ex_ira = .1):
    iter_payments = loans['total_debt']
    normal_savings = 0
    ira_savings = 0
    ira = 0
    asset_apr = assets['total_assets']
    normal_df = pd.DataFrame(columns=['year','remaining debt', 'savings', 'assets'])
    ira_df = pd.DataFrame(columns=['year', 'remaining debt', 'savings','ira','assets'])
    year = 1
    normal_savings += income['total_income'] - expenses['total_exp'] \
                    - loans['pi']
    #print(iter_payments)

    normal_df = normal_df.append(pd.DataFrame([[year, iter_payments, normal_savings, asset_apr]],\
                        columns=normal_df.columns))
    ### WITH IRA ###
    expected_savings = income['total_income'] - expenses['total_exp'] \
                    - loans['pi']
    ira_added = min(expected_savings/2, 5500) ### To ensure you keep 50% of your income
    ira_savings += expected_savings - ira_added
    ira *= (1 + ex_ira)
    ira += ira_added
    ira_df = ira_df.append(pd.DataFrame([[year, iter_payments, ira_savings, ira, asset_apr]],\
                        columns=ira_df.columns))
    iter_payments *= (1 + loans['interest'])

    while iter_payments > 0:
        year += 1
        iter_payments *= (1 + loans['interest'])
        ### WITHOUT IRA ###
        asset_apr *= (1 + assets['interest'])
        normal_savings += income['total_income'] - expenses['total_exp'] \
                        - loans['pi']
        iter_payments -= loans['pi']
        #print(iter_payments)

        normal_df = normal_df.append(pd.DataFrame([[year, iter_payments, normal_savings, asset_apr]],\
                            columns=normal_df.columns))
        ### WITH IRA ###
        expected_savings = income['total_income'] - expenses['total_exp'] \
                        - loans['pi']
        ira_added = min(expected_savings/2, 5500) ### To ensure you keep 50% of your income
        ira_savings += expected_savings - ira_added
        ira *= (1 + ex_ira)
        ira += ira_added
        ira_df = ira_df.append(pd.DataFrame([[year, iter_payments, ira_savings, ira, asset_apr]],\
                            columns=ira_df.columns))
    return(normal_df, ira_df)














''''''
