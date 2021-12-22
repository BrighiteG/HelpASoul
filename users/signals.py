# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from .models import Profile
#
#
# def create_profile(sender, instance, created, **kwargs):
#     print('signal triggered')
#     if created:
#         user = instance
#         profile = Profile.objects.create(
#             user=user
#         )
#
#
# def delete_profile(sender, instance, **kwargs):
#     user = instance.user
#     user.delete()
#
#
# post_save.connect(create_profile, sender=User)
# post_delete.connect(delete_profile, sender=Profile)
