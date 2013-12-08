# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ToolEntry.angle'
        db.alter_column(u'toollist_toolentry', 'angle', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'ToolEntry.chip_flute_length'
        db.alter_column(u'toollist_toolentry', 'chip_flute_length', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'ToolEntry.radius'
        db.alter_column(u'toollist_toolentry', 'radius', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

    def backwards(self, orm):

        # Changing field 'ToolEntry.angle'
        db.alter_column(u'toollist_toolentry', 'angle', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'ToolEntry.chip_flute_length'
        db.alter_column(u'toollist_toolentry', 'chip_flute_length', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'ToolEntry.radius'
        db.alter_column(u'toollist_toolentry', 'radius', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=3))

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
            'angle': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'chip_flute_length': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'cog_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cooling': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['toollist.ToolCooling']"}),
            'diameter': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'edge_radius': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'holder': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['toollist.ToolHolder']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'machine': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['toollist.Machine']"}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'pliers': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '1', 'blank': 'True'}),
            'radius': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
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