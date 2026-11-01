USE seguranca;
CREATE TABLE IF NOT EXISTS alertas (id INT AUTO_INCREMENT PRIMARY KEY,tipo VARCHAR(50),ip_origem VARCHAR(45),severidade ENUM('baixa','media','alta','critica'),status VARCHAR(20) DEFAULT 'aberto',criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
INSERT INTO alertas(tipo,ip_origem,severidade) VALUES('PORT_SCAN','192.168.1.10','alta'),('BRUTE_FORCE','192.168.1.20','critica'),('LOGIN_FAIL','192.168.1.30','alta');
SELECT * FROM alertas WHERE severidade='alta';
UPDATE alertas SET status='resolvido' WHERE tipo='PORT_SCAN' AND ip_origem='192.168.1.10';
SELECT severidade,COUNT(*) total FROM alertas GROUP BY severidade;
DELETE FROM alertas WHERE criado_em < NOW()-INTERVAL 90 DAY;
