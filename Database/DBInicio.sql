CREATE TABLE IF NOT EXISTS estado (
	id INTEGER NOT NULL UNIQUE,
    nombre VARCHAR(255) NOT NULL,
    PRIMARY KEY(id AUTOINCREMENT)
);

INSERT INTO estado (nombre) SELECT 'Sin estado' WHERE NOT EXISTS (SELECT 1 FROM estado WHERE nombre = 'Sin estado');
INSERT INTO estado (nombre) SELECT 'Aprobado' WHERE NOT EXISTS (SELECT 1 FROM estado WHERE nombre = 'Aprobado');
INSERT INTO estado (nombre) SELECT 'Bloqueado' WHERE NOT EXISTS (SELECT 1 FROM estado WHERE nombre = 'Bloqueado');
INSERT INTO estado (nombre) SELECT 'Cancelado' WHERE NOT EXISTS (SELECT 1 FROM estado WHERE nombre = 'Cancelado');
INSERT INTO estado (nombre) SELECT 'Urgente' WHERE NOT EXISTS (SELECT 1 FROM estado WHERE nombre = 'Urgente');
INSERT INTO estado (nombre) SELECT 'Critico' WHERE NOT EXISTS (SELECT 1 FROM estado WHERE nombre = 'Critico');
INSERT INTO estado (nombre) SELECT 'Cambios' WHERE NOT EXISTS (SELECT 1 FROM estado WHERE nombre = 'Cambios');

CREATE TABLE IF NOT EXISTS carpeta (
	id INTEGER NOT NULL UNIQUE,
	nombre VARCHAR(255) NOT NULL,
	padre INTEGER,
	PRIMARY KEY(id AUTOINCREMENT),
	FOREIGN KEY(padre) REFERENCES carpeta(id)
);

INSERT INTO carpeta (nombre, padre) SELECT 'Todos los presupuestos', NULL WHERE NOT EXISTS (SELECT 1 FROM carpeta WHERE nombre = 'Todos los presupuestos');
INSERT INTO carpeta (nombre, padre) SELECT 'Carpeta principal', NULL WHERE NOT EXISTS (SELECT 1 FROM carpeta WHERE nombre = 'Carpeta principal');
INSERT INTO carpeta (nombre, padre) SELECT 'Carpeta BA', 2 WHERE NOT EXISTS (SELECT 1 FROM carpeta WHERE nombre = 'Carpeta BA');
INSERT INTO carpeta (nombre, padre) SELECT 'Carpeta BB', 2 WHERE NOT EXISTS (SELECT 1 FROM carpeta WHERE nombre = 'Carpeta BB');
INSERT INTO carpeta (nombre, padre) SELECT 'Carpeta BC', 2 WHERE NOT EXISTS (SELECT 1 FROM carpeta WHERE nombre = 'Carpeta BC');


CREATE TABLE IF NOT EXISTS proyecto (
	id INTEGER NOT NULL UNIQUE,
    nombre VARCHAR(255) NOT NULL,
    estado INTEGER NOT NULL,
    carpeta INTEGER NOT NULL,
    PRIMARY KEY(id AUTOINCREMENT),
    FOREIGN KEY (estado) REFERENCES estado(id),
    FOREIGN KEY (carpeta) REFERENCES carpeta(id)
);

