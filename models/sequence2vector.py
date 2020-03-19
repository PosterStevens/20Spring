# -*- coding: utf-8 -*-

from keras import layers, Model, activations
from keras import backend as K


class CrossInnerProduct(layers.Layer):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

    def call(self, center_vec, windows_vecs, neg_vecs, buy_vec):
        '''
        把center和windows以及negative sampling里每一个向量做内积
        '''
        
        cross_center_windows = [] # center和windows的内积结果
        cross_center_negtive = [] # center和negative sampling的内积结果

        for vec in windows_vecs:
            # 循环windows里所有的向量
            # 每个向量都和中心向量做内积
            inner_product = K.dot(center_vec, K.transpose(vec))
            cross_center_windows.append(inner_product)
        for neg_vec in neg_vecs:
            # 循环negative sampling里所有向量
            # 每个向量都和中心向量做内积
            # 结果取相反数
            inner_product = -K.dot(center_vec, K.transpose(neg_vec))
            cross_center_negtive.append(inner_product)
        # 中心向量与购买商品的embedding向量做内积
        cross_center_buy = K.dot(center_vec, K.transpose(buy_vec))
        
        # 将内积结果concatena
        cross_center_windows = K.concatenate(cross_center_windows)
        cross_center_negtive = K.concatenate(cross_center_negtive)
        
        # 将center与windows的内积结果
        # center 与负采样的内积结果
        # center 与购买向量的内积结果
        # concate在一起
        output = K.concatenate([cross_center_windows, 
                                cross_center_negtive, cross_center_buy])

        return K.concatenate([cross_center_windows, cross_center_negtive, cross_center_buy])
    
    def __call__(self, *args):
        output = self.call(*args)
        return output


class Sequence2Vector(Model):
    def __init__(self, embedding_dim, name=''):
        super(Model, self).__init__(name=name)
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



    if __name__ == '__main__':

        '''
        测试内积层
        '''

        # 初始话内积层
        test_layer = CrossInnerProduct()

        # 做一个center向量
        center = K.variable([[1.1,2.0,1.0,1.0]])

        # windows宽度为1
        windowsvec = [K.variable([[2,2,2,2.0]]),
                        K.variable([[0,2.0,1,0]])]

        # 随便输入两个负采样向量
        negvec = [K.variable([[2,0,0,2]]),
                        K.variable([[0,2,2.0,0]])]

        # 购买商品的向量
        buy = K.variable([[1,1,1,.01]])

        # 测试计算结果
        result = test_layer(center, windowsvec, negvec, buy)
        print(K.eval(result))



