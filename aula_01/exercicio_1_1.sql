CREATE DATABASE IF NOT EXISTS seguranca; USE seguranca;
CREATE TABLE IF NOT EXISTS ativos (id INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(100),ip VARCHAR(45) UNIQUE,tipo VARCHAR(50),criticidade VARCHAR(20));
CREATE TABLE IF NOT EXISTS vulnerabilidades (id INT AUTO_INCREMENT PRIMARY KEY,cve_id VARCHAR(30) UNIQUE,descricao TEXT,severidade ENUM('Baixa','Media','Alta','Critica'),cvss DECIMAL(3,1));
CREATE TABLE IF NOT EXISTS ativo_vulnerabilidade (ativo_id INT,vuln_id INT,status VARCHAR(30) DEFAULT 'aberta',detectada_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,PRIMARY KEY(ativo_id,vuln_id),FOREIGN KEY(ativo_id) REFERENCES ativos(id),FOREIGN KEY(vuln_id) REFERENCES vulnerabilidades(id));
INSERT IGNORE INTO ativos(nome,ip,tipo,criticidade) VALUES('SRV-WEB01','192.168.1.10','servidor','alta');
INSERT IGNORE INTO vulnerabilidades(cve_id,descricao,severidade,cvss) VALUES('CVE-2024-001','Exemplo didatico','Alta',8.5);
INSERT IGNORE INTO ativo_vulnerabilidade(ativo_id,vuln_id) SELECT a.id,v.id FROM ativos a JOIN vulnerabilidades v WHERE a.ip='192.168.1.10' AND v.cve_id='CVE-2024-001';
SELECT a.nome,v.cve_id,v.cvss FROM ativo_vulnerabilidade av JOIN ativos a ON a.id=av.ativo_id JOIN vulnerabilidades v ON v.id=av.vuln_id;
