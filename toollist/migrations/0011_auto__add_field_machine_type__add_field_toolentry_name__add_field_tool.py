# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Machine.type'
        db.add_column(u'toollist_machine', 'type',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'ToolEntry.name'
        db.add_column(u'toollist_toolentry', 'name',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ToolEntry.geometry_x'
        db.add_column(u'toollist_toolentry', 'geometry_x',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=3, blank=True),
                      keep_default=False)

        # Adding field 'ToolEntry.geometry_y'
        db.add_column(u'toollist_toolentry', 'geometry_y',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=3, blank=True),
                      keep_default=False)

        # Adding field 'ToolEntry.geometry_z'
        db.add_column(u'toollist_toolentry', 'geometry_z',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=3, blank=True),
                      keep_default=False)

        # Adding field 'ToolEntry.geometry_c'
        db.add_column(u'toollist_toolentry', 'geometry_c',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=3, blank=True),
                      keep_default=False)

        # Adding field 'ToolEntry.wear_x'
        db.add_column(u'toollist_toolentry', 'wear_x',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=3, blank=True),
                      keep_default=False)

        # Adding field 'ToolEntry.wear_y'
        db.add_column(u'toollist_toolentry', 'wear_y',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=3, blank=True),
                      keep_default=False)

        # Adding field 'ToolEntry.wear_z'
        db.add_column(u'toollist_toolentry', 'wear_z',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=3, blank=True),
                      keep_default=False)

        # Adding field 'ToolEntry.wear_c'
        db.add_column(u'toollist_toolentry', 'wear_c',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=3, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Machine.type'
        db.delete_column(u'toollist_machine', 'type')

        # Deleting field 'ToolEntry.name'
        db.delete_column(u'toollist_toolentry', 'name')

        # Deleting field 'ToolEntry.geometry_x'
        db.delete_column(u'toollist_toolentry', 'geometry_x')

        # Deleting field 'ToolEntry.geometry_y'
        db.delete_column(u'toollist_toolentry', 'geometry_y')

        # Deleting field 'ToolEntry.geometry_z'
        db.delete_column(u'toollist_toolentry', 'geometry_z')

        # Deleting field 'ToolEntry.geometry_c'
        db.delete_column(u'toollist_toolentry', 'geometry_c')

        # Deleting field 'ToolEntry.wear_x'
        db.delete_column(u'toollist_toolentry', 'wear_x')

        # Deleting field 'ToolEntry.wear_y'
        db.delete_column(u'toollist_toolentry', 'wear_y')

        # Deleting field 'ToolEntry.wear_z'
        db.delete_column(u'toollist_toolentry', 'wear_z')

        # Deleting field 'ToolEntry.wear_c'
        db.delete_column(u'toollist_toolentry', 'wear_c')


    models = {
        u'toollist.machine': {
            'Meta': {'object_name': 'Machine'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '1'})
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
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'cooling': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['toollist.ToolCooling']"}),
            'diameter': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'edge_radius': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'geometry_c': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '3', 'blank': 'True'}),
            'geometry_x': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '3', 'blank': 'True'}),
            'geometry_y': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '3', 'blank': 'True'}),
            'geometry_z': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '3', 'blank': 'True'}),
            'holder': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['toollist.ToolHolder']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'machine': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['toollist.Machine']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'pliers': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '1', 'blank': 'True'}),
            'radius': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'tool': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['toollist.Tool']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['toollist.ToolType']"}),
            'wear_c': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '3', 'blank': 'True'}),
            'wear_x': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '3', 'blank': 'True'}),
            'wear_y': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '3', 'blank': 'True'}),
            'wear_z': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '3', 'blank': 'True'})
        },
        u'toollist.toolholder': {
            'Meta': {'ordering': "('name',)", 'object_name': 'ToolHolder'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['toollist.Machine']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'toollist.tooltype': {
            'Meta': {'ordering': "('name',)", 'object_name': 'ToolType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['toollist']