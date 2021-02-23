import requests as re
from tqdm import tqdm


for i in tqdm(range(1000)):

    # Make 1 in 5 requests have bad formatting
    if i % 5 == 1:
        x = "a"
    else:
        x = "1"
    
    # x must be a number, so x = a will return an HTTP 400 error
    
    url = f"http://192.168.1.189:8000/input?device_id=test&temp=1&humid=1&light={x}"
    r = re.post(url)
    