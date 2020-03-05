# -*- coding: utf-8 -*-
import load_dataset



def join_click_order(cols1 = ['user_ID', 'sku_ID', 'request_date'],
                     cols2 = ['user_ID', 'sku_ID', 'order_date', 'order_ID']):
    from pandas import merge
    click_table = load_dataset.load_click()[cols1]
    order_table = load_dataset.load_order()[cols2]

    click_table.merge(order_table, how='outer',
                      left_on = ['user_ID', 'sku_ID', 'request_date'],
                      right_on = ['user_ID', 'sku_ID', 'order_date'])
    
    return click_table
    




