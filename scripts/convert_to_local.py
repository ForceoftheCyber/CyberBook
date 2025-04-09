# Small script for converting download FaceIT-questions

import requests
import json

URL = "https://dev.faceittools.com/questions/fetch_questions_cu/it2901Adaptive"

response = requests.get(URL)

if response.status_code == 204:
    print("error")
elif response.status_code == 200:
    content = response.json()
    
    # Sanity check
    if content["status"] != "success":
        raise RuntimeError("Fetch returned with response code 200, but status in body was not 'success'")
    
    # Also limits questions
    questions = json.loads(content["questions"])

    with open("output.json", "w") as file:
        file.write(content["questions"])