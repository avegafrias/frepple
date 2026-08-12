#
# Copyright (C) 2026 by Partes Industriales Laguna
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
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
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "client_pil",
            },
        ),
        migrations.CreateModel(
            name="Operator",
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
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "operator_pil",
            },
        ),
        migrations.CreateModel(
            name="ProductionFloor",
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
                ("description", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "production_floor_pil",
            },
        ),
        migrations.CreateModel(
            name="Operation",
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
                ("description", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "operation_pil",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.CharField(
                        max_length=20, primary_key=True, serialize=False
                    ),
                ),
                ("line", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=255)),
                ("weight", models.IntegerField()),
                ("inventory", models.IntegerField()),
                ("inventory_last_updated", models.DateTimeField()),
            ],
            options={
                "db_table": "product_pil",
            },
        ),
        migrations.CreateModel(
            name="PurchaseOrder",
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
                ("status", models.CharField(max_length=50)),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="database_PIL.client",
                    ),
                ),
            ],
            options={
                "db_table": "purchase_order_pil",
            },
        ),
        migrations.CreateModel(
            name="OrderEntry",
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
                ("quantity", models.IntegerField()),
                (
                    "purchase_order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="database_PIL.purchaseorder",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="database_PIL.product",
                    ),
                ),
            ],
            options={
                "db_table": "order_entry_pil",
            },
        ),
        migrations.CreateModel(
            name="ProductDependency",
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
                ("quantity", models.CharField(max_length=50)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="database_PIL.product",
                    ),
                ),
                (
                    "operation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="database_PIL.operation",
                    ),
                ),
            ],
            options={
                "db_table": "product_dependency_pil",
            },
        ),
        migrations.CreateModel(
            name="OperationDependency",
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
                ("quantity", models.CharField(max_length=50)),
                (
                    "operation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="database_PIL.operation",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="database_PIL.product",
                    ),
                ),
            ],
            options={
                "db_table": "operation_dependency_pil",
            },
        ),
        migrations.CreateModel(
            name="ProductionSprint",
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
                ("start_date", models.DateTimeField()),
                ("end_date", models.DateTimeField()),
                (
                    "production_floor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="database_PIL.productionfloor",
                    ),
                ),
            ],
            options={
                "db_table": "production_sprint_pil",
            },
        ),
        migrations.CreateModel(
            name="ProductionStation",
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
                (
                    "production_floor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="database_PIL.productionfloor",
                    ),
                ),
                (
                    "operation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="database_PIL.operation",
                    ),
                ),
                (
                    "operator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="database_PIL.operator",
                    ),
                ),
            ],
            options={
                "db_table": "production_station_pil",
            },
        ),
        migrations.CreateModel(
            name="OperatorCapacity",
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
                ("capacity", models.IntegerField()),
                (
                    "operator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="database_PIL.operator",
                    ),
                ),
                (
                    "operation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="database_PIL.operation",
                    ),
                ),
            ],
            options={
                "db_table": "operator_capacity_pil",
            },
        ),
        migrations.CreateModel(
            name="WorkOrder",
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
                ("quantity", models.IntegerField()),
                ("status", models.CharField(max_length=50)),
                (
                    "production_station",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="database_PIL.productionstation",
                    ),
                ),
            ],
            options={
                "db_table": "work_order_pil",
            },
        ),
        migrations.CreateModel(
            name="WorkOrderDependency",
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
                (
                    "work_order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dependencies",
                        to="database_PIL.workorder",
                    ),
                ),
                (
                    "needed_work_order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="needed_by",
                        to="database_PIL.workorder",
                    ),
                ),
            ],
            options={
                "db_table": "work_order_dependency_pil",
            },
        ),
        migrations.AlterUniqueTogether(
            name="productionsprint",
            unique_together={("start_date", "end_date")},
        ),
    ]
