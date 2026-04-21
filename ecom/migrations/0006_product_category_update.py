from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0005_feedback_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('RACEBOY', 'Raceboy Termékek'), ('ESCOBAR', 'Escobar Termékek'), ('KOZOS', 'Közös Termékek')], default='KOZOS', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=160),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=80),
        ),
    ]
