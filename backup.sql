--
-- PostgreSQL database dump
--

\restrict 2ZIFbmApCrgIwNvrlGsYniotP7Qlf75vNfoo6roBgVgKPt8ZubNuRmS69Gx7Urb

-- Dumped from database version 17.6 (Debian 17.6-1.pgdg12+1)
-- Dumped by pg_dump version 17.6 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: bd_postgres_farmacare_user
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO bd_postgres_farmacare_user;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: ajustes_inventario; Type: TABLE; Schema: public; Owner: bd_postgres_farmacare_user
--

CREATE TABLE public.ajustes_inventario (
    id integer NOT NULL,
    producto_id integer,
    tipo_producto character varying(20),
    cantidad_ajustada integer NOT NULL,
    motivo character varying(255),
    fecha_ajuste timestamp without time zone,
    usuario_id integer
);


ALTER TABLE public.ajustes_inventario OWNER TO bd_postgres_farmacare_user;

--
-- Name: ajustes_inventario_id_seq; Type: SEQUENCE; Schema: public; Owner: bd_postgres_farmacare_user
--

CREATE SEQUENCE public.ajustes_inventario_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.ajustes_inventario_id_seq OWNER TO bd_postgres_farmacare_user;

--
-- Name: ajustes_inventario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER SEQUENCE public.ajustes_inventario_id_seq OWNED BY public.ajustes_inventario.id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: bd_postgres_farmacare_user
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO bd_postgres_farmacare_user;

--
-- Name: clientes; Type: TABLE; Schema: public; Owner: bd_postgres_farmacare_user
--

CREATE TABLE public.clientes (
    id integer NOT NULL,
    rfc character varying(20) NOT NULL,
    nombre character varying(100) NOT NULL,
    telefono character varying(15),
    direccion character varying(200)
);


ALTER TABLE public.clientes OWNER TO bd_postgres_farmacare_user;

--
-- Name: clientes_id_seq; Type: SEQUENCE; Schema: public; Owner: bd_postgres_farmacare_user
--

CREATE SEQUENCE public.clientes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.clientes_id_seq OWNER TO bd_postgres_farmacare_user;

--
-- Name: clientes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER SEQUENCE public.clientes_id_seq OWNED BY public.clientes.id;


--
-- Name: compras; Type: TABLE; Schema: public; Owner: bd_postgres_farmacare_user
--

CREATE TABLE public.compras (
    id integer NOT NULL,
    fecha_compra timestamp without time zone,
    proveedor_id integer NOT NULL,
    total double precision NOT NULL,
    usuario_id integer
);


ALTER TABLE public.compras OWNER TO bd_postgres_farmacare_user;

--
-- Name: compras_id_seq; Type: SEQUENCE; Schema: public; Owner: bd_postgres_farmacare_user
--

CREATE SEQUENCE public.compras_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.compras_id_seq OWNER TO bd_postgres_farmacare_user;

--
-- Name: compras_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER SEQUENCE public.compras_id_seq OWNED BY public.compras.id;


--
-- Name: dispositivos_medicos; Type: TABLE; Schema: public; Owner: bd_postgres_farmacare_user
--

CREATE TABLE public.dispositivos_medicos (
    id integer NOT NULL,
    codigo_barras character varying(50) NOT NULL,
    nombre_comercial character varying(100) NOT NULL,
    nombre_comun character varying(100),
    laboratorio character varying(100),
    presentacion character varying(50),
    iva double precision,
    precio_venta double precision NOT NULL,
    stock integer,
    fecha_modificacion timestamp without time zone
);


ALTER TABLE public.dispositivos_medicos OWNER TO bd_postgres_farmacare_user;

--
-- Name: dispositivos_medicos_id_seq; Type: SEQUENCE; Schema: public; Owner: bd_postgres_farmacare_user
--

CREATE SEQUENCE public.dispositivos_medicos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.dispositivos_medicos_id_seq OWNER TO bd_postgres_farmacare_user;

--
-- Name: dispositivos_medicos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER SEQUENCE public.dispositivos_medicos_id_seq OWNED BY public.dispositivos_medicos.id;


