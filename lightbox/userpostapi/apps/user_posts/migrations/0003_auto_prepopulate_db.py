# migrations/0003_auto_prepopulate_db.py

from django.db import migrations

def populate_database(apps, schema_editor):
    # Import your models dynamically to avoid circular dependencies
    # User = apps.get_model('user_posts', 'User')  # Example: replace with your model
    #
    # # Create or prepopulate data
    # if not User.objects.exists():  # Prevent duplicate entries
    #     User.objects.create(name='John Doe', email='john@example.com')
    #     User.objects.create(name='Jane Smith', email='jane@example.com')

    from django.core.management import call_command
    call_command('loaddata', 'all_app_data.json')  # Ensure the fixture is in the correct folder



def reverse_populate_database(apps, schema_editor):
    User = apps.get_model('user_posts', 'User')
    User.objects.all().delete()  # Remove the prepopulated data if rolling back

class Migration(migrations.Migration):

    dependencies = [
        ('user_posts', '0002_rename_username_user_name'),  # Ensure this matches your last migration
    ]

    operations = [
        migrations.RunPython(populate_database, reverse_code=reverse_populate_database),
    ]
