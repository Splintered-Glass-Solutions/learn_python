# %%
import requests

# %%
url = "https://catfact.ninja/fact"
r = requests.get(url)
fact = r.json()['fact']
print(fact)

# %%
