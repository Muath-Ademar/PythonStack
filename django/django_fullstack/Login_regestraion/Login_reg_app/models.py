from django.db import models

import re
class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
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

        
        return errors

class Registration(models.Model):
    first_name = models.CharField(max_length=45)
    Last_name = models.CharField(max_length=45)
    email= models.CharField(max_length=45)
    password = models.CharField(max_length=62)
    CMpassword = models.CharField(max_length=62)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()
