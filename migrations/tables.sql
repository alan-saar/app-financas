CREATE TABLE "VOIP".conta (
        id INT NOT NULL GENERATED BY DEFAULT AS IDENTITY (START WITH 1),
        nome VARCHAR(50) NOT NULL,
        resumo VARCHAR(100) NOT NULL,
        valor FLOAT NOT NULL,
        PRIMARY KEY (id)
);

CREATE TABLE "VOIP".operacao (
        id INT NOT NULL GENERATED BY DEFAULT AS IDENTITY (START WITH 1),
        nome VARCHAR(50) NOT NULL,
        resumo VARCHAR(100) NOT NULL,
        custo FLOAT NOT NULL,
        tipo VARCHAR(30) NOT NULL,
        PRIMARY KEY (id)
);


ALTER TABLE voip.operacao ADD COLUMN CONTA_ID INT;

ALTER TABLE voip.operacao ADD FOREIGN KEY (CONTA_ID) REFERENCES VOIP.CONTA(ID);

CALL admin_cmd('REORG table voip.operacao');
