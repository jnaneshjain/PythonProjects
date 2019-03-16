has_high_income = True
has_good_credit = False
has_criminal_record = True

if has_good_credit and has_high_income:
    print("Eligible for loan")
if has_good_credit or has_high_income:
    print("Eligible for loan")
if has_good_credit and has_high_income and not has_criminal_record:
    print("Eligible for loan")