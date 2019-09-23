#!/usr/bin/python
# -*- coding: UTF-8 -*-


from bert_serving.client import BertClient
import datetime

bc = BertClient()
m = '2'

def trigger(m):
    file_dir = './gcn/why_merged_' + m + '_set.tsv'
    trigger = []
    with open(file_dir, 'r') as f:
        line = f.readline()
        while line:
            trigger.append(line[:-1])
            line = f.readline()
    return trigger

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))            
node_feat_vec_H0 = bc.encode(trigger(m))
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

node_feat_vec_H0.tofile('./node_feat_vec_H0_cutoff_' + m + '.txt')
print(node_feat_vec_H0.shape)