--
-- Name: entradas; Type: TABLE; Schema: public; Owner: bd_postgres_farmacare_user
--

CREATE TABLE public.entradas (
    id integer NOT NULL,
    compra_id integer,
    producto_id integer,
    tipo_producto character varying(20),
    cantidad integer NOT NULL,
    importe_unitario double precision NOT NULL,
    importe_antes_iva double precision NOT NULL,
    iva_porcentaje double precision NOT NULL,
    valor_iva double precision NOT NULL,
    importe_total double precision NOT NULL
);


ALTER TABLE public.entradas OWNER TO bd_postgres_farmacare_user;

--
-- Name: entradas_id_seq; Type: SEQUENCE; Schema: public; Owner: bd_postgres_farmacare_user
--

CREATE SEQUENCE public.entradas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.entradas_id_seq OWNER TO bd_postgres_farmacare_user;

--
-- Name: entradas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER SEQUENCE public.entradas_id_seq OWNED BY public.entradas.id;


--
-- Name: inventario; Type: TABLE; Schema: public; Owner: bd_postgres_farmacare_user
--

CREATE TABLE public.inventario (
    id integer NOT NULL,
    producto_id integer,
    tipo_producto character varying(20),
    cantidad integer,
    inventario_valor double precision,
    punto_reorden integer,
    cantidad_faltante integer,
    fecha_modificacion timestamp without time zone
);


ALTER TABLE public.inventario OWNER TO bd_postgres_farmacare_user;

--
-- Name: inventario_id_seq; Type: SEQUENCE; Schema: public; Owner: bd_postgres_farmacare_user
--

CREATE SEQUENCE public.inventario_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.inventario_id_seq OWNER TO bd_postgres_farmacare_user;

--
-- Name: inventario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER SEQUENCE public.inventario_id_seq OWNED BY public.inventario.id;


--
-- Name: medicamentos; Type: TABLE; Schema: public; Owner: bd_postgres_farmacare_user
--

CREATE TABLE public.medicamentos (
    id integer NOT NULL,
    codigo_barras character varying(50) NOT NULL,
    nombre_comercial character varying(100) NOT NULL,
    nombre_generico character varying(100),
    laboratorio character varying(100),
    presentacion character varying(50),
    grupo character varying(20),
    iva double precision,
    precio_venta double precision NOT NULL,
    stock integer,
    fecha_modificacion timestamp without time zone
);


ALTER TABLE public.medicamentos OWNER TO bd_postgres_farmacare_user;

--
-- Name: medicamentos_id_seq; Type: SEQUENCE; Schema: public; Owner: bd_postgres_farmacare_user
--

CREATE SEQUENCE public.medicamentos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.medicamentos_id_seq OWNER TO bd_postgres_farmacare_user;

--
-- Name: medicamentos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER SEQUENCE public.medicamentos_id_seq OWNED BY public.medicamentos.id;


--
-- Name: no_hay; Type: TABLE; Schema: public; Owner: bd_postgres_farmacare_user
--

CREATE TABLE public.no_hay (
    id integer NOT NULL,
    nombre character varying(100) NOT NULL,
    tipo character varying(50),
    descripcion character varying(255),
    fecha_registro timestamp without time zone
);


ALTER TABLE public.no_hay OWNER TO bd_postgres_farmacare_user;

--
-- Name: no_hay_id_seq; Type: SEQUENCE; Schema: public; Owner: bd_postgres_farmacare_user
--

CREATE SEQUENCE public.no_hay_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.no_hay_id_seq OWNER TO bd_postgres_farmacare_user;

--
-- Name: no_hay_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER SEQUENCE public.no_hay_id_seq OWNED BY public.no_hay.id;


--
-- Name: proveedores; Type: TABLE; Schema: public; Owner: bd_postgres_farmacare_user
--

CREATE TABLE public.proveedores (
    id integer NOT NULL,
    nombre character varying(100) NOT NULL,
    rfc character varying(20),
    direccion character varying(200),
    telefono character varying(20),
    email character varying(100)
);


ALTER TABLE public.proveedores OWNER TO bd_postgres_farmacare_user;

--
-- Name: proveedores_id_seq; Type: SEQUENCE; Schema: public; Owner: bd_postgres_farmacare_user
--

CREATE SEQUENCE public.proveedores_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.proveedores_id_seq OWNER TO bd_postgres_farmacare_user;

--
-- Name: proveedores_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER SEQUENCE public.proveedores_id_seq OWNED BY public.proveedores.id;


--
-- Name: salidas; Type: TABLE; Schema: public; Owner: bd_postgres_farmacare_user
--

CREATE TABLE public.salidas (
    id integer NOT NULL,
    venta_id integer,
    producto_id integer,
    tipo_producto character varying(20),
    cantidad integer NOT NULL,
    importe_unitario double precision NOT NULL,
    importe_antes_iva double precision NOT NULL,
    iva_porcentaje double precision NOT NULL,
    valor_iva double precision NOT NULL,
    importe_total double precision NOT NULL
);


ALTER TABLE public.salidas OWNER TO bd_postgres_farmacare_user;

--
-- Name: salidas_id_seq; Type: SEQUENCE; Schema: public; Owner: bd_postgres_farmacare_user
--

CREATE SEQUENCE public.salidas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.salidas_id_seq OWNER TO bd_postgres_farmacare_user;

--
-- Name: salidas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER SEQUENCE public.salidas_id_seq OWNED BY public.salidas.id;


--
-- Name: usuarios; Type: TABLE; Schema: public; Owner: bd_postgres_farmacare_user
--

CREATE TABLE public.usuarios (
    id integer NOT NULL,
    nombre character varying(100) NOT NULL,
    rol character varying(20) NOT NULL,
    "contraseña" character varying(200) NOT NULL,
    fecha_creacion timestamp without time zone
);


ALTER TABLE public.usuarios OWNER TO bd_postgres_farmacare_user;

--
-- Name: usuarios_id_seq; Type: SEQUENCE; Schema: public; Owner: bd_postgres_farmacare_user
--

CREATE SEQUENCE public.usuarios_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.usuarios_id_seq OWNER TO bd_postgres_farmacare_user;

--
-- Name: usuarios_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER SEQUENCE public.usuarios_id_seq OWNED BY public.usuarios.id;


--
-- Name: ventas; Type: TABLE; Schema: public; Owner: bd_postgres_farmacare_user
--

CREATE TABLE public.ventas (
    id integer NOT NULL,
    fecha timestamp without time zone,
    cliente_id integer,
    total double precision NOT NULL,
    usuario_id integer
);


ALTER TABLE public.ventas OWNER TO bd_postgres_farmacare_user;

--
-- Name: ventas_id_seq; Type: SEQUENCE; Schema: public; Owner: bd_postgres_farmacare_user
--

CREATE SEQUENCE public.ventas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.ventas_id_seq OWNER TO bd_postgres_farmacare_user;

--
-- Name: ventas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER SEQUENCE public.ventas_id_seq OWNED BY public.ventas.id;


--
-- Name: ajustes_inventario id; Type: DEFAULT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.ajustes_inventario ALTER COLUMN id SET DEFAULT nextval('public.ajustes_inventario_id_seq'::regclass);


--
-- Name: clientes id; Type: DEFAULT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.clientes ALTER COLUMN id SET DEFAULT nextval('public.clientes_id_seq'::regclass);


--
-- Name: compras id; Type: DEFAULT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.compras ALTER COLUMN id SET DEFAULT nextval('public.compras_id_seq'::regclass);


--
-- Name: dispositivos_medicos id; Type: DEFAULT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.dispositivos_medicos ALTER COLUMN id SET DEFAULT nextval('public.dispositivos_medicos_id_seq'::regclass);


--
-- Name: entradas id; Type: DEFAULT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.entradas ALTER COLUMN id SET DEFAULT nextval('public.entradas_id_seq'::regclass);


--
-- Name: inventario id; Type: DEFAULT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.inventario ALTER COLUMN id SET DEFAULT nextval('public.inventario_id_seq'::regclass);


