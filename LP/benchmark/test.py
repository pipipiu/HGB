import numpy as np
import pickle
import os

from scripts.data_loader import data_loader

data_name = LastFM
data_dir = f'./data/{data_name}'
dl_pickle_f = os.path.join(data_dir, 'dl_pickle')
if os.path.exists(dl_pickle_f):
    dl = pickle.load(open(dl_pickle_f, 'rb'))
    print(f'Info: load {data_name} from {dl_pickle_f}')
else:
    dl = data_loader(data_dir)
    pickle.dump(dl, open(dl_pickle_f, 'wb'))
    print(f'Info: load {data_name} from original data and generate {dl_pickle_f}')

print(dl.nodes)
print(dl.links)
print(dl.links_test)
pred = dl.links_test['data']
print(dl.evaluate(pred))
train_idx = np.nonzero(dl.labels_train['mask'])[0]
test_idx = np.nonzero(dl.labels_test['mask'])[0]
print(train_idx)
print(train_idx.shape)
print(test_idx)
print(test_idx.shape)

meta = [(0, 1), (1, 0)]
print(dl.get_meta_path(meta))
print(dl.get_full_meta_path(meta)[0])