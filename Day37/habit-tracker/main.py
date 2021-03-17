import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
username = "worldcole"
token = "buJJINn890YonT"
user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# TODO 1: Creates a username in pixela and gives back the response as a piece of text. We perform this code once

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_id = "graph1"
graph_config = {
    "id": graph_id,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "int",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": token
}

# TODO 2: Creates a graph and checks if its successfully posted
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now().strftime("%Y%m%d")
yesterday = datetime(year=2021, month=3, day=16).strftime("%Y%m%d")
post_endpoint = f"{graph_endpoint}/{graph_id}"
post_parameters = {
    "date": f"{today}",
    "quantity": input("How many hours did you code today?"),
}

# TODO 3: Creates a pixel
response = requests.post(url=post_endpoint, json=post_parameters, headers=headers)
print(response.text)

delete_endpoint = f"{post_endpoint}/20200317"
# TODO 4: Delete a post
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

# TODO 5: Update a post

update_endpoint = f"{post_endpoint}/{today}"
update_config = {
    "quantity": "16"
}
# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)
