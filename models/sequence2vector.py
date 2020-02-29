# -*- coding: utf-8 -*-

from tensorflow.keras import layers, Model, activations



class CrossProduct(layers.Layer):
    pass


class Sequence2Vector(Model):
    def __init__(self):
        pass
        self.layer1 = layers.Embedding()
        self.layer2 = CrossProduct()
        self.layer3 = activations()
        
    def call(self, x_center, x_positive, x_negative):
        pass
        v_center = self.layer1(x_center)
        v_pos = self.layer1(x_positive)
        v_neg = self.layer1(x_negative)
        
        h1 = self.layer2(v_center, v_pos, v_neg)
        prob = self.layer3(h1)
    
    def compute_output_shape(self, input_shape):
        pass