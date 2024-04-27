from django.shortcuts import render
from.models import *
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
import ast


def index(request):
    return render(request, "ADLitMiner/homepage.html")


def intro(request):
    return render(request, "ADLitMiner/introduction.html")


# @csrf_exempt
# def data(request):
#     re_data = smalldata.objects.filter(Q(relation='ThemeOf') | Q(relation='CauseOf')).values()
#     all_sentence = []
#     evidence_table = []
#     entity = []
#     link = []
#     # gene_list = []
#     gene_list = {'Gene': [], 'Var': [], 'Reg': [], 'PosReg': [], 'NegReg': [],
#                  'Protein': [], 'Enzyme': [], 'MPA': [], 'CPA': [], 'Disease': [],
#                  'Pathway': [], 'Interaction': []}
#     color_dic = {'Gene': '#FFA500', 'Var': '#9400D3', 'Reg': '#696969', 'PosReg': '#dc143c', 'NegReg': '#4169e1',
#                  'Protein': '#F0E68C', 'Enzyme': '#BDB76B', 'MPA': '#008000', 'CPA': '#98FB98', 'Disease': '#87CEFA',
#                  'Pathway': '#FF69B4', 'Interaction': '#FFB6C1'}
#
#     for single_data in re_data:
#         pmid = single_data['pmid']
#         sentid = single_data['sentid']
#         sent = single_data['sentence']
#         entity1 = single_data['entity1']
#         type1 = single_data['type1']
#         # site1 = single_data['site1']
#         entity2 = single_data['entity2']
#         type2 = single_data['type2']
#         # site2 = single_data['site2']
#         relation = single_data['relation']
#
#         if {'id': entity1, 'text': entity1} not in gene_list[type1]:
#             gene_list[type1].append({'id': entity1, 'text': entity1})
#         if {'id': entity2, 'text': entity2} not in gene_list[type2]:
#             gene_list[type2].append({'id': entity2, 'text': entity2})
#
#         # [gene_list.append(x) for x in [entity1, entity2] if x not in gene_list]
#
#         new_sent = {'id': pmid, 'sentid': sentid}
#         if new_sent in all_sentence:
#             entity = entity + [{'name': entity1, 'category': type1, 'color': color_dic[type1]},
#                                {'name': entity2, 'category': type2, 'color': color_dic[type2]}]
#             entity = [dict(t) for t in set([tuple(d.items()) for d in entity])]      #去重复
#             link = link + [{'source': entity1, 'target': entity2, 'category': relation}]
#             link = [dict(t) for t in set([tuple(d.items()) for d in link])]
#             for en in entity:
#                 tag_en = '<b><font color=\"' + en['color'] + '\">' + en['name'] + '</font></b>'
#                 sent = sent.replace(en['name'], tag_en)
#             single_evidence = {'id': pmid, 'sentid': sentid, 'sent': sent, 'node': entity, 'link': link}
#             evidence_table[len(evidence_table)-1] = single_evidence
#         else:
#             all_sentence.append(new_sent)
#             entity = [{'name': entity1, 'category': type1, 'color': color_dic[type1]},
#                       {'name': entity2, 'category': type2, 'color': color_dic[type2]}]
#             link = [{'source': entity1, 'target': entity2, 'category': relation}]
#             for en in entity:
#                 tag_en = '<b><font color=\"' + en['color'] + '\">' + en['name'] + '</font></b>'
#                 sent = sent.replace(en['name'], tag_en)
#             single_evidence = {'id': pmid, 'sentid': sentid, 'sent': sent, 'node': entity, 'link': link}
#             evidence_table.append(single_evidence)
#
#     if request.method == 'POST':
#         input_list = request.POST.getlist('list[]')
#         print(input_list)
#         update_evidence = [d for d in evidence_table if 'node' in d and any(e['name'] in input_list for e in d['node'])]
#
#         return JsonResponse({'data': update_evidence}, safe=False)
#
#     return render(request, "ADLitMiner/data.html", {'gene_list': gene_list, 'evidence': evidence_table})

