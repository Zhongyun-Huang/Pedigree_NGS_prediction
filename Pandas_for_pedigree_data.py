##### Python Pandas demo for large scale pedigree data ####
###########################################################


import pandas as pd
import pandas as pd
import pylab
from pandas import *
from pylab import *
import numpy as np
a=np.array(range(15))
a
a.reshape(3,
a=a.reshape(3,5)
a
a.columns
a=pd.DataFrame(a)
type(a)
a
a.columns=['c1', 'c2','c3','c4', 'c5']
a
a.index=['r1', 'r2', 'r3']
a
a.sum()
a.sum(axis=0)
a.sum(axis=1)
perc_matrix = pd.read_csv('/data/genome/project/u783407/SLB60_5AASL0041/fake_SLB60_3ZZSB2361/matrix_out_TF_fake_DH-SLB60.csv')
perc_matrix.head(2)

perc_matrix = pd.read_csv('/data/genome/project/u783407/SLB60_5AASL0041/fake_SLB60_3ZZSB2361/matrix_out_TF_fake_DH-SLB60.csv', sep='\t', header=0, index_col=0)
perc_matrix.head(2)
perc_matrix = pd.read_csv('/data/genome/project/u783407/SLB60_5AASL0041/fake_SLB60_3ZZSB2361/matrix_out_TF_fake_DH-SLB60.csv', sep='\t', header=0, index_col=None)
perc_matrix.head(2)
a=perc_matrix
a.head(2)
a.sum().head(2)
a.replace(0,1).head(2)
a.replace(0,1).sum().head(2)
a.replace(0,1).sum().head(10)
a.sum()/a.replace(0,1).sum()
a
a.sum()/a.replace(0,1).sum()
a.sum()/a.replace(0,1).sum().sort_values()
m=a.sum()/a.replace(0,1).sum()
type(m)
m.sort_values
m.head(2)
m
m.head(10)
m.sort_values?
m.sort_values(axis=0)