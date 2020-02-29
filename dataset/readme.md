# dataset module

This module is designed to manage dataset. Tables can be read by using 

* dataset.load_dataset.load_click
* dataset.load_dataset.load_sku 
* ......

Data within a given timerange can be selected by using
* dataset.select_data.select_timerange


We recommend to put all function that's related to query and modify in this module.
