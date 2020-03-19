# -*- coding: utf-8 -*-
from tqdm import tqdm
import sys
sys.path.append('../')
import utils

def to_sequence(df, attrs=['sku_ID', 'user_ID', 'if_order', 'request_time'],
                 num_clicks=1000000):
    '''
    convert sorted dataframe into sequence:
    [[user_ID1, [sku_ID_1, sku_ID2, ...], [time1, time2, ...], [False, True, ...]]]
     [user_ID2, [sku_ID_3, sku_ID4, ...], [time3, time4, ...], [False, False, ...]]
    
    '''
    df = df.query('user_ID != "-"')
    same_user_indicator = df['user_ID'].shift(1) == df['user_ID']
    same_user_indicator.iloc[0] = True
    
    sequences = []
    sequence = [None, [], [], []]
    sequence[0] = df['user_ID'].iloc[0]
    for i in tqdm(range(0, num_clicks)):
        user = df['user_ID'].iloc[i]
        if_same_user = same_user_indicator.iloc[i]
        if not if_same_user:
            sequences.append(sequence)
            sequence = [None] + [[] for attr in attrs]
            sequence[0] = user
        for _, attr in enumerate(attrs):
            attr_value = df[attr].iloc[i]
            sequence[_+1].append(attr_value)
    utils.save_pickle(sequences, 'click_sequence.pk')
    return sequences



        