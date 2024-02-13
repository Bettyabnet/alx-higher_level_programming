
#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
  """Returns the number of subscribers for a given subreddit."""
  # Set the base URL and the custom User-Agent
  base_url = "https://www.reddit.com/"
  headers = {"User-Agent": "alx-student"}

  # Make a GET request to the subreddit's about.json endpoint
  response = requests.get(base_url + "r/" + subreddit + "/about.json", headers=headers)

  if response.status_code == 200 and response.headers["content-type"] == "application/json; charset=UTF-8":
    data = response.json()

    if data["kind"] == "t5" and not data["data"]["over18"]:
      return data["data"]["subscribers"]
    else:
      return 0
  else:
    return 0
