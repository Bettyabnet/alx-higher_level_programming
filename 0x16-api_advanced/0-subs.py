
#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Apple' +
        'WebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.3666666'    }
    r = requests.get('https://www.reddit.com/r/{:}/about.json'.format(
        subreddit), headers=headers, allow_redirects=False)
    if r.status_code >= 300:
        return 0
    json = r.json()
    data_dict = json.get('data')
    return(data_dict.get('subscribers'))
