import requests


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

    def total_comments(self):
        response = requests.get(self.url + "/comments", params={"per_page": 1})
        return int(response.headers['X-WP-Total'])

    def comment_on_post(self, post_id, comment_to_post):
        url = (self.url + '/comments')
        data = {
            'post':post_id,
            'author_name':'Your name',
            'author_email':'YourEmail@gmail.com',
            'content':comment_to_post
        }
        print("Making a POST request to URL: {}".format(url))
        response = requests.post(url, data)
        return response.content



blog = Blog('http://blog.example.com/wp-json/wp/v2')
posts = blog.list_posts(per_page=1)
print([post['title']['rendered'] for post in posts])
print("😀")
print(
    *[blog.list_comments_on_post(post_id=post['id'], per_page=5) for post in posts],
  sep='\n')

print('Enter your comment')
comment_to_post = input()
print('Posting your comment')
print(
    *[blog.comment_on_post(post_id=post['id'], comment_to_post=comment_to_post) for post in posts],
    sep='\n')