INSERT INTO proyecto (nombre, estado, carpeta) SELECT 'Proyecto A', 1, 2 WHERE NOT EXISTS (SELECT 1 FROM proyecto WHERE nombre = 'Proyecto A');
INSERT INTO proyecto (nombre, estado, carpeta) SELECT 'Proyecto B', 3, 2 WHERE NOT EXISTS (SELECT 1 FROM proyecto WHERE nombre = 'Proyecto B');
INSERT INTO proyecto (nombre, estado, carpeta) SELECT 'Proyecto C', 3, 3 WHERE NOT EXISTS (SELECT 1 FROM proyecto WHERE nombre = 'Proyecto C');
INSERT INTO proyecto (nombre, estado, carpeta) SELECT 'Proyecto D', 3, 3 WHERE NOT EXISTS (SELECT 1 FROM proyecto WHERE nombre = 'Proyecto D');
INSERT INTO proyecto (nombre, estado, carpeta) SELECT 'Proyecto E', 3, 3 WHERE NOT EXISTS (SELECT 1 FROM proyecto WHERE nombre = 'Proyecto E');
INSERT INTO proyecto (nombre, estado, carpeta) SELECT 'Proyecto F', 3, 4 WHERE NOT EXISTS (SELECT 1 FROM proyecto WHERE nombre = 'Proyecto F');
INSERT INTO proyecto (nombre, estado, carpeta) SELECT 'Proyecto G', 1, 4 WHERE NOT EXISTS (SELECT 1 FROM proyecto WHERE nombre = 'Proyecto G');
INSERT INTO proyecto (nombre, estado, carpeta) SELECT 'Proyecto H', 1, 4 WHERE NOT EXISTS (SELECT 1 FROM proyecto WHERE nombre = 'Proyecto H');
INSERT INTO proyecto (nombre, estado, carpeta) SELECT 'Proyecto i', 1, 3 WHERE NOT EXISTS (SELECT 1 FROM proyecto WHERE nombre = 'Proyecto i');
INSERT INTO proyecto (nombre, estado, carpeta) SELECT 'Proyecto j', 1, 5 WHERE NOT EXISTS (SELECT 1 FROM proyecto WHERE nombre = 'Proyecto j');
INSERT INTO proyecto (nombre, estado, carpeta) SELECT 'Proyecto k', 2, 5 WHERE NOT EXISTS (SELECT 1 FROM proyecto WHERE nombre = 'Proyecto k');


CREATE TABLE IF NOT EXISTS subPresupuesto (
	id INTEGER NOT NULL UNIQUE,
    nombre VARCHAR(255) NOT NULL,
    orden INTEGER NOT NULL,
    proyecto INTEGER NOT NULL,
    PRIMARY KEY(id AUTOINCREMENT),
    FOREIGN KEY (proyecto) REFERENCES proyecto(id)
);

INSERT INTO subPresupuesto (nombre, proyecto, orden) SELECT 'SubPresupuesto 01', 1, 1 WHERE NOT EXISTS (SELECT 1 FROM subPresupuesto WHERE nombre = 'SubPresupuesto 01');
INSERT INTO subPresupuesto (nombre, proyecto, orden) SELECT 'SubPresupuesto 02', 1, 2 WHERE NOT EXISTS (SELECT 1 FROM subPresupuesto WHERE nombre = 'SubPresupuesto 02');
INSERT INTO subPresupuesto (nombre, proyecto, orden) SELECT 'SubPresupuesto 03', 2, 1 WHERE NOT EXISTS (SELECT 1 FROM subPresupuesto WHERE nombre = 'SubPresupuesto 03');
INSERT INTO subPresupuesto (nombre, proyecto, orden) SELECT 'SubPresupuesto 04', 2, 2 WHERE NOT EXISTS (SELECT 1 FROM subPresupuesto WHERE nombre = 'SubPresupuesto 04');
INSERT INTO subPresupuesto (nombre, proyecto, orden) SELECT 'SubPresupuesto 05', 3, 1 WHERE NOT EXISTS (SELECT 1 FROM subPresupuesto WHERE nombre = 'SubPresupuesto 05');
INSERT INTO subPresupuesto (nombre, proyecto, orden) SELECT 'SubPresupuesto 06', 3, 2 WHERE NOT EXISTS (SELECT 1 FROM subPresupuesto WHERE nombre = 'SubPresupuesto 06');
INSERT INTO subPresupuesto (nombre, proyecto, orden) SELECT 'SubPresupuesto 07', 4, 1 WHERE NOT EXISTS (SELECT 1 FROM subPresupuesto WHERE nombre = 'SubPresupuesto 07');


CREATE TABLE IF NOT EXISTS tipoReferencia (
	id INTEGER NOT NULL UNIQUE,
    nombre VARCHAR(50) UNIQUE NOT NULL,
    PRIMARY KEY(id AUTOINCREMENT)
);

