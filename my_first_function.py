# %% def connect_to_api(url:str):
import logging
import time

logging.getLogger().setLevel(logging.DEBUG)

a_list = ['1', '2', 3, '4', '5']

# %%
for i in a_list:
    try:
        logging.info("Count: " + i)
    except Exception as e:
        logging.error(e)
        continue

print("code done")
# %%

# %%
