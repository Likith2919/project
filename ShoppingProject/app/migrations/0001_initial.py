# Generated by Django 3.1.5 on 2021-03-09 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Andra Pradesh ', 'Andra Pradesh '), ('Arunachal Pradesh ', 'Arunachal Pradesh '), ('Assam ', 'Assam '), ('Bihar ', 'Bihar'), ('Chandigarh ', 'Chandigarh'), ('Chattisgarh ', 'Chattisgarh'), ('Dadra & Nagar Haveli ', 'Dadra & Nagar Haveli'), ('Daman & Diu ', 'Daman & Diu'), ('Delhi  ', 'Delhi '), ('Gujarat ', 'Gujarat'), ('Haryana ', 'Haryana'), ('Himachal Pradesh ', 'Himachal Pradesh'), ('Jammu & Kashmir ', 'Jammu & Kashmir'), ('Jharkhand ', 'Jharkhand'), ('Karnataka ', 'Karnataka'), ('Kerala ', 'Kerala'), ('Lakshadweep ', 'Lakshadweep'), ('Madhya Pradesh ', 'Madhya Pradesh'), ('Maharastra ', 'Maharastra'), ('Manipur ', 'Manipur'), ('Meghalaya ', 'Meghalaya'), ('Mizoram ', 'Mizoram'), ('Nagaland ', 'Nagaland'), ('Odisha ', 'Odisha'), ('Puducherry ', 'Puducherry'), ('Punjab ', 'Punjab'), ('Rajasthan ', 'Rajasthan'), ('Sikkim ', 'Sikkim'), ('Tamil Nadu ', 'Tamil Nadu'), ('Telangana ', 'Telangana'), ('Tripura ', 'Tripura'), ('Uttarakhand ', 'Uttarakhand'), ('Utter Pradesh ', 'Utter Pradesh'), ('West Bengal ', 'Wesh Bengal')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('brand', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptop'), ('TW', 'Top Wear'), ('BW', 'Bottom Wear')], max_length=2)),
                ('product_image', models.ImageField(upload_to='productimg')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('orderd_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='Pending', max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
