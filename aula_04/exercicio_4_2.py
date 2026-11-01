import numpy as np
from sklearn.ensemble import IsolationForest
X=np.array([[9,1,200],[10,1,500],[14,2,300],[11,1,250],[16,1,400],[3,40,900000],[10,1,350],[15,2,280],[2,55,800000]])
r=IsolationForest(contamination=.25,random_state=42).fit_predict(X)
for i,(x,y) in enumerate(zip(X,r)):
    print('Amostra',i,x,'->','ANOMALIA' if y==-1 else 'Normal')
