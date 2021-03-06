# Generated by Django 3.2.8 on 2021-10-16 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('flag', models.ImageField(default='default.jpg', upload_to='Country')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stadium_name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=20)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='venues', to='tournament.country')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(default='default.jpg', upload_to='Team_logo')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='teams', to='tournament.country')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('picture', models.ImageField(default='default.jpg', upload_to='Player_pic')),
                ('dob', models.DateField()),
                ('role', models.CharField(choices=[('Batsman', 'Batsman'), ('Bowler', 'Bowler'), ('All Rounder', 'All Rounder')], default='All Rounder', max_length=11)),
                ('birth_place', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='players', to='tournament.country')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='players', to='tournament.team')),
            ],
        ),
        migrations.CreateModel(
            name='MatchSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('best_fielder', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tournament.player')),
                ('bowler_of_the_match', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='bowler', to='tournament.player')),
                ('man_of_the_match', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='matchsummarys', to='tournament.player')),
                ('match_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchsummarys', to='tournament.match')),
                ('match_looser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.team')),
                ('match_winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchsummarys', to='tournament.team')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchs', to='tournament.team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.team'),
        ),
        migrations.AddField(
            model_name='match',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='matchs', to='tournament.venue'),
        ),
    ]
