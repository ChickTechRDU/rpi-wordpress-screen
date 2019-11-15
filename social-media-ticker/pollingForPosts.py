from datetime import datetime
import time
import requests

class Blog:

    def __init__(self, url):
        self.base_url = url

    def list_latest_posts(self, at_most):
        response = requests.get(self.base_url + "/posts", params={"per_page": at_most})
        return response.json()

    def list_comments_on_post(self, post_id, at_most):
        response = requests.get(self.base_url + "/comments", params={"post": post_id, "per_page": at_most})
        return response.json()

    def total_comments(self):
        response = requests.get(self.base_url + "/comments", params={"per_page": 1})
        return int(response.headers['X-WP-Total'])

    def comment_on_post(self, post_id, comment_to_post):
        url = (self.base_url + '/comments')
        data = {
            'post': post_id,
            'author_name': 'Your name',
            'author_email': 'YourEmail@gmail.com',
            'content': comment_to_post
        }
        print("Making a POST request to URL: {}".format(url))
        response = requests.post(url, data)
        return response.content


blog = Blog("http://dminnich.example.com/wp-json/wp/v2")
# This is a programming trick that is pretty handy. It turns out that most
# machines increment time forward from a 0-point, and that 0-point is not too far
# in the past, by and large.
#
last_commented_date = datetime.utcnow()

while True: # run forever until we kill the program
    posts = blog.list_latest_posts(at_most=1)
    if len(posts) > 0:
        latest_post = posts[0]
        latest_post_date = latest_post['date']
        post_date = datetime.fromisoformat(latest_post_date)
        if post_date > last_commented_date:
            last_commented_date = post_date
            print("a new post just came up on ", blog.base_url, "at ", last_commented_date)
            blog.comment_on_post(latest_post['id'],"Hello there, do you want to be my friend!")
    time.sleep(3) # wait 3s before doing anything else.
