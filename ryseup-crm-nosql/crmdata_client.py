import os

import click
import requests

@click.command()
@click.option("--userdata", default="Friend")
def get_user_data(name):
    headers = {"X-Github-Token": os.eviron.get("CRMDATA_GITHUB_TOKEN")}
    url = f"https://redesigned-funicular-v6vrxqq4qxq4hw9q4-7071.app.github.dev/api/crmdata?name=[firstname]"
    data = requests.get(url).json()
    print(data[name])

if __name__ == "__main__":
    get_user_data()