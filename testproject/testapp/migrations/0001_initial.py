# Generated by Django 2.1.2 on 2018-10-10 03:57

import django.contrib.postgres.indexes
from django.db import migrations, models
import django_pgtree.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TestModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tree_path", django_pgtree.fields.LtreeField()),
                ("name", models.CharField(max_length=128)),
            ],
            options={"abstract": False},
        ),
        migrations.AddIndex(
            model_name="testmodel",
            index=django.contrib.postgres.indexes.GistIndex(
                fields=["tree_path"], name="tree_path_idx"
            ),
        ),
    ]
