from sklearn.metrics import confusion_matrix,precision_score,recall_score,f1_score,accuracy_score
a=[0,0,0,0,0,0,0,0,1,1];b=[0,0,0,0,0,0,0,0,0,1]
print('Matriz:',confusion_matrix(a,b));print('Precisão:',precision_score(a,b),'Recall:',recall_score(a,b),'F1:',round(f1_score(a,b),2),'Acurácia:',accuracy_score(a,b))
