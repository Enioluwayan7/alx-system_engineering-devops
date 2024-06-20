#!/usr/bin/python3
""" Uses Reddit API to get all hot posts"""

import requests

def recurse(subreddit, hot_list=None, after=None):

    if hot_list is None:
        hot_list = []

    # Define the base URL and the headers for the Reddit API request
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'python:recurse.hot.articles:v1.0 (by /u/your_username)'}
    params = {'after': after}  # Add pagination parameter

    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        # Check if the response is valid and the subreddit exists
        if response.status_code != 200:
            return None

        # Parse the JSON response
        data = response.json()

        # Extract the list of posts
        posts = data['data']['children']

        # Append the titles of the hot posts to hot_list
        for post in posts:
            hot_list.append(post['data']['title'])

        # Get the next 'after' value for pagination
        after = data['data']['after']

        # If there is no next page, return the accumulated list
        if after is None:
            return hot_list

        # Recursive call to get the next page of results
        return recurse(subreddit, hot_list, after)
    except Exception as e:
        # Return None in case of any exception (network issues, etc.)
        return None

# Example usage:
titles = recurse('python')
if titles is not None:
    for title in titles:
        print(title)
else:
    print(None)
