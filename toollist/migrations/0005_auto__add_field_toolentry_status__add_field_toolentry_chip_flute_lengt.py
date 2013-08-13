# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ToolEntry.status'
        db.add_column(u'toollist_toolentry', 'status',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'ToolEntry.chip_flute_length'
        db.add_column(u'toollist_toolentry', 'chip_flute_length',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'ToolEntry.edge_count'
        db.add_column(u'toollist_toolentry', 'edge_count',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=3, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ToolEntry.status'
        db.delete_column(u'toollist_toolentry', 'status')

        # Deleting field 'ToolEntry.chip_flute_length'
        db.delete_column(u'toollist_toolentry', 'chip_flute_length')

        # Deleting field 'ToolEntry.edge_count'
        db.delete_column(u'toollist_toolentry', 'edge_count')


    models = {
        u'toollist.machine': {
            'Meta': {'object_name': 'Machine'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'toollist.tool': {
            'Meta': {'ordering': "('type__name', 'name')", 'object_name': 'Tool'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['toollist.ToolType']"})
        },
        u'toollist.toolcooling': {
            'Meta': {'object_name': 'ToolCooling'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'toollist.toolentry': {
            'Meta': {'unique_together': "(('number', 'machine'),)", 'object_name': 'ToolEntry'},
            'angle': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'chip_flute_length': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cog_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cooling': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['toollist.ToolCooling']"}),
            'diameter': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'edge_count': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'holder': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['toollist.ToolHolder']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'machine': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['toollist.Machine']"}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'pliers': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '1', 'blank': 'True'}),
            'radius': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'tool': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['toollist.Tool']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['toollist.ToolType']"})
        },
        u'toollist.toolholder': {
            'Meta': {'ordering': "('name',)", 'object_name': 'ToolHolder'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'toollist.tooltype': {
            'Meta': {'ordering': "('name',)", 'object_name': 'ToolType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['toollist']