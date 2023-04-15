from levels_functions import *
if __name__ == '__main__':

    pass_level = run_first_level()
    if pass_level == 1:
        pass_second_level = run_second_level()
        if pass_second_level == 1:
            third_level = run_third_level()
