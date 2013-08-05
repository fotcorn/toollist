# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'ToolEntry', fields ['machine', 'number']
        db.create_unique(u'toollist_toolentry', ['machine_id', 'number'])


    def backwards(self, orm):
        # Removing unique constraint on 'ToolEntry', fields ['machine', 'number']
        db.delete_unique(u'toollist_toolentry', ['machine_id', 'number'])


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
            'Meta': {'unique_together': "(('number', 'machine'),)", 'object_name': 'ToolEntry'},
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