INSERT INTO tipoReferencia (nombre) SELECT 'Titulo' WHERE NOT EXISTS (SELECT 1 FROM tipoReferencia WHERE nombre = 'Titulo');
INSERT INTO tipoReferencia (nombre) SELECT 'Partida' WHERE NOT EXISTS (SELECT 1 FROM tipoReferencia WHERE nombre = 'Partida');


CREATE TABLE IF NOT EXISTS titulo (
	id INTEGER NOT NULL UNIQUE,
    nombre VARCHAR(50) UNIQUE NOT NULL,
    PRIMARY KEY(id AUTOINCREMENT)
);

INSERT INTO titulo (nombre) SELECT 'Titulo 1' WHERE NOT EXISTS (SELECT 1 FROM titulo WHERE nombre = 'Titulo 1');
INSERT INTO titulo (nombre) SELECT 'Titulo 1' WHERE NOT EXISTS (SELECT 1 FROM titulo WHERE nombre = 'Titulo 1');
INSERT INTO titulo (nombre) SELECT 'Titulo 1' WHERE NOT EXISTS (SELECT 1 FROM titulo WHERE nombre = 'Titulo 1');



CREATE TABLE IF NOT EXISTS partida (
	id INTEGER NOT NULL UNIQUE,
    nombre VARCHAR(50) UNIQUE NOT NULL,
    PRIMARY KEY(id AUTOINCREMENT)
);

INSERT INTO partida (nombre) SELECT 'Partida 1' WHERE NOT EXISTS (SELECT 1 FROM partida WHERE nombre = 'Partida 1');
INSERT INTO partida (nombre) SELECT 'Partida 2' WHERE NOT EXISTS (SELECT 1 FROM partida WHERE nombre = 'Partida 2');
INSERT INTO partida (nombre) SELECT 'Partida 3' WHERE NOT EXISTS (SELECT 1 FROM partida WHERE nombre = 'Partida 3');


CREATE TABLE IF NOT EXISTS casilla (
	id INTEGER NOT NULL UNIQUE,
	padre INTEGER,
	subPresupuesto INTEGER NOT NULL,
    elementoId INTEGER NOT NULL,
    tipoReferencia INTEGER NOT NULL,

    PRIMARY KEY (id AUTOINCREMENT),
    FOREIGN KEY (padre) REFERENCES carpeta(id),
    FOREIGN KEY (subPresupuesto) REFERENCES subPresupuesto(id),
    FOREIGN KEY (tipoReferencia) REFERENCES tipoReferencia(id)
);

INSERT INTO casilla (padre, subPresupuesto, elementoId, tipoReferencia) SELECT NULL, 1, 1, 1 WHERE NOT EXISTS (SELECT 1 FROM casilla WHERE id = 1);
INSERT INTO casilla (padre, subPresupuesto, elementoId, tipoReferencia) SELECT NULL, 1, 2, 1 WHERE NOT EXISTS (SELECT 1 FROM casilla WHERE id = 2);
INSERT INTO casilla (padre, subPresupuesto, elementoId, tipoReferencia) SELECT 1 , 1, 3, 2 WHERE NOT EXISTS (SELECT 1 FROM casilla WHERE id = 3);
INSERT INTO casilla (padre, subPresupuesto, elementoId, tipoReferencia) SELECT NULL, 2, 1, 1 WHERE NOT EXISTS (SELECT 1 FROM casilla WHERE id = 4);
INSERT INTO casilla (padre, subPresupuesto, elementoId, tipoReferencia) SELECT NULL, 2, 2, 2 WHERE NOT EXISTS (SELECT 1 FROM casilla WHERE id = 5);
INSERT INTO casilla (padre, subPresupuesto, elementoId, tipoReferencia) SELECT 4 , 2, 3, 1 WHERE NOT EXISTS (SELECT 1 FROM casilla WHERE id = 6);
INSERT INTO casilla (padre, subPresupuesto, elementoId, tipoReferencia) SELECT 4 , 2, 1, 2 WHERE NOT EXISTS (SELECT 1 FROM casilla WHERE id = 7);

