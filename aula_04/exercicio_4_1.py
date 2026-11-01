import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
X=np.array([[1,0,0,0,0],[0,0,0,0,1],[2,1,0,0,0],[1,0,0,0,0],[8,1,1,1,5],[12,0,1,1,8],[6,1,1,1,3],[10,1,1,1,6],[0,0,0,0,0],[15,1,1,1,9]])
y=np.array([0,0,0,0,1,1,1,1,0,1]);a,b,c,d=train_test_split(X,y,test_size=.3,random_state=42,stratify=y)
m=RandomForestClassifier(random_state=42).fit(a,c);p=m.predict(b)
for nome,valor in [('Acurácia',accuracy_score(d,p)),('Precisão',precision_score(d,p,zero_division=0)),('Recall',recall_score(d,p,zero_division=0)),('F1',f1_score(d,p,zero_division=0))]:print(nome,round(valor,3))
print('Caso novo:', 'Phishing' if m.predict([[11,1,1,1,7]])[0] else 'Legítimo')
