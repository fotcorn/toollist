# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ToolType'
        db.create_table(u'toollist_tooltype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'toollist', ['ToolType'])

        # Adding model 'Tool'
        db.create_table(u'toollist_tool', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tool_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['toollist.ToolType'])),
        ))
        db.send_create_signal(u'toollist', ['Tool'])

        # Adding model 'ToolHolder'
        db.create_table(u'toollist_toolholder', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'toollist', ['ToolHolder'])

        # Adding model 'ToolCooling'
        db.create_table(u'toollist_toolcooling', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'toollist', ['ToolCooling'])

        # Adding model 'Machine'
        db.create_table(u'toollist_machine', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'toollist', ['Machine'])

        # Adding model 'ToolEntry'
        db.create_table(u'toollist_toolentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('tool_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['toollist.ToolType'])),
            ('tool', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['toollist.Tool'])),
            ('machine', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['toollist.Machine'])),
            ('holder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['toollist.ToolHolder'])),
            ('cooling', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['toollist.ToolCooling'])),
            ('diameter', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('angle', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('pliers', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=1, blank=True)),
            ('length', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=3, blank=True)),
            ('radius', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=3, blank=True)),
        ))
        db.send_create_signal(u'toollist', ['ToolEntry'])


    def backwards(self, orm):
        # Deleting model 'ToolType'
        db.delete_table(u'toollist_tooltype')

        # Deleting model 'Tool'
        db.delete_table(u'toollist_tool')

        # Deleting model 'ToolHolder'
        db.delete_table(u'toollist_toolholder')

        # Deleting model 'ToolCooling'
        db.delete_table(u'toollist_toolcooling')

        # Deleting model 'Machine'
        db.delete_table(u'toollist_machine')

        # Deleting model 'ToolEntry'
        db.delete_table(u'toollist_toolentry')


    models = {
        u'toollist.machine': {
            'Meta': {'object_name': 'Machine'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'toollist.tool': {
            'Meta': {'object_name': 'Tool'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tool_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['toollist.ToolType']"})
        },
        u'toollist.toolcooling': {
            'Meta': {'object_name': 'ToolCooling'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'toollist.toolentry': {
            'Meta': {'object_name': 'ToolEntry'},
            'angle': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cooling': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['toollist.ToolCooling']"}),
            'diameter': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'holder': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['toollist.ToolHolder']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'machine': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['toollist.Machine']"}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'pliers': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '1', 'blank': 'True'}),
            'radius': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'tool': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['toollist.Tool']"}),
            'tool_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['toollist.ToolType']"})
        },
        u'toollist.toolholder': {
            'Meta': {'object_name': 'ToolHolder'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'toollist.tooltype': {
            'Meta': {'object_name': 'ToolType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['toollist']