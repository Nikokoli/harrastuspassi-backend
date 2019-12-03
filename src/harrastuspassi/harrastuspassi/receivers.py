
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from harrastuspassi.models import Hobby, Municipality
from harrastuspassi import tasks


@receiver(post_save, sender=Hobby)
def hobby_post_save(sender, instance, **kwargs):
    tasks.update_hobby_permissions(instance.pk)


@receiver(m2m_changed, sender=Municipality.moderators.through)
def municipality_moderators_change(sender, instance, action, reverse, pk_set, **kwargs):
    if action == 'post_add' or action == 'post_remove':
        if reverse:
            user_ids = [instance.pk]
        else:
            user_ids = list(pk_set)
        tasks.update_user_hobby_permissions(user_ids)