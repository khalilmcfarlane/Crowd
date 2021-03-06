from google.cloud import datastore


def get_client():
    return datastore.Client()

def create_post():
    client = get_client()
    key = client.key('post')
    return datastore.Entity(key)

class PostsManager():
     def __init__(self):
        self.countOfPosts = 0

     def find_post(self, title):
         """Queries for post by title"""
         client = get_client()         
         query = client.query(kind='post')
         query.add_filter("title", "=", title)
         post = None
         for entity in query.fetch():
             post = entity
         return post

     def store_post(self, title, article, username, tag):
        """Stores new posts"""
        blog = create_post()
        self.countOfPosts = self.countOfPosts + 1
        blog['title'] = title
        blog['article'] = article
        blog['username'] = username
        blog['tag'] = tag 
        #print(username)
        client = get_client()
        client.put(blog)

     def return_posts(self):
        client = get_client()
        query = client.query(kind='post')
        
        defaultPost = {}
        defaultsPosts = []
        if self.countOfPosts == 0:
            defaultPost['article'] = 'No posts yet'
            defaultPost['username'] = 'n/a'
            defaultPost['title'] = 'no title'
            defaultPost['tag'] = 'other'
            defaultsPosts.append(defaultPost)
            return defaultsPosts
        
        posts = list(query.fetch())
        return posts
        
     def query_post_by_username(self, username):
          """Queries for all posts from specific user"""
          client = get_client()         
          query = client.query(kind='post')
          query.add_filter("username", "=", username)
          post = list(query.fetch())
          return post              

    
     def store_user(self, username):
        """Associates user with post: Used when user needs to see all posts"""
        blog = create_post()
        blog['username'] = username
        client = get_client()
        client.put(blog)

     def query_posts(self):

        '''Generic post query function'''

        client = get_client()

        query = client.query(kind='post')

        post = list(query.fetch())

        return post

     def query_post_by_title(self, title):

        """Queries for post by title"""

        client = get_client()        

        query = client.query(kind='post')

        query.add_filter("title", "=", title)

        post = None

        for entity in query.fetch():

            post = entity

        return post
        
