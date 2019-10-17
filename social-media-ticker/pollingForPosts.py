from datetime import datetime
import time
import requests

class Blog:

    def __init__(self, url):
        self.url = url

    def list_latest_posts(self, at_most):
        response = requests.get(self.url + "/posts", params={"per_page": at_most})
        return response.json()

    def list_comments_on_post(self, post_id, at_most):
        response = requests.get(self.url + "/comments", params={"post": post_id, "per_page": at_most})
        return response.json()

    def total_comments(self):
        response = requests.get(self.url + "/comments", params={"per_page": 1})
        return int(response.headers['X-WP-Total'])

    def comment_on_post(self, post_id, comment_to_post):
        url = (self.url + '/comments')
        data = {
            'post': post_id,
            'author_name': 'Your name',
            'author_email': 'YourEmail@gmail.com',
            'content': comment_to_post
        }
        print("Making a POST request to URL: {}".format(url))
        response = requests.post(url, data)
        return response.content


blog = Blog("http://demo.wp-api.org/wp-json/wp/v2")
last_commented_date = datetime.fromtimestamp(0)

while True:
    posts = blog.list_latest_posts(at_most=1)
    if len(posts) > 0:
        latest_post = posts[0]

        post_date = datetime.fromisoformat(latest_post['date'])
        if post_date > last_commented_date:
            last_commented_date = post_date
            print("a new post just came up on ", blog.url, "at ", last_commented_date)
            blog.comment_on_post(latest_post['id'])
    time.sleep(3)
