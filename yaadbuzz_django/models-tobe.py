from django.db import models


class CustomUser(models.Model):
    firstName = models.CharField()
    lastName = models.CharField()
    email = models.CharField()
    activated = models.CharField()
    langKey = models.CharField()
    phone = models.CharField()
    default_user_per_department = models.ForeignKey('UserPerDepartment')


class CustomFile(models.Model):
    original_file = models.FileField()


class Department(models.Model):
    base_department = models.ForeignKey('Department', null=True)
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
    # add limit on number of votes
    topic = models.ForeignKey(Topic)
    user_per_department = models.ForeignKey(UserPerDepartment)
    voter = models.ForeignKey(UserPerDepartment)


class Comment(models.Model):
    text = models.CharField()
    writer = models.ForeignKey(UserPerDepartment)
    supper_comment = models.ForeignKey('Comment', null=True)


class CommentFiles(models.Model):
    comment = models.ForeignKey(Comment)
    file = models.ForeignKey(CustomFile)


class Memorial(models.Model):
    # can be changed to support several anonymous_comment and not_anonymous_comment
    anonymous_comment = models.ForeignKey(Comment)
    not_anonymous_comment = models.ForeignKey(Comment)
    writer = models.ForeignKey(UserPerDepartment)
    recipient = models.ForeignKey(UserPerDepartment)
    department = models.ForeignKey(Department)


class Memory(models.Model):
    title = models.CharField()
    is_private = models.BooleanField()
    writer = models.ForeignKey(UserPerDepartment)
    department = models.ForeignKey(Department)
    base_comment = models.ForeignKey(Comment)


class TagedUsers(models.Model):
    Comment = models.ForeignKey(Comment)
    user_per_department = models.ForeignKey(UserPerDepartment)


class Reminder(models.Model):
    user_per_department = models.ForeignKey(UserPerDepartment)
    # can be changed to add words instead of text
    text = models.CharField()
