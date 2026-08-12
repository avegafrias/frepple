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
    dependencies = [
        ("database_PIL", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="weight",
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name="productdependency",
            name="quantity",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="operationdependency",
            name="quantity",
            field=models.IntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name="productionsprint",
            unique_together={("start_date", "end_date", "production_floor")},
        ),
        migrations.AddField(
            model_name="workorder",
            name="order_entry",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="database_PIL.orderentry",
            ),
        ),
    ]