@csrf_exempt
def evidence(request):
    # re_data = Evidence.objects.all().values()
    # sentence_tag = []
    # entity_all = []
    # link_all = []
    evidence_table = []
    select_entity = {'Gene': [], 'Var': [], 'Reg': [], 'PosReg': [], 'NegReg': [],
                 'Protein': [], 'Enzyme': [], 'MPA': [], 'CPA': [], 'Disease': [],
                 'Pathway': [], 'Interaction': []}
    # color_dic = {'Gene': '#FFA500', 'Var': '#9400D3', 'Reg': '#000000', 'PosReg': '#dc143c', 'NegReg': '#4169e1',
    #              'Protein': '#F0E68C', 'Enzyme': '#BDB76B', 'MPA': '#008000', 'CPA': '#98FB98', 'Disease': '#87CEFA',
    #              'Pathway': '#FF69B4', 'Interaction': '#FFB6C1', 'ThemeOf': '#696969', 'CauseOf': '#696969'}
    #
    # for single_data in re_data:
    #     pmid = single_data['pmid']
    #     sentid = single_data['sentid']
    #     sent = single_data['sentence']
    #     # print(single_data['entity1'])
    #     # print(eval(str(single_data['entity1'])))
    #
    #     # 整理该句的实体信息
    #     entity_info = [single_data['entity1'], single_data['entity2'], single_data['entity4']]
    #     entity_list = []
    #     for entity in entity_info:
    #         name, category, _, _ = eval(str(entity))
    #         entity_dict = {
    #                 "name": name,
    #                 "category": category,
    #                 "color": color_dic.get(category, "")
    #         }
    #         entity_list.append(entity_dict)
    #         if {'id': name, 'text': name} not in select_entity[category]:
    #             select_entity[category].append({'id': name, 'text': name})
    #
    #     # 整理关系信息
    #     link_list = []
    #     reg_name, reg_type, _, _ = eval(str(single_data['entity3']))
    #     link_info = [(single_data['entity1'], single_data['relation1'], single_data['entity2']),
    #                  (single_data['entity2'], reg_type, single_data['entity4'])]
    #
    #     for link in link_info:
    #         source_entity, relation, target_entity = link
    #         source_name, _, _, _ = eval(str(source_entity))
    #         target_name, _, _, _ = eval(str(target_entity))
    #         link_dict = {
    #             "source": source_name,
    #             "target": target_name,
    #             "category": relation,
    #             "color": color_dic.get(relation, "")
    #         }
    #         link_list.append(link_dict)
    #
    #     new_sent = {'pmid': pmid, 'sentid': sentid}
    #     if new_sent in sentence_tag:
    #         entity_all = entity_all + entity_list
    #         entity_all = [dict(t) for t in set([tuple(d.items()) for d in entity_all])]  # 去重复
    #         link_all = link_all + link_list
    #         link_all = [dict(t) for t in set([tuple(d.items()) for d in link_all])]
    #         for en in entity_all:
    #             tag_en = '<b><font color=\"' + en['color'] + '\">' + en['name'] + '</font></b>'
    #             sent = sent.replace(en['name'], tag_en)
    #         tag_reg_en = '<span class="underline">' + reg_name +'</span>'
    #         sent = sent.replace(reg_name, tag_reg_en)
    #         single_evidence = {'id': pmid, 'sentid': sentid, 'sent': sent, 'node': entity_all, 'link': link_all}
    #         evidence_table[len(evidence_table) - 1] = single_evidence
    #     else:
    #         sentence_tag.append(new_sent)
    #         entity_all = entity_list
    #         link_all = link_list
    #         for en in entity_all:
    #             tag_en = '<b><font color=\"' + en['color'] + '\">' + en['name'] + '</font></b>'
    #             sent = sent.replace(en['name'], tag_en)
    #         single_evidence = {'id': pmid, 'sentid': sentid, 'sent': sent, 'node': entity_all, 'link': link_all}
    #         evidence_table.append(single_evidence)

    re_data = Evidence_Processed.objects.all().values()

    for single_data in re_data:
        node = ast.literal_eval(single_data['node'])
        # print(type(node), node)
        link = ast.literal_eval(single_data['link'])
        single_evidence = {'tag': single_data['id'], 'id': single_data['pmid'], 'sentid': single_data['sentid'], 'sent': single_data['sentence'], 'node': node, 'link': link}
        # print(type(single_data['node']))
        # print(single_data['link'])
        evidence_table.append(single_evidence)
        for i in node:
            if {'id': i['name'], 'text': i['name']} not in select_entity[i['category']]:
                select_entity[i['category']].append({'id': i['name'], 'text': i['name']})

    if request.method == 'POST':
        input_list = request.POST.getlist('list[]')
        print(input_list)
        update_evidence = [d for d in evidence_table if 'node' in d and any(e['name'] in input_list for e in d['node'])]
        # update_evidence = [d for d in evidence_table if 'node' in d and any(e in d['node'] for e in input_list)]

        return JsonResponse({'data': update_evidence}, safe=False)

    return render(request, "ADLitMiner/evidence.html", {'select_entity': select_entity, 'evidence': evidence_table})


