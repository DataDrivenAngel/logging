import requests as re
from tqdm import tqdm


for i in tqdm(range(1000)):

    if i % 5 == 1:
        x = "a"
    else:
        x = "1"
    
    url = f"http://192.168.1.189:8000/input?device_id=test&temp=1&humid=1&light={x}"
    r = re.post(url)
    