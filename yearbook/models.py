from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    default_user_per_department = models.ForeignKey(
        "UserPerDepartment",
        null=True,
        on_delete=models.SET_NULL,
        related_name="user_default_department",
    )
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
    )


class CustomFile(models.Model):
    original_file = models.FileField()


class Department(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.deletion.CASCADE)
    name = models.CharField(max_length=140)
    join_password = models.CharField(null=True, max_length=50)
    is_join_allowed = models.BooleanField(default=True)
    avatar = models.ForeignKey(CustomFile, null=True, on_delete=models.SET_NULL)


class UserPerDepartment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    avatar = models.ForeignKey(CustomFile, null=True, on_delete=models.SET_NULL)
    nickname = models.CharField(max_length=50, null=True)
    bio = models.CharField(max_length=140, null=True)

    class Meta:
        unique_together = (("user", "department"),)


# class Topic(models.Model):
#     title = models.CharField()
#     department = models.ForeignKey(Department)


# class TopicVote(models.Model):
#     # add limit on number of votes
#     topic = models.ForeignKey(Topic)
#     user_per_department = models.ForeignKey(UserPerDepartment)
#     voter = models.ForeignKey(UserPerDepartment)


# class Comment(models.Model):
#     text = models.CharField()
#     writer = models.ForeignKey(UserPerDepartment)
#     supper_comment = models.ForeignKey("Comment", null=True)


# class CommentFiles(models.Model):
#     comment = models.ForeignKey(Comment)
#     file = models.ForeignKey(CustomFile)


# class Memorial(models.Model):
#     # can be changed to support several anonymous_comment and not_anonymous_comment
#     anonymous_comment = models.ForeignKey(Comment)
#     not_anonymous_comment = models.ForeignKey(Comment)
#     writer = models.ForeignKey(UserPerDepartment)
#     recipient = models.ForeignKey(UserPerDepartment)
#     department = models.ForeignKey(Department)


# class Memory(models.Model):
#     title = models.CharField()
#     is_private = models.BooleanField()
#     writer = models.ForeignKey(UserPerDepartment)
#     department = models.ForeignKey(Department)
#     base_comment = models.ForeignKey(Comment)


# class TagedUsers(models.Model):
#     Comment = models.ForeignKey(Comment)
#     user_per_department = models.ForeignKey(UserPerDepartment)


# class Reminder(models.Model):
#     user_per_department = models.ForeignKey(UserPerDepartment)
#     # can be changed to add words instead of text
#     text = models.CharField()
