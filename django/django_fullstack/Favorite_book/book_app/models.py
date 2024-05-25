from django.db import models

import re
class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first']) < 2:
            errors["first"] = "User first name should be at least 2 characters"
        if len(postData['last']) < 2:
            errors["last"] = "User last name should be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']): 
            errors['email'] = "invalid email address"
        if len(postData['password']) < 8:
            errors['password'] = 'password should be at least 8 characters'
        postData['password']
        if len(postData['conform']) < 8:
            errors['conform'] = 'should be at least 8 charecters'
        if postData['password'] != postData['conform']:
            errors['password'] = 'the password does not match the conform password section'
            errors['conform'] = 'the password does not match the conform password section'
        if len(postData['desc']) < 5:
            errors['desc'] = 'Description must be at least 5 charecters'
        if len(postData['title']) == 0:
            errors['title'] = 'Title is required'
        return errors

class bookManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['desc']) < 5:
            errors['desc'] = 'Description must be at least 5 charecters'
        if len(postData['title']) == 0:
            errors['title'] = 'Title is required'
        return errors
    
class User(models.Model):
    first_name = models.CharField(max_length=45)
    Last_name = models.CharField(max_length=45)
    email= models.CharField(max_length=45)
    password = models.CharField(max_length=62)
    CMpassword = models.CharField(max_length=62)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="users", on_delete=models.CASCADE, null=True)
    users = models.ManyToManyField(User, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = bookManager()

