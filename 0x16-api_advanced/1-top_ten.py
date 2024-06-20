import requests

def top_ten(subreddit):
    # Define the base URL and the headers for the Reddit API request
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'python:top.ten.hot.posts:v1.0 (by /u/your_username)'}
    
    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response is valid and the subreddit exists
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract the list of posts
            posts = data['data']['children']
            
            # Print the titles of the first 10 hot posts
            for post in posts[:10]:
                print(post['data']['title'])
        else:
            # If the response status is not 200, print None (invalid subreddit)
            print(None)
    except Exception as e:
        # Print None in case of any exception (network issues, etc.)
        print(None)

# Example usage:
top_ten('python')

