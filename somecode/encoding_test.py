# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 09:10:33 2022
Encoding Test
@author: Eric Huang
"""

import numpy as np
import pandas as pd
country=['Taiwan','Australia','Ireland','Australia','Ireland','Taiwan']
age=[25,30,45,35,22,36]
salary=[20000,32000,59000,60000,43000,52000]
dic={'Country':country,'Age':age,'Salary':salary}
data=pd.DataFrame(dic)
print(data)

## 原始資料是有序離散值的話 => Label Encoding
## 原始資料是無序離散值的話 => One Hot Encoding (Dummies)

### One Hot Encoding by pandas
data_dum = pd.get_dummies(data)
data2 = pd.DataFrame(data_dum)
print(data2)


### One Hot Encoding by sklearn
# =============================================================================
# from sklearn.preprocessing import OneHotEncoder
# onehotencoder = OneHotEncoder(data['Country'])
# print(onehotencoder)
# onehotencoder = OneHotEncoder()
# data_str_ohe=onehotencoder.fit_transform(data).toarray()
# print(data_str_ohe)
# print(pd.DataFrame(data_str_ohe))
# =============================================================================


### Label Encoding by sklearn
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
data_le=pd.DataFrame(dic)
data_le['Country'] = labelencoder.fit_transform(data['Country'])
print(data_le)
