from django.db import models
from datetime import datetime
import re
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first'])<2:
            errors['first'] = "first name must be at least 2 characters "
        if len(postData['last']) <2:
            errors['last'] = "last name must be at least 2 characters"
        if not EMAIL_REGEX.match(postData["email"]):
            errors['email'] = "invalid email adress"
        if len(postData['password']) < 8:
            errors['password'] = "invalid password"
        if postData['password'] != postData['CMpassword']:
            errors['password'] = "passwords dont match"
        return errors
        
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = created_at = models.DateTimeField(auto_now_add=True)
    updated_at = updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    
class Message(models.Model):
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    message = models.TextField()
    created_at = created_at = models.DateTimeField(auto_now_add=True)
    updated_at = updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE )
    message = models.ForeignKey(Message, related_name="message_comments", on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = created_at = models.DateTimeField(auto_now_add=True)
    updated_at = updated_at = models.DateTimeField(auto_now=True)