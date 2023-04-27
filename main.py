def display_main_menu():
    print ("Enter some numbers separated by commas (eg. 5 ,67 ,32)")

def get_user_inputs():
    temp1 = input('numbers: ').split(",")
    yes = [float(x) for x in strings]
    return yes

def calc_average_temperature(temp):
    avg = sum(temp) / len(temp)
    print (avg)
def calc_min_max_temperature(temp):
    min_temp = min(temp)
    max_temp = max(temp)
    print(min_temp, max_temp)


def main():
   display_main_menu()
   get_user_inputs()
   calc_min_max_temperature()
   calc_average_temperature()






