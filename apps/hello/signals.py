from apps.hello.models import Action
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver(post_save)
def log_save(sender, **kwargs):
    if type(kwargs['instance']) is Action:
        return False
    action = 'update' if not kwargs['created'] else 'save'
    Action.objects.create(model=str(sender._meta),
                          instance=kwargs['instance'].pk, action=action)


@receiver(post_delete)
def log_delete(sender, **kwargs):
    if type(kwargs['instance']) is Action:
        return False
    Action.objects.create(model=str(sender._meta),
                          instance=kwargs['instance'].pk, action='delete')
