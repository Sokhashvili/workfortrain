class User:
    def __init__(self, username):
        self.username = username
        self.posts = []
        self.friends = set()

    def create_post(self, content):
        post = Post(content, self)
        self.posts.append(post)
        return post

    def comment_on_post(self, post, content):
        comment = Comment(content, self)
        post.add_comment(comment)
        return comment

    def like_post(self, post):
        post.add_like(self)

class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.comments = []
        self.likes = []

    def add_comment(self, comment):
        self.comments.append(comment)

    def add_like(self, user):
        self.likes.append(user)

class Comment:
    def __init__(self, content, author):
        self.content = content
        self.author = author


user1 = User('User1')
user2 = User('User2')

user1.friends.add(user2)
user2.friends.add(user1)

post1 = user1.create_post('world is mine!')
comment1 = user2.comment_on_post(post1, 'Antonio Montana =D')
user1.like_post(post1) 

post2 = user1.create_post('keep it quiet.')
user2.like_post(post2)  


print("User1's posts:")
for post in user1.posts:
    print("Post:", post.content)
    print("Likes:", len(post.likes))
    print("Comments:")
    for comment in post.comments:
        print("- Comment:", comment.content, "by", comment.author.username)
    print()
    
print("User2's posts:")
for post in user2.posts:
    print("Post:", post.content)
    print("Likes:", len(post.likes))
    print("Comments:")
    for comment in post.comments:
        print("- Comment:", comment.content, "by", comment.author.username)
    print()