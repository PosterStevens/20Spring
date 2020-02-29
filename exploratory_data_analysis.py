# -*- coding: utf-8 -*-

import utils
import dataset.load_dataset as data_load
import dataset.select_data as data_select
import pandas as pd



if __name__ == '__main__':
    print(data_load.load_click.__doc__)
    df_click = data_load.load_click()
    
    d = data_select.select_timerange(df_click, '2018-2-1',
                                     '2018-4-1')
    

