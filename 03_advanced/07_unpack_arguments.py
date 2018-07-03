
"""
Unpacking arguments is all about passing parameters to a function in many ways
"""


def health_calc(age, apples_ate, cigs_smoked):
    answer = (100-age) + (apples_ate * 3.5) - (cigs_smoked) * 2
    print(answer)


data1 = [25, 20, 6]
health_calc(data1[0],data1[1],data1[2])  # This works but takes a lot of code for bigger data
health_calc(*data1)                      # This is how we pass the data all at once and is called unpacking


# Output is gonna be the same