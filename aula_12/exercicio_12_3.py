from dados import X,y
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib,hashlib
from pathlib import Path
p=Path(__file__).with_name('modelo_seguranca.pkl')
m=Pipeline([('scaler',StandardScaler()),('clf',RandomForestClassifier(random_state=42))]).fit(X,y)
joblib.dump(m,p)
def hash_file(path):return hashlib.sha256(path.read_bytes()).hexdigest()
antes=hash_file(p);p.with_suffix('.sha256').write_text(antes,encoding='utf8')
print('Modelo salvo:',p.name,'Hash SHA-256:',antes)
if hash_file(p)!=p.with_suffix('.sha256').read_text(encoding='utf8'):raise SystemExit('ALERTA: arquivo do modelo foi modificado!')
# Carregar somente modelos próprios e verificados; joblib não é seguro para arquivos desconhecidos.
modelo=joblib.load(p);print('Hash confere: modelo íntegro. Previsão de teste:',modelo.predict([[58000,4444,16.]]))