--
-- Name: medicamentos id; Type: DEFAULT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.medicamentos ALTER COLUMN id SET DEFAULT nextval('public.medicamentos_id_seq'::regclass);


--
-- Name: no_hay id; Type: DEFAULT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.no_hay ALTER COLUMN id SET DEFAULT nextval('public.no_hay_id_seq'::regclass);


--
-- Name: proveedores id; Type: DEFAULT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.proveedores ALTER COLUMN id SET DEFAULT nextval('public.proveedores_id_seq'::regclass);


--
-- Name: salidas id; Type: DEFAULT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.salidas ALTER COLUMN id SET DEFAULT nextval('public.salidas_id_seq'::regclass);


--
-- Name: usuarios id; Type: DEFAULT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.usuarios ALTER COLUMN id SET DEFAULT nextval('public.usuarios_id_seq'::regclass);


--
-- Name: ventas id; Type: DEFAULT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.ventas ALTER COLUMN id SET DEFAULT nextval('public.ventas_id_seq'::regclass);


--
-- Data for Name: ajustes_inventario; Type: TABLE DATA; Schema: public; Owner: bd_postgres_farmacare_user
--

COPY public.ajustes_inventario (id, producto_id, tipo_producto, cantidad_ajustada, motivo, fecha_ajuste, usuario_id) FROM stdin;
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: bd_postgres_farmacare_user
--

COPY public.alembic_version (version_num) FROM stdin;
\.


--
-- Data for Name: clientes; Type: TABLE DATA; Schema: public; Owner: bd_postgres_farmacare_user
--

COPY public.clientes (id, rfc, nombre, telefono, direccion) FROM stdin;
\.


--
-- Data for Name: compras; Type: TABLE DATA; Schema: public; Owner: bd_postgres_farmacare_user
--

COPY public.compras (id, fecha_compra, proveedor_id, total, usuario_id) FROM stdin;
\.


--
-- Data for Name: dispositivos_medicos; Type: TABLE DATA; Schema: public; Owner: bd_postgres_farmacare_user
--

COPY public.dispositivos_medicos (id, codigo_barras, nombre_comercial, nombre_comun, laboratorio, presentacion, iva, precio_venta, stock, fecha_modificacion) FROM stdin;
\.


--
-- Data for Name: entradas; Type: TABLE DATA; Schema: public; Owner: bd_postgres_farmacare_user
--

COPY public.entradas (id, compra_id, producto_id, tipo_producto, cantidad, importe_unitario, importe_antes_iva, iva_porcentaje, valor_iva, importe_total) FROM stdin;
\.


--
-- Data for Name: inventario; Type: TABLE DATA; Schema: public; Owner: bd_postgres_farmacare_user
--

COPY public.inventario (id, producto_id, tipo_producto, cantidad, inventario_valor, punto_reorden, cantidad_faltante, fecha_modificacion) FROM stdin;
\.


--
-- Data for Name: medicamentos; Type: TABLE DATA; Schema: public; Owner: bd_postgres_farmacare_user
--

COPY public.medicamentos (id, codigo_barras, nombre_comercial, nombre_generico, laboratorio, presentacion, grupo, iva, precio_venta, stock, fecha_modificacion) FROM stdin;
\.


--
-- Data for Name: no_hay; Type: TABLE DATA; Schema: public; Owner: bd_postgres_farmacare_user
--

COPY public.no_hay (id, nombre, tipo, descripcion, fecha_registro) FROM stdin;
\.


--
-- Data for Name: proveedores; Type: TABLE DATA; Schema: public; Owner: bd_postgres_farmacare_user
--

COPY public.proveedores (id, nombre, rfc, direccion, telefono, email) FROM stdin;
\.


--
-- Data for Name: salidas; Type: TABLE DATA; Schema: public; Owner: bd_postgres_farmacare_user
--

COPY public.salidas (id, venta_id, producto_id, tipo_producto, cantidad, importe_unitario, importe_antes_iva, iva_porcentaje, valor_iva, importe_total) FROM stdin;
\.


--
-- Data for Name: usuarios; Type: TABLE DATA; Schema: public; Owner: bd_postgres_farmacare_user
--

