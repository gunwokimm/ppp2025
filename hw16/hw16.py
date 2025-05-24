from sfarm_hw import submit_to_api
from answerone import get_2015_rainfall
from answertwo import get_top_weather
from answerthr import get_max_gap
from answerfour import get_rainfall_difference

def main():
    name = "김건우"
    affiliation = "스마트팜학과"
    student_id = "202112855"

    answer1 = get_2015_rainfall()
    answer2 = get_top_weather()
    answer3 = get_max_gap()
    answer4 = get_rainfall_difference()

    submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=True)


if __name__ == "__main__":
    main()