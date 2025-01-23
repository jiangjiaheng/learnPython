try:
    user_weight = float(input("input your weight (kg) "))
    user_height = float(input("input your height (m) "))
    user_BMI = user_weight / user_height ** 2
except ValueError:
    print("your input is inval")
# except ZeroDivisionError:
#     print("don't input zeo")
except:
    print("something bad happened")
else:
    print("your BMI is " + str(user_BMI))
finally:
    print("game over")
