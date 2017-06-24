from django.test import TestCase
from .models import Comment, Like 
from posts.models import Post
from django.contrib.auth.models import User

class CommentTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="test_user")
        self.post = Post.objects.create(title='Test Post', body='test content', user=self.user)
        self.comment = Comment.objects.create(body="test comment", post=self.post, user=self.user)

    def test_post_has_comment(self):
        self.assertIn(self.comment, self.post.comment_set.all()) 
    
    def test_post_has_comments(self):
        comment2 = Comment.objects.create(body="test comment 2", post=self.post, user=self.user)
        commentsList = [self.comment, comment2]
        allCommentsInList = True

        for comment in commentsList:
            if comment not in self.post.comment_set.all():
                allCommentsInList = False
        
        self.assertTrue(allCommentsInList)

class LikeTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="test_user")
        self.post = Post.objects.create(title='Test Post', body='test content', user=self.user)
        self.liker1 = User.objects.create(username="liker1")
        self.like = Like.objects.create(post=self.post, liker=self.liker1)

    def test_post_has_like(self):
        self.assertIn(self.like, self.post.like_set.all())
    
    def test_post_has_likes(self):
        liker2 = User.objects.create(username="liker2")
        like2 = Like.objects.create(post=self.post, liker=liker2)
        
        likesList = [self.like, like2]
        allLikesInList = True

        for like in likesList:
            if like not in self.post.like_set.all():
                allLikesInList = False

        self.assertTrue(allLikesInList)

    

