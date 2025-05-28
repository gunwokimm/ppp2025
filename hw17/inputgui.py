from answerone import get_2015_rainfall
from answertwo import get_top_weather
from answerthr import get_max_gap
from answerfour import get_rainfall_difference
from rich import print


def main():
    answer1 = get_2015_rainfall()
    answer2 = get_top_weather()
    answer3 = get_max_gap()
    answer4 = get_rainfall_difference()

    
    print(f"[bold blue]{answer1} :umbrella:")
    print(f"[bold yellow]{answer2} :sun_behind_cloud:")
    print(f"[bold red]{answer3} :zap:")
    print(f"[bold cyan]{answer4} :droplet:")
    


if __name__ == "__main__":
    main()