COPY public.usuarios (id, nombre, rol, "contraseña", fecha_creacion) FROM stdin;
1	admin	Administrador	scrypt:32768:8:1$WQko8sUiBkdiWAOA$f95ee6e8129a598a18d60fadfad9e09c68992ff56143f61062df4165dbaf3b7df4aede3b1ae60cb9c767d2d4e620699f33f18ae47e959f427ea4a9ab4b47575d	2025-08-28 20:34:08.460976
2	victoria iste	cajero	scrypt:32768:8:1$zVJQ89Oalg8jfyCp$0b859b2484d094fc46096670ccb03b0ed0123d3fe2d8ec57595d712dda25631e0aba21d9c00b55e34c24c53bbce57ced27d6c3c615394bbd271f58063a0c0237	2025-08-28 20:35:22.660792
\.


--
-- Data for Name: ventas; Type: TABLE DATA; Schema: public; Owner: bd_postgres_farmacare_user
--

COPY public.ventas (id, fecha, cliente_id, total, usuario_id) FROM stdin;
\.


--
-- Name: ajustes_inventario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bd_postgres_farmacare_user
--

SELECT pg_catalog.setval('public.ajustes_inventario_id_seq', 1, false);


--
-- Name: clientes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bd_postgres_farmacare_user
--

SELECT pg_catalog.setval('public.clientes_id_seq', 1, false);


--
-- Name: compras_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bd_postgres_farmacare_user
--

SELECT pg_catalog.setval('public.compras_id_seq', 1, false);


--
-- Name: dispositivos_medicos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bd_postgres_farmacare_user
--

SELECT pg_catalog.setval('public.dispositivos_medicos_id_seq', 1, false);


--
-- Name: entradas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bd_postgres_farmacare_user
--

SELECT pg_catalog.setval('public.entradas_id_seq', 1, false);


--
-- Name: inventario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bd_postgres_farmacare_user
--

SELECT pg_catalog.setval('public.inventario_id_seq', 1, false);


--
-- Name: medicamentos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bd_postgres_farmacare_user
--

SELECT pg_catalog.setval('public.medicamentos_id_seq', 1, false);


--
-- Name: no_hay_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bd_postgres_farmacare_user
--

SELECT pg_catalog.setval('public.no_hay_id_seq', 1, false);


--
-- Name: proveedores_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bd_postgres_farmacare_user
--

SELECT pg_catalog.setval('public.proveedores_id_seq', 1, false);


--
-- Name: salidas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bd_postgres_farmacare_user
--

SELECT pg_catalog.setval('public.salidas_id_seq', 1, false);


--
-- Name: usuarios_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bd_postgres_farmacare_user
--

SELECT pg_catalog.setval('public.usuarios_id_seq', 2, true);


--
-- Name: ventas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bd_postgres_farmacare_user
--

SELECT pg_catalog.setval('public.ventas_id_seq', 1, false);


