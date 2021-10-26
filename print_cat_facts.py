import requests
import time
import traceback2 as traceback


def print_cat_fact(mode: str, i: int, sleep: int = 3):
    try:
        url = "https://catfact.ninja/fact"
        r = requests.get(url)
        fact = r.json()['fact']
        time.sleep(sleep)
        if mode == 'print':
            print(f"{i}: {fact}")
        else:
            return fact
    except Exception as e:
        print(e)
        print(traceback.format_exc())
