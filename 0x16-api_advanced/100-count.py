#!/usr/bin/python3
import requests
import json

def count_words(subreddit, word_list, after=None, word_counts=None):
    # Initialize word_counts dictionary on the first call
    if word_counts is None:
        word_counts = {word.lower(): 0 for word in word_list}

    # Prepare Reddit API request
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'User-Agent': 'count_words_bot/0.1'}
    params = {'limit': 100}  # Maximum allowed by Reddit API
    if after:
        params['after'] = after

    # Make the request
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # If subreddit is valid and not redirected
    if response.status_code == 200:
        data = response.json()
        articles = data['data']['children']

        # Parse titles and count keywords
        for article in articles:
            title = article['data']['title'].lower()
            for word in word_counts.keys():
                word_counts[word] += title.split().count(word)

        # Continue to the next page recursively
        next_after = data['data']['after']
        if next_after:
            count_words(subreddit, word_list, after=next_after, word_counts=word_counts)

    # Print sorted results
    sorted_results = sorted([(k, v) for k, v in word_counts.items() if v > 0], key=lambda x: (-x[1], x[0]))
    for word, count in sorted_results:
        print(f'{word}: {count}')

# Example usage
count_words('learnprogramming', ['python', 'java', 'javascript', 'c++', 'ruby'])
