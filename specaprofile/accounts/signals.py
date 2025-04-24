from django.db.models.signals import post_save,m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User

from accounts.models import Profile,Website

@receiver(post_save, sender=User)
def creating_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(m2m_changed, sender=Website.users.through)
def edit_biography_m2m(sender, instance, action, reverse, **kwargs):
    if action in ['post_add', 'post_remove']:
        if reverse:
            user = instance
            profile = Profile.objects.get(user=user)
            website_urls = sorted([website.url for website in user.website_set.all()])
            profile.bio = "\n".join(website_urls)
            profile.save()
        else:
            users = instance.users.all()
            for user in users:
                profile = Profile.objects.get(user=user)
                website_urls = sorted([website.url for website in user.website_set.all()])
                profile.bio = "\n".join(website_urls)
                profile.save()