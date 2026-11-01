from dados import X,y
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedKFold,cross_val_score,GridSearchCV
cv=StratifiedKFold(n_splits=5,shuffle=True,random_state=42)
modelos={'RandomForest':RandomForestClassifier(random_state=42),'SVM':SVC(),'KNN':KNeighborsClassifier(n_neighbors=3)}
resultados={}
for nome,clf in modelos.items():
    p=Pipeline([('scaler',StandardScaler()),('clf',clf)]);resultados[nome]=cross_val_score(p,X,y,cv=cv).mean();print(nome,round(resultados[nome],3))
vencedor=max(resultados,key=resultados.get);print('Vencedor:',vencedor)
parametros={'RandomForest':{'clf__n_estimators':[50,100],'clf__max_depth':[None,3]},'SVM':{'clf__C':[.1,1,10],'clf__kernel':['linear','rbf']},'KNN':{'clf__n_neighbors':[1,3]}}
busca=GridSearchCV(Pipeline([('scaler',StandardScaler()),('clf',modelos[vencedor])]),parametros[vencedor],cv=cv);busca.fit(X,y);print('Melhores parâmetros:',busca.best_params_)
