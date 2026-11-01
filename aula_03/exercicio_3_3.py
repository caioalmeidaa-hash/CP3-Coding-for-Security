import os
import mysql.connector
from mysql.connector import Error

def conectar():
    return mysql.connector.connect(host=os.getenv('MYSQL_HOST','localhost'),user=os.getenv('MYSQL_USER','root'),password=os.getenv('MYSQL_PASSWORD',''),database=os.getenv('MYSQL_DATABASE','seguranca'))

con=conectar();cur=con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS alertas_relatorio (id INT AUTO_INCREMENT PRIMARY KEY,tipo VARCHAR(40),ip_origem VARCHAR(45),severidade VARCHAR(20))')
cur.execute('DELETE FROM alertas_relatorio')
linhas=[('BRUTE_FORCE','185.220.101.1','critica')]*3+[('BRUTE_FORCE','185.220.101.1','alta')]+[('PORT_SCAN','45.33.32.156','alta')]*3+[('XSS','8.8.8.8','media')]*2+[('SQLI','1.1.1.1','baixa')]
cur.executemany('INSERT INTO alertas_relatorio(tipo,ip_origem,severidade) VALUES(%s,%s,%s)',linhas);con.commit()
for titulo,sql in [('Por severidade','SELECT severidade,COUNT(*) FROM alertas_relatorio GROUP BY severidade'),('Por tipo','SELECT tipo,COUNT(*) FROM alertas_relatorio GROUP BY tipo'),('Top IPs','SELECT ip_origem,COUNT(*) total FROM alertas_relatorio GROUP BY ip_origem ORDER BY total DESC LIMIT 5')]:
    print('===',titulo,'===');cur.execute(sql)
    for linha in cur.fetchall():print(*linha)
con.close()
