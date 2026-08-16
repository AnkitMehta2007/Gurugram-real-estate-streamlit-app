import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "https://www.google.com/search?q="

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def get_coordinates(sector):

    search_term = f"sector {sector} gurgaon longitude latitude"

    response = requests.get(
        BASE_URL + search_term,
        headers=HEADERS
    )

    if response.status_code == 200:

        soup = BeautifulSoup(response.content, "html.parser")

        coordinates_div = soup.find(
            "div",
            class_="Z0LcW t2b5Cf"
        )

        if coordinates_div:
            return coordinates_div.text

    return None


df = pd.DataFrame(
    columns=["Sector", "Coordinates"]
)


for sector in range(1, 116):

    coordinates = get_coordinates(sector)

    df.loc[len(df)] = [
        f"Sector {sector}",
        coordinates
    ]


df.to_csv(
    "gurgaon_sectors_coordinates.csv",
    index=False
)

