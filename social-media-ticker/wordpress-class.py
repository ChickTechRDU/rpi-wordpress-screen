import requests

# response = requests.get("http://demo.wp-api.org/wp-json/wp/v2/posts", params={'per_page': 4})
# post = response.json()[0]
# print('{0}: {1}'.format(post['date'], post['title']['rendered']))


class Blog:
    """
    Simple Wordpress blog client.
    """

    def __init__(self, url):
        self.url = url

    def get(self, path_template, *args, **kwargs):
        url = (self.url + path_template).format(*args)
        response = requests.get(url, params=kwargs)
        print("Making a GET request to URL: {}".format(response.url))
        return response

    def list_posts(self, per_page=3):
        return self.get("/posts", per_page=per_page).json()

    def list_comments_on_post(self, post_id, per_page=3):
        return self.get("/comments", post=post_id, per_page=per_page).json()


blog = Blog('http://demo.wp-api.org/wp-json/wp/v2')
posts = blog.list_posts(per_page=5)
print([post['title']['rendered'] for post in posts])
print(*[blog.list_comments_on_post(post_id=post['id'], per_page=5)['author_name'] for post in posts], sep='\n')

