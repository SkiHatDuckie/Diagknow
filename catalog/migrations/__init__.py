from django.db import migrations

def create_user(apps, schema_editor):
    patient = apps.get_model('users', 'User')


class Migration(migrations.Migration):
