from sequence2vector import Sequence2Vector, CrossInnerProduct
from sequence2vector import empty_loss

import numpy as np
import keras.backend as K

if __name__ == "__main__":
    center = np.array([[0], [10], [20], [0]], dtype=int)
    windows = np.array([[1,2,3,4], [11,12,13,14], [21,22,23,23], [0,1,1,3]], dtype=int)
    negtive = np.array([[11,21,31,14], [21,2,23,4], [1,2,13,13], [10,21,21,13]], dtype=int)
    buy = np.array([[1], [11], [21], [1]], dtype=int)

    model = Sequence2Vector(40, 3)
    model.compile(optimizer='adam', loss = empty_loss)
    model.fit(x=[center, windows, negtive, buy], y=np.array([1,1,1,1]), epochs=50, batch_size=2)
    print(K.eval(model.to_vector(np.array([0]))))
    print(K.eval(model.to_vector(np.array([1]))))