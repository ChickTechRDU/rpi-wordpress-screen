import requests
import datetime
import time

class Blog:

   def __init__(self, url):
        self.url = url

   def has_anything_new_been_posted_yet(self):
       polling = True
       while polling:
        response = requests.get(self.url + "/comments", params={"post": 1, "per_page": 1})
        current_timestamp = datetime.datetime.fromtimestamp(0)
        print("current timestamp before ",current_timestamp)
        most_recent_post = datetime.datetime.fromisoformat(response.json()[0]['date'])
        if most_recent_post > current_timestamp:
           current_timestamp =  most_recent_post
           print("a new post just came up on ",self.url, "at ",current_timestamp)
           polling = False
        else:
            polling = True
        time.sleep(3)

blog_urls = {
    "Alec's blog": "http://demo.wp-api.org/wp-json/wp/v2",
    "Dustin's blog": "http://demo.wp-api.org/wp-json/wp/v2"
    }

blog = Blog(blog_urls.get("Alec's blog"));
blog.has_anything_new_been_posted_yet()
