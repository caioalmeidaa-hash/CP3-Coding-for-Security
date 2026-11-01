from dados import X,y
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold,cross_val_score
m=Pipeline([('scaler',StandardScaler()),('clf',RandomForestClassifier(random_state=42))]);r=cross_val_score(m,X,y,cv=StratifiedKFold(n_splits=5,shuffle=True,random_state=42))
print('Acurácia:',round(r.mean(),3),'+/-',round(r.std(),3))
