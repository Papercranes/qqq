from django.db import models

# Create your models here.


# class smalldata(models.Model):
#     id = models.CharField(max_length=200, db_column='ID', primary_key=True)
#     entity1 = models.CharField(max_length=200, db_column='ENTITY1')
#     type1 = models.CharField(max_length=200, db_column='TYPE1')
#     site1 = models.CharField(max_length=200, db_column='SITE1')
#     entity2 = models.CharField(max_length=200, db_column='ENTITY2')
#     type2 = models.CharField(max_length=200, db_column='TYPE2')
#     site2 = models.CharField(max_length=200, db_column='SITE2')
#     sentid = models.CharField(max_length=200, db_column='SENTID')
#     sentence = models.CharField(max_length=200, db_column='SENTENCE')
#     pmid = models.CharField(max_length=200, db_column='PMID')
#     relation = models.CharField(max_length=200, db_column='RELATION')
#
#     class Meta():
#         managed = True,
#         app_label = 'ADLitMiner'
#         db_table = 'smalldata'


class Evidence(models.Model):
    id = models.CharField(max_length=200, db_column='ID', primary_key=True)
    pmid = models.CharField(max_length=200, db_column='PMID')
    sentid = models.CharField(max_length=200, db_column='SENTID')
    sentence = models.CharField(max_length=200, db_column='SENTENCE')
    entity1 = models.CharField(max_length=200, db_column='ENTITY1')
    relation1 = models.CharField(max_length=200, db_column='RELATION1')
    entity2 = models.CharField(max_length=200, db_column='ENTITY2')
    relation2 = models.CharField(max_length=200, db_column='RELATION2')
    entity3 = models.CharField(max_length=200, db_column='ENTITY3')
    relation3 = models.CharField(max_length=200, db_column='RELATION3')
    entity4 = models.CharField(max_length=200, db_column='ENTITY4')

    class Meta():
        managed = True,
        app_label = 'ADLitMiner'
        db_table = 'evidence_small_test'


class Evidence_Processed(models.Model):
    id = models.CharField(max_length=200, db_column='ID', primary_key=True)
    pmid = models.CharField(max_length=200, db_column='PMID')
    sentid = models.CharField(max_length=200, db_column='SENTID')
    sentence = models.CharField(max_length=200, db_column='SENTENCE')
    node = models.CharField(max_length=200, db_column='NODE')
    link = models.CharField(max_length=200, db_column='LINK')

    class Meta():
        managed = True,
        app_label = 'ADLitMiner'
        db_table = 'drug_il1b_info'
        # db_table = 'evidence_small_test_data2'


class Function(models.Model):
    id = models.CharField(max_length=200, db_column='ID', primary_key=True)
    drugid = models.CharField(max_length=200, db_column='DRUGID')
    drugname = models.CharField(max_length=200, db_column='DRUGNAME')
    indicati = models.CharField(max_length=200, db_column='INDICATI')
    hcs = models.CharField(max_length=200, db_column='Highest_status')
    targetid = models.CharField(max_length=200, db_column='TargetID')
    targname = models.CharField(max_length=200, db_column='TARGNAME')
    gene = models.CharField(max_length=200, db_column='GENE')
    geneid = models.CharField(max_length=200, db_column='GENEID')
    moa = models.CharField(max_length=200, db_column='MOA')
    evidence = models.CharField(max_length=200, db_column='EVIDENCE')
    distance = models.CharField(max_length=200, db_column='DISTANCE')
    evidenceall = models.CharField(max_length=200, db_column='EVIDENCEALL')

    class Meta():
        managed = True,
        app_label = 'ADLitMiner'
        # db_table = 'dr_example'
        db_table = 'dr_result'


class func1_test2(models.Model):
    id = models.CharField(max_length=200, db_column='ID', primary_key=True)
    targetid = models.CharField(max_length=200, db_column='TARGETID')
    targname = models.CharField(max_length=200, db_column='TARGNAME')
    genename = models.CharField(max_length=200, db_column='GENENAME')
    geneid = models.CharField(max_length=200, db_column='GENEID')
    targtype = models.CharField(max_length=200, db_column='TARGTYPE')
    synonyms = models.CharField(max_length=200, db_column='SYNONYMS')
    function = models.CharField(max_length=200, db_column='FUNCTION')
    druginfo = models.CharField(max_length=200, db_column='DRUGINFO')
    keggpath = models.CharField(max_length=200, db_column='KEGGPATH')
    sentid = models.CharField(max_length=200, db_column='SENTID')
    pmid = models.CharField(max_length=200, db_column='PMID')
    sentence = models.CharField(max_length=200, db_column='SENTENCE')
    tagging = models.CharField(max_length=200, db_column='TAGGING')

    class Meta():
        managed = True,
        app_label = 'ADLitMiner'
        db_table = 'func1_test2'