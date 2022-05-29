def calc_down_payment():
    annual_salary = float(input("Please enter your annual salary: "))
    portion_saved = float(input("Please enter what percent of your money you would like to save each month: "))
    total_cost = float(input("Please enter the cost of your dream home: "))
    semi_annual_raise = float(input("Please enter your semi-annual salary raise: "))
    portion_down_payment = .25 * total_cost
    current_savings = 0
    r = 0.04
    months = 0
    while current_savings < portion_down_payment:
        if months % 6 == 0 and months != 0:
            annual_salary = annual_salary * (1 + semi_annual_raise)
        current_savings = current_savings + (portion_saved * annual_salary/12) + (current_savings * r/12)
        months = months + 1
    print(months)
calc_down_payment()







