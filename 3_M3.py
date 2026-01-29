gender = input("Enter your gender (male/female):") . lower()
hb_value = float(input("Enter your hemoglobin value (g/l) :"))
if gender == "male":
    if hb_value < 134:
        print("Your hemoglobin value is low")
    elif 134 <= hb_value <= 167:
        print("Your hemoglobin value is normal")
    else:
        print("Your hemoglobin value is high")
elif gender == "female":
    if hb_value < 117:
        print("Your hemoglobin value is low")
    elif 117 <= hb_value <= 155:
        print("your hemoglobin value is normal")
    else:
        print("Your hemoglobin value is high")
else:
    print("Invalid gender entered ")
