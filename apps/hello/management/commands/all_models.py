from django.core.management.base import NoArgsCommand
from django.contrib.contenttypes.models import ContentType


class Command(NoArgsCommand):
    help = 'Prints all models and rows'

    def handle_noargs(self, **options):
        for ct in ContentType.objects.all():
            m = ct.model_class()
            self.stdout.write("%s.%s\t%d" % (
                m.__module__, m.__name__, m._default_manager.count()))
            self.stderr.write("error: %s.%s\t%d" % (
                m.__module__, m.__name__, m._default_manager.count()))
