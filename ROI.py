
from ast import Break


class Property:
    def __init__(self):
        self.type = ''
        self.price = 0
        self.income = 0
        self.expense = 0
        self.investment = 0
        self.monthly_cashflow = 0
        self.annual_cashflow = 0

    def income_enter(self):
        income_dict = {'1) Rental Income': 0, '2) Laundry': 0, '3) Storage': 0, '4) Miscellaneous': 0}
        while True:
            print("=======================================")
            self.income = sum(income_dict.values())
            print(f"Total Monthly Income: ${self.income}")
            for key, value in income_dict.items():
                print(f"{str(key)}: ${str(value)}")
            selection = input("""
                --- Please select the appropriate number options and enter the data
                or Enter b to go back to the menu ---""")
            if selection.lower() == '1':
                rental_income = int(input('1) Rental Income: $'))
                income_dict['1) Rental Income'] = rental_income
            elif selection.lower() == '2':
                laundry = int(input('2) Laundry: $'))
                income_dict['2) Laundry'] = laundry
            elif selection.lower() == '3':
                storage = int(input('3) Storage: $'))
                income_dict['3) Storage'] = storage
            elif selection.lower() == '4':
                misc = int(input('4) Miscellaneous: $'))
                income_dict['4) Miscellaneous'] = misc
            elif selection.lower() == 'b':
                break
            else:
                print('Error: Please try again. ')

    def expense_enter(self):
        expense_dict = {'1) Taxes':0, '2) Insurance':0, '3) Utilities':0, '4) HOA':0, '5) Lawn/Snow':0, '6) Vacancy':0, '7) Repairs':0, '8) Capex':0, '9) Management':0, '10) Mortgage':0}
        while True:
            print("=======================================")
            self.expense = sum(expense_dict.values())
            print(f"Total Monthly Expense: ${self.expense}")
            for key, value in expense_dict.items():
                print(f"{str(key)}: ${str(value)}")
            selection = input("""
                --- Please select the appropriate number options and enter the data
                or Enter b to go back to the menu ---""")
            if selection == '1':
                taxes = int(input('1) Taxes: $'))
                expense_dict['1) Taxes'] = taxes
            elif selection == '2':
                insurance = int(input('2) Insurance: $'))
                expense_dict['2) Insurance'] = insurance
            elif selection == '3':
                utilities = int(input('3) Utilities: $'))
                expense_dict['3) Utilities'] = utilities
            elif selection == '4':
                hoa = int(input('4) Homeowner Association Fees: $'))
                expense_dict['4) HOA'] = hoa
            elif selection == '5':
                lawn_snow = int(input('5) Lawn/Snow: $'))
                expense_dict['5) Lawn/Snow'] = lawn_snow
            elif selection == '6':
                vacancy = int(input('6) Vacancy: $'))
                expense_dict['6) Vacancy'] = vacancy
            elif selection == '7':
                repairs = int(input('7) Repairs: $'))
                expense_dict['7) Repairs'] = repairs
            elif selection == '8':
                capex = int(input('8) Capital Expenditure (CAPEX): $'))
                expense_dict['8) Capex'] = capex
            elif selection == '9':
                management = int(input('9) Management: $'))
                expense_dict['9) Management'] = management
            elif selection == '10':
                mortgage = int(input('10) Mortgage: $'))
                expense_dict['10) Mortgage'] = mortgage
            elif selection == 'b':
                break
            else:
                print('Error: Please try again. ')

    def cashflow(self):
        self.monthly_cashflow = self.income - self.expense
        self.annual_cashflow = self.monthly_cashflow*12

    def investmenting(self):
        investment_dict = {'1) Down Payment':0, '2) Closing Costs':0, '3) Rehab Budget':0, '4) Miscellaneous/Other':0}
        while True:
            print("=======================================")
            self.investment = sum(investment_dict.values())
            print(f"Total Investment: ${self.investment}")
            for key, value in investment_dict.items():
                print(f"{str(key)}: ${str(value)}")
            selection = input("""
                --- Please select the appropriate number options and enter the data
                or Enter b to go back to the menu ---""")
            if selection == '1':
                down_payment = int(input("1) Down Payment: $"))
                investment_dict['1) Down Payment'] = down_payment
            elif selection == '2':
                closing_costs = int(input("2) Closing Costs: $"))
                investment_dict['2) Closing Costs'] = closing_costs
            elif selection == '3':
                rehab = int(input("3) Rehab Budget: $"))
                investment_dict['3) Rehab Budget'] = rehab
            elif selection == '4':
                misc_other = int(input("4) Miscellaneous/Other: $"))
                investment_dict['4) Miscellaneous/Other'] = misc_other
            elif selection.lower() == 'b':
                break
            else: 
                print("Error: Please try again. ")

    def roi(self):
        self.cashflow()
        ROI = (self.annual_cashflow/self.investment)*100
        print(f"""
        ============================================================
        Summary:
        Property type: {self.type}
        Property price: ${self.price}
        Property investment: ${self.investment}
        Cash on Cash ROI: {ROI}%
        ===============================
        Other important details:
        Total Annual Cashflow: ${self.annual_cashflow}

        Total Monthly Cashflow: ${self.monthly_cashflow}
        Total Monthly Income: ${self.income}
        Total Monthly Expenses: ${self.expense}
        ============================================================
        """)

    def run(self):
        print("Welcome to the Real Estate Cash on Cash ROI Calculator!")
        while True:
            choice = input("""
            Please select a number option and enter information for the following sections:
            1) Property
            2) Income
            3) Expenses
            4) Investment
            When section 1) ~ 4) is completed, 
            Enter 5) to compute ROI or 'q' to quit. 
            """)
            if choice == '1':
                self.type = input("Please enter the property type (e.g. Condo): ").title()
                self.price = input("Please enter the property price: $")
            elif choice == '2':
                self.income_enter()
            elif choice == '3':
                self.expense_enter()
            elif choice == '4':
                self.investmenting()
            elif choice == '5':
                self.roi()
            elif choice.lower() == 'q':
                break
            else:
                print("Error: Please try again.")

my_property = Property()
my_property.run()


