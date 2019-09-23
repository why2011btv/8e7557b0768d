node_feat_vec_H0_c2_gen.ipynb: feature vector generator, H_0 = X 

node_feat_vec_H0_cutoff_m.txt: feature vector generated, m (= 1,2,3,5,10) is cutoff.

SubG_m.tsv: Graph, m (= 1,2,3,5,10) is cutoff.
Usage: G = nx.read_edgelist('/tf/gcn/gcn/SubG_' + str(cutoff) + '.tsv')

HiEve_merged_m_set.tsv: list of triggers with '_', m (= 1,2,3,5,10) is cutoff.

why_merged_10_set.tsv: list of triggers without '_', m (= 1,2,3,5,10) is cutoff. These triggers can be found in ConceptNet, we use pretrained BERT (https://github.com/hanxiao/bert-as-service) to generate feature vectors for each trigger.

bert-serving-start -model_dir /notebooks/uncased_L-24_H-1024_A-16 -num_worker=1 -max_seq_len=None -device_map=0

