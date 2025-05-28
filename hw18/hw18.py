from sfarm_hw import submit_to_api
from one import year_rainfall
from two import year_max_temp
from three import temp_diff
from four import dif_total_rainfall



def main():
    name = "김건우"
    affiliation = "스마트팜학과"
    student_id = "202112855"

    answer1 = year_rainfall()
    answer2 = year_max_temp()
    answer3 = temp_diff()
    answer4 = dif_total_rainfall()


    submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=True)


if __name__ == "__main__":
    main()