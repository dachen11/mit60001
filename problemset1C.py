def find_monthly_savings():
    annual_salary = float(input("Please enter your annual salary: "))
    a = annual_salary
    portion_down_payment = 250000
    r = .04
    steps = 0
    if (annual_salary * 38.1/12) < portion_down_payment:
        print("It is not possible to pay the down payment in three years.")
    else:
        low = 0.0
        high = 1.0
        guess = .5
        while high - low >= .0003:
            steps = steps + 1
            current_savings = 0
            annual_salary = a
            for i in range(35):
                if i % 6 == 0 and i != 0:
                    annual_salary = 1.07 * annual_salary
                current_savings = current_savings + (guess * annual_salary/12) + (current_savings * r/12)
            if (current_savings == portion_down_payment):
                break
            elif (current_savings < portion_down_payment):
                low = guess
                guess = guess + ((high - guess)/2)
            else:
                high = guess
                guess = guess - ((guess - low)/2)
        print("Best savings rate: " + str(float(int(guess * 10000)/10000)))
        print("Steps taken: " + str(steps))
find_monthly_savings()