def function(request):
    drug_gene = Function.objects.all().values()
    info_out = []
    for target in drug_gene:
        drugid = target['drugid']
        drugname = target['drugname']
        indicati = target['indicati']
        hcs = target['hcs']
        targetid = target['targetid']
        targname = target['targname']
        gene = target['gene']
        geneid = target['geneid']
        moa = target['moa']
        evidence = target['evidence'].split('|')[0]
        evidence_all = target['evidenceall'].split('|')
        distance = target['distance']
        info_out.append([drugid, drugname, indicati, hcs, targetid, targname, gene, geneid, moa, evidence, distance, evidence_all])

    return render(request, "ADLitMiner/function.html", {'info_output': info_out})


def tutorial(request):
    return render(request, "ADLitMiner/tutorial.html")


def contact(request):
    return render(request, "ADLitMiner/contact.html")


# @csrf_exempt
# def test_ajax(request):
#     re_data = smalldata.objects.filter(Q(relation='ThemeOf') | Q(relation='CauseOf')).values()
#     all_sentence = []
#     evidence_table = []
#     single_evidence = {}
#     entity = []
#     link = []
#     gene_list = []
#     for single_data in re_data:
#         pmid = single_data['pmid']
#         sentid = single_data['sentid']
#         sent = single_data['sentence']
#         entity1 = single_data['entity1']
#         type1 = single_data['type1']
#         site1 = single_data['site1']
#         entity2 = single_data['entity2']
#         type2 = single_data['type2']
#         site2 = single_data['site2']
#         relation = single_data['relation']
#
#         [gene_list.append(x) for x in [entity1, entity2] if x not in gene_list]
#
#         new_sent = {'id': pmid, 'sentid': sentid}
#         if new_sent in all_sentence:
#             entity = entity + [{'name': entity1, 'category': type1},
#                                {'name': entity2, 'category': type2}]
#             entity = [dict(t) for t in set([tuple(d.items()) for d in entity])]      #去重复
#             link = link + [{'source': entity1, 'target': entity2, 'category': relation}]
#             link = [dict(t) for t in set([tuple(d.items()) for d in link])]
#             single_evidence = {'id': pmid, 'sentid': sentid, 'sent': sent, 'node': entity, 'link': link}
#             evidence_table[len(evidence_table)-1] = single_evidence
#         else:
#             all_sentence.append(new_sent)
#             entity = [{'name': entity1, 'category': type1},
#                       {'name': entity2, 'category': type2}]
#             link = [{'source': entity1,'target': entity2, 'category': relation}]
#             single_evidence = {'id': pmid, 'sentid': sentid, 'sent': sent, 'node': entity, 'link': link}
#             evidence_table.append(single_evidence)
#
#     # evidence_table.append(single_evidence)
#     # evidence_table.remove({})
#     # print(evidence_table[0:5])
#
#     if request.method == 'POST':
#         input_list = request.POST.getlist('list[]')
#         print(input_list)
#
#         update_evidence = [d for d in evidence_table if 'node' in d and any(e['name'] in input_list for e in d['node'])]
#         # table_data = [d[['id','sentid',]] for d in update_evidence]
#         # 在数据库中执行查询操作，获取相关数据
#         # 假设你已经实现了一个名为 get_data_from_db 的函数来查询数据
#         # data = [{'id':'a', 'sent':'b'},{'id':'c', 'sent':'d'}]
#         return JsonResponse({'data': update_evidence}, safe=False)
#         # return JsonResponse({'data': update_evidence})
#
#     # gene_list = ['CHR', 'AD', 'gene1', 'gene2']
#
#     return render(request, "ADLitMiner/test.html", {'gene_list': gene_list, 'evidence': evidence_table})
#
