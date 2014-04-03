# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'University'
        db.create_table(u'course_university', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
        ))
        db.send_create_signal(u'course', ['University'])

        # Adding model 'Course'
        db.create_table(u'course_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('university', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['course.University'])),
        ))
        db.send_create_signal(u'course', ['Course'])


    def backwards(self, orm):
        # Deleting model 'University'
        db.delete_table(u'course_university')

        # Deleting model 'Course'
        db.delete_table(u'course_course')


    models = {
        u'course.course': {
            'Meta': {'object_name': 'Course'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'university': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['course.University']"})
        },
        u'course.university': {
            'Meta': {'object_name': 'University'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        }
    }

    complete_apps = ['course']