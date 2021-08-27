from django.db import models


class CustomUser(models.Model):
    firstName = models.CharField()
    lastName = models.CharField()
    email = models.CharField()
    activated = models.CharField()
    langKey = models.CharField()
    phone = models.CharField()
    defaultUserPerDepartment = models.ForeignKey('IUserPerDepartment')


class CustomFile(models.Model):
    original_file = models.FileField()


class Department(models.Model):
    name = models.CharField()
    password = models.CharField()
    avatar = models.ForeignKey(CustomFile)
    owner = models.ForeignKey(CustomUser)


class UserPerDepartment(models.Model):
    user = models.ForeignKey(CustomUser)
    nickname = models.CharField()
    bio = models.CharField()
    avatar = models.ForeignKey(CustomFile)
    department = models.ForeignKey(Department)


class Topic(models.Model):
    title = models.CharField()
    department = models.ForeignKey(Department)


class TopicVote(models.Model):
    topic = models.ForeignKey(Topic)
    user_per_department = models.ForeignKey(UserPerDepartment)
    voter = models.ForeignKey(UserPerDepartment)


class Memory(models.Model):
    title = models.CharField()
    is_private = models.BooleanField()
    writer = models.ForeignKey(UserPerDepartment)
    # tageds = models.ForeignKey(UserPerDepartment)
    department = models.ForeignKey(Department)


class Comment(models.Model):
    text = models.CharField()
    # pictures several custom file
    writer = models.ForeignKey(UserPerDepartment)
    memory = models.ForeignKey(Memory)
    base_comment = models.ForeignKey('Comment')


class Memorial(models.Model):
    anonymousComment = models.ForeignKey(Comment)
    notAnonymousComment = models.ForeignKey(Comment)
    writer = models.ForeignKey(UserPerDepartment)
    recipient = models.ForeignKey(UserPerDepartment)
    department = models.ForeignKey(Department)
