# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Ride.description_markup_type'
        db.add_column('rides', 'description_markup_type',
                      self.gf('django.db.models.fields.CharField')(default='markdown', max_length=30, blank=True),
                      keep_default=False)

        # Adding field 'Ride._description_rendered'
        db.add_column('rides', '_description_rendered',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Ride.terms_and_conditions_markup_type'
        db.add_column('rides', 'terms_and_conditions_markup_type',
                      self.gf('django.db.models.fields.CharField')(default='markdown', max_length=30, blank=True),
                      keep_default=False)

        # Adding field 'Ride._terms_and_conditions_rendered'
        db.add_column('rides', '_terms_and_conditions_rendered',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


        # Changing field 'Ride.description'
        db.alter_column('rides', 'description', self.gf('markupfield.fields.MarkupField')(null=True, rendered_field=True))

        # Changing field 'Ride.terms_and_conditions'
        db.alter_column('rides', 'terms_and_conditions', self.gf('markupfield.fields.MarkupField')(null=True, rendered_field=True))

    def backwards(self, orm):
        # Deleting field 'Ride.description_markup_type'
        db.delete_column('rides', 'description_markup_type')

        # Deleting field 'Ride._description_rendered'
        db.delete_column('rides', '_description_rendered')

        # Deleting field 'Ride.terms_and_conditions_markup_type'
        db.delete_column('rides', 'terms_and_conditions_markup_type')

        # Deleting field 'Ride._terms_and_conditions_rendered'
        db.delete_column('rides', '_terms_and_conditions_rendered')


        # Changing field 'Ride.description'
        db.alter_column('rides', 'description', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Ride.terms_and_conditions'
        db.alter_column('rides', 'terms_and_conditions', self.gf('django.db.models.fields.TextField')(null=True))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'chapters.chapter': {
            'Meta': {'object_name': 'Chapter', 'db_table': "'chapters'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': "'255'"}),
            'stripe_priv_key': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'stripe_pub_key': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'stripe_test_priv_key': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'stripe_test_pub_key': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'rides.ride': {
            'Meta': {'object_name': 'Ride', 'db_table': "'rides'"},
            '_description_rendered': ('django.db.models.fields.TextField', [], {}),
            '_terms_and_conditions_rendered': ('django.db.models.fields.TextField', [], {}),
            'chapter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chapters.Chapter']", 'null': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'gbp'", 'max_length': '3'}),
            'description': ('markupfield.fields.MarkupField', [], {'null': 'True', 'rendered_field': 'True', 'blank': 'True'}),
            'description_markup_type': ('django.db.models.fields.CharField', [], {'default': "'markdown'", 'max_length': '30', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'end_location': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '6', 'decimal_places': '2'}),
            'rider_capacity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'riders': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['auth.User']", 'null': 'True', 'through': "orm['rides.RideRiders']", 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': "'255'"}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'start_location': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'terms_and_conditions': ('markupfield.fields.MarkupField', [], {'null': 'True', 'rendered_field': 'True', 'blank': 'True'}),
            'terms_and_conditions_markup_type': ('django.db.models.fields.CharField', [], {'default': "'markdown'", 'max_length': '30', 'blank': 'True'})
        },
        'rides.rideriders': {
            'Meta': {'object_name': 'RideRiders', 'db_table': "'rides_riders'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paid': ('django.db.models.fields.BooleanField', [], {}),
            'pending': ('django.db.models.fields.BooleanField', [], {}),
            'ride': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rides.Ride']"}),
            'sale': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sales.Sale']", 'null': 'True', 'blank': 'True'}),
            'signup_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 8, 26, 0, 0)'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'sales.sale': {
            'Meta': {'object_name': 'Sale', 'db_table': "'sales'"},
            'amount': ('django.db.models.fields.IntegerField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'card': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'charge_id': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'gbp'", 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'livemode': ('django.db.models.fields.BooleanField', [], {}),
            'rider': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'sale_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 8, 26, 0, 0)'})
        }
    }

    complete_apps = ['rides']