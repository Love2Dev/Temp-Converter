user_temp = input('Please enter a temperature: ').lower()

just_num_of_temp = int((user_temp[0:len(user_temp)-1]))

def calculate_temp():
    if 'c' in user_temp:
        print(
            "The temp in F is: " + str(((9 * just_num_of_temp) + 160) / 5)
        )
    elif 'f' in user_temp:
        print(
            "The temp in C is: " + str(((5 * just_num_of_temp) - 160) / 9)
        )

calculate_temp()