--
-- Name: ajustes_inventario ajustes_inventario_pkey; Type: CONSTRAINT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.ajustes_inventario
    ADD CONSTRAINT ajustes_inventario_pkey PRIMARY KEY (id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: clientes clientes_pkey; Type: CONSTRAINT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.clientes
    ADD CONSTRAINT clientes_pkey PRIMARY KEY (id);


--
-- Name: clientes clientes_rfc_key; Type: CONSTRAINT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.clientes
    ADD CONSTRAINT clientes_rfc_key UNIQUE (rfc);


--
-- Name: compras compras_pkey; Type: CONSTRAINT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.compras
    ADD CONSTRAINT compras_pkey PRIMARY KEY (id);


--
-- Name: dispositivos_medicos dispositivos_medicos_codigo_barras_key; Type: CONSTRAINT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.dispositivos_medicos
    ADD CONSTRAINT dispositivos_medicos_codigo_barras_key UNIQUE (codigo_barras);


--
-- Name: dispositivos_medicos dispositivos_medicos_pkey; Type: CONSTRAINT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.dispositivos_medicos
    ADD CONSTRAINT dispositivos_medicos_pkey PRIMARY KEY (id);


--
-- Name: entradas entradas_pkey; Type: CONSTRAINT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.entradas
    ADD CONSTRAINT entradas_pkey PRIMARY KEY (id);


--
-- Name: inventario inventario_pkey; Type: CONSTRAINT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.inventario
    ADD CONSTRAINT inventario_pkey PRIMARY KEY (id);


--
-- Name: medicamentos medicamentos_codigo_barras_key; Type: CONSTRAINT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.medicamentos
    ADD CONSTRAINT medicamentos_codigo_barras_key UNIQUE (codigo_barras);


--
-- Name: medicamentos medicamentos_pkey; Type: CONSTRAINT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.medicamentos
    ADD CONSTRAINT medicamentos_pkey PRIMARY KEY (id);


--
-- Name: no_hay no_hay_pkey; Type: CONSTRAINT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.no_hay
    ADD CONSTRAINT no_hay_pkey PRIMARY KEY (id);


--
-- Name: proveedores proveedores_pkey; Type: CONSTRAINT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.proveedores
    ADD CONSTRAINT proveedores_pkey PRIMARY KEY (id);


--
-- Name: proveedores proveedores_rfc_key; Type: CONSTRAINT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.proveedores
    ADD CONSTRAINT proveedores_rfc_key UNIQUE (rfc);


--
-- Name: salidas salidas_pkey; Type: CONSTRAINT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.salidas
    ADD CONSTRAINT salidas_pkey PRIMARY KEY (id);


--
-- Name: usuarios usuarios_nombre_key; Type: CONSTRAINT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_nombre_key UNIQUE (nombre);


--
-- Name: usuarios usuarios_pkey; Type: CONSTRAINT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_pkey PRIMARY KEY (id);


--
-- Name: ventas ventas_pkey; Type: CONSTRAINT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.ventas
    ADD CONSTRAINT ventas_pkey PRIMARY KEY (id);


--
-- Name: ajustes_inventario ajustes_inventario_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.ajustes_inventario
    ADD CONSTRAINT ajustes_inventario_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuarios(id);


--
-- Name: compras compras_proveedor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.compras
    ADD CONSTRAINT compras_proveedor_id_fkey FOREIGN KEY (proveedor_id) REFERENCES public.proveedores(id);


--
-- Name: compras compras_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.compras
    ADD CONSTRAINT compras_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuarios(id);


--
-- Name: entradas entradas_compra_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.entradas
    ADD CONSTRAINT entradas_compra_id_fkey FOREIGN KEY (compra_id) REFERENCES public.compras(id);


--
-- Name: salidas salidas_venta_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.salidas
    ADD CONSTRAINT salidas_venta_id_fkey FOREIGN KEY (venta_id) REFERENCES public.ventas(id);


--
-- Name: ventas ventas_cliente_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.ventas
    ADD CONSTRAINT ventas_cliente_id_fkey FOREIGN KEY (cliente_id) REFERENCES public.clientes(id);


--
-- Name: ventas ventas_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: bd_postgres_farmacare_user
--

ALTER TABLE ONLY public.ventas
    ADD CONSTRAINT ventas_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuarios(id);


--
-- Name: DEFAULT PRIVILEGES FOR SEQUENCES; Type: DEFAULT ACL; Schema: -; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres GRANT ALL ON SEQUENCES TO bd_postgres_farmacare_user;


--
-- Name: DEFAULT PRIVILEGES FOR TYPES; Type: DEFAULT ACL; Schema: -; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres GRANT ALL ON TYPES TO bd_postgres_farmacare_user;


--
-- Name: DEFAULT PRIVILEGES FOR FUNCTIONS; Type: DEFAULT ACL; Schema: -; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres GRANT ALL ON FUNCTIONS TO bd_postgres_farmacare_user;


--
-- Name: DEFAULT PRIVILEGES FOR TABLES; Type: DEFAULT ACL; Schema: -; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres GRANT ALL ON TABLES TO bd_postgres_farmacare_user;


--
-- PostgreSQL database dump complete
--

\unrestrict 2ZIFbmApCrgIwNvrlGsYniotP7Qlf75vNfoo6roBgVgKPt8ZubNuRmS69Gx7Urb

