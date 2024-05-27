from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(max_length=10, choices=GENDER, null=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=200, null=True, blank=True)
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    CATEGORY = (
        ('Elementary', 'Elementary'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
    )
    title = models.CharField(max_length=50, null=True)
    content = models.TextField(null=True)
    category = models.CharField(max_length=50, null=True, choices=CATEGORY)
    image = models.ImageField(null=True, blank=True)
    account = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title
    
    def like_count(self):
        return Like.objects.filter(post=self).count()
    def comment_count(self):
        return Comment.objects.filter(post=self).count()
    
class Comment(models.Model):
    STATUS = (
        ('Good', 'Good'),
        ('Bad', 'Bad'),
    )
    post = models.ForeignKey(Post, null=True, on_delete= models.SET_NULL)
    account = models.ForeignKey(Account, null=True, on_delete= models.SET_NULL)
    note = models.CharField(max_length=1000, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.note
    
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.account.name
    
    class Meta:
        unique_together = ('post', 'account')
    
class Follow(models.Model):
    following = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, related_name="following")
    follower = models.ForeignKey(Account, null=True, on_delete=models.CASCADE, related_name="follower")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f"{self.follower.name} followed post {self.following.id}"
    
class Setting(models.Model):
    account = models.OneToOneField(Account, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    value = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    sender = models.ForeignKey(Account, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Account, related_name='received_messages', on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Message from {self.sender} to {self.receiver} at {self.timestamp}'

class Comment_Like(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.account.name
    
    class Meta:
        unique_together = ('comment', 'account')    