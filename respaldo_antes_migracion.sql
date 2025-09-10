--
-- PostgreSQL database dump
--

\restrict uC0eJn7b3amIgfdSEPppS8KNq8Jatpc8W7lJCROayD6DOBUU6yCYJyxTzhb2mlM

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
-- Name: public; Type: SCHEMA; Schema: -; Owner: nueva_farmacare_db_user
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO nueva_farmacare_db_user;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: ajustes_inventario; Type: TABLE; Schema: public; Owner: nueva_farmacare_db_user
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


ALTER TABLE public.ajustes_inventario OWNER TO nueva_farmacare_db_user;

--
-- Name: ajustes_inventario_id_seq; Type: SEQUENCE; Schema: public; Owner: nueva_farmacare_db_user
--

CREATE SEQUENCE public.ajustes_inventario_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.ajustes_inventario_id_seq OWNER TO nueva_farmacare_db_user;

--
-- Name: ajustes_inventario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER SEQUENCE public.ajustes_inventario_id_seq OWNED BY public.ajustes_inventario.id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: nueva_farmacare_db_user
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO nueva_farmacare_db_user;

--
-- Name: clientes; Type: TABLE; Schema: public; Owner: nueva_farmacare_db_user
--

CREATE TABLE public.clientes (
    id integer NOT NULL,
    rfc character varying(20),
    nombre character varying(150) NOT NULL,
    telefono character varying(20),
    direccion character varying(200),
    email character varying(100),
    contacto character varying(100),
    telefono_contacto character varying(20),
    fecha_creacion timestamp without time zone,
    fecha_modificacion timestamp without time zone
);


ALTER TABLE public.clientes OWNER TO nueva_farmacare_db_user;

--
-- Name: clientes_id_seq; Type: SEQUENCE; Schema: public; Owner: nueva_farmacare_db_user
--

CREATE SEQUENCE public.clientes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.clientes_id_seq OWNER TO nueva_farmacare_db_user;

--
-- Name: clientes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER SEQUENCE public.clientes_id_seq OWNED BY public.clientes.id;


--
-- Name: compras; Type: TABLE; Schema: public; Owner: nueva_farmacare_db_user
--

CREATE TABLE public.compras (
    id integer NOT NULL,
    fecha_compra timestamp without time zone,
    proveedor_id integer NOT NULL,
    total double precision NOT NULL,
    usuario_id integer,
    folio_factura character varying(100)
);


ALTER TABLE public.compras OWNER TO nueva_farmacare_db_user;

--
-- Name: compras_id_seq; Type: SEQUENCE; Schema: public; Owner: nueva_farmacare_db_user
--

CREATE SEQUENCE public.compras_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.compras_id_seq OWNER TO nueva_farmacare_db_user;

--
-- Name: compras_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER SEQUENCE public.compras_id_seq OWNED BY public.compras.id;


--
-- Name: detalle_compra; Type: TABLE; Schema: public; Owner: nueva_farmacare_db_user
--

CREATE TABLE public.detalle_compra (
    id integer NOT NULL,
    compra_id integer NOT NULL,
    producto_id integer NOT NULL,
    cantidad integer NOT NULL,
    precio_unitario double precision NOT NULL,
    precio_sin_iva double precision NOT NULL,
    importe double precision NOT NULL,
    descuento double precision NOT NULL,
    iva double precision NOT NULL
);


ALTER TABLE public.detalle_compra OWNER TO nueva_farmacare_db_user;

--
-- Name: detalle_compra_id_seq; Type: SEQUENCE; Schema: public; Owner: nueva_farmacare_db_user
--

CREATE SEQUENCE public.detalle_compra_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.detalle_compra_id_seq OWNER TO nueva_farmacare_db_user;

--
-- Name: detalle_compra_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER SEQUENCE public.detalle_compra_id_seq OWNED BY public.detalle_compra.id;


--
-- Name: dispositivos_medicos; Type: TABLE; Schema: public; Owner: nueva_farmacare_db_user
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
    fecha_modificacion timestamp without time zone,
    descuento double precision,
    activo boolean
);


ALTER TABLE public.dispositivos_medicos OWNER TO nueva_farmacare_db_user;

--
-- Name: dispositivos_medicos_id_seq; Type: SEQUENCE; Schema: public; Owner: nueva_farmacare_db_user
--

CREATE SEQUENCE public.dispositivos_medicos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.dispositivos_medicos_id_seq OWNER TO nueva_farmacare_db_user;

--
-- Name: dispositivos_medicos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER SEQUENCE public.dispositivos_medicos_id_seq OWNED BY public.dispositivos_medicos.id;


--
-- Name: entradas; Type: TABLE; Schema: public; Owner: nueva_farmacare_db_user
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


ALTER TABLE public.entradas OWNER TO nueva_farmacare_db_user;

--
-- Name: entradas_id_seq; Type: SEQUENCE; Schema: public; Owner: nueva_farmacare_db_user
--

CREATE SEQUENCE public.entradas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.entradas_id_seq OWNER TO nueva_farmacare_db_user;

--
-- Name: entradas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER SEQUENCE public.entradas_id_seq OWNED BY public.entradas.id;


--
-- Name: inventario; Type: TABLE; Schema: public; Owner: nueva_farmacare_db_user
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


ALTER TABLE public.inventario OWNER TO nueva_farmacare_db_user;

--
-- Name: inventario_id_seq; Type: SEQUENCE; Schema: public; Owner: nueva_farmacare_db_user
--

CREATE SEQUENCE public.inventario_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.inventario_id_seq OWNER TO nueva_farmacare_db_user;

--
-- Name: inventario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER SEQUENCE public.inventario_id_seq OWNED BY public.inventario.id;


--
-- Name: medicamentos; Type: TABLE; Schema: public; Owner: nueva_farmacare_db_user
--

CREATE TABLE public.medicamentos (
    id integer NOT NULL,
    codigo_barras character varying(50) NOT NULL,
    nombre_comercial character varying(150) NOT NULL,
    nombre_generico character varying(150) NOT NULL,
    laboratorio character varying(100) NOT NULL,
    presentacion character varying(100) NOT NULL,
    grupo character varying(50) NOT NULL,
    iva double precision,
    precio_venta double precision NOT NULL,
    stock integer,
    fecha_modificacion timestamp without time zone,
    descuento double precision,
    activo boolean,
    punto_reorden integer,
    fecha_creacion timestamp without time zone
);


ALTER TABLE public.medicamentos OWNER TO nueva_farmacare_db_user;

--
-- Name: medicamentos_id_seq; Type: SEQUENCE; Schema: public; Owner: nueva_farmacare_db_user
--

CREATE SEQUENCE public.medicamentos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.medicamentos_id_seq OWNER TO nueva_farmacare_db_user;

--
-- Name: medicamentos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER SEQUENCE public.medicamentos_id_seq OWNED BY public.medicamentos.id;


--
-- Name: no_hay; Type: TABLE; Schema: public; Owner: nueva_farmacare_db_user
--

CREATE TABLE public.no_hay (
    id integer NOT NULL,
    nombre character varying(100) NOT NULL,
    tipo character varying(50) NOT NULL,
    descripcion text,
    fecha_creacion timestamp without time zone,
    fecha_modificacion timestamp without time zone
);


ALTER TABLE public.no_hay OWNER TO nueva_farmacare_db_user;

--
-- Name: no_hay_id_seq; Type: SEQUENCE; Schema: public; Owner: nueva_farmacare_db_user
--

CREATE SEQUENCE public.no_hay_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.no_hay_id_seq OWNER TO nueva_farmacare_db_user;

--
-- Name: no_hay_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER SEQUENCE public.no_hay_id_seq OWNED BY public.no_hay.id;


--
-- Name: productos; Type: TABLE; Schema: public; Owner: nueva_farmacare_db_user
--

CREATE TABLE public.productos (
    id integer NOT NULL,
    nombre character varying(100) NOT NULL,
    descripcion character varying(250),
    stock integer,
    precio double precision NOT NULL,
    proveedor_id integer,
    fecha_creacion timestamp without time zone
);


ALTER TABLE public.productos OWNER TO nueva_farmacare_db_user;

--
-- Name: productos_id_seq; Type: SEQUENCE; Schema: public; Owner: nueva_farmacare_db_user
--

CREATE SEQUENCE public.productos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.productos_id_seq OWNER TO nueva_farmacare_db_user;

--
-- Name: productos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER SEQUENCE public.productos_id_seq OWNED BY public.productos.id;


--
-- Name: proveedores; Type: TABLE; Schema: public; Owner: nueva_farmacare_db_user
--

CREATE TABLE public.proveedores (
    id integer NOT NULL,
    nombre character varying(150) NOT NULL,
    rfc character varying(20),
    direccion character varying(200),
    telefono character varying(20),
    email character varying(100),
    contacto character varying(100),
    telefono_contacto character varying(20),
    fecha_creacion timestamp without time zone,
    fecha_modificacion timestamp without time zone
);


ALTER TABLE public.proveedores OWNER TO nueva_farmacare_db_user;

--
-- Name: proveedores_id_seq; Type: SEQUENCE; Schema: public; Owner: nueva_farmacare_db_user
--

CREATE SEQUENCE public.proveedores_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.proveedores_id_seq OWNER TO nueva_farmacare_db_user;

--
-- Name: proveedores_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER SEQUENCE public.proveedores_id_seq OWNED BY public.proveedores.id;


--
-- Name: salidas; Type: TABLE; Schema: public; Owner: nueva_farmacare_db_user
--

CREATE TABLE public.salidas (
    id integer NOT NULL,
    venta_id integer,
    producto_id integer NOT NULL,
    cantidad integer NOT NULL,
    importe_unitario double precision NOT NULL,
    importe_antes_iva double precision NOT NULL,
    iva_porcentaje double precision,
    valor_iva double precision,
    importe_total double precision NOT NULL,
    fecha timestamp without time zone,
    producto_tipo character varying(20) NOT NULL,
    cliente_id integer,
    usuario_id integer NOT NULL,
    eliminada boolean
);


ALTER TABLE public.salidas OWNER TO nueva_farmacare_db_user;

--
-- Name: salidas_id_seq; Type: SEQUENCE; Schema: public; Owner: nueva_farmacare_db_user
--

CREATE SEQUENCE public.salidas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.salidas_id_seq OWNER TO nueva_farmacare_db_user;

--
-- Name: salidas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER SEQUENCE public.salidas_id_seq OWNED BY public.salidas.id;


--
-- Name: usuarios; Type: TABLE; Schema: public; Owner: nueva_farmacare_db_user
--

CREATE TABLE public.usuarios (
    id integer NOT NULL,
    nombre character varying(100) NOT NULL,
    rol character varying(20) NOT NULL,
    "contraseña" character varying(255) NOT NULL,
    fecha_creacion timestamp without time zone,
    fecha_modificacion timestamp without time zone,
    activo boolean
);


ALTER TABLE public.usuarios OWNER TO nueva_farmacare_db_user;

--
-- Name: usuarios_id_seq; Type: SEQUENCE; Schema: public; Owner: nueva_farmacare_db_user
--

CREATE SEQUENCE public.usuarios_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.usuarios_id_seq OWNER TO nueva_farmacare_db_user;

--
-- Name: usuarios_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER SEQUENCE public.usuarios_id_seq OWNED BY public.usuarios.id;


--
-- Name: ventas; Type: TABLE; Schema: public; Owner: nueva_farmacare_db_user
--

CREATE TABLE public.ventas (
    id integer NOT NULL,
    fecha timestamp without time zone,
    cliente_id integer,
    total double precision NOT NULL,
    usuario_id integer
);


ALTER TABLE public.ventas OWNER TO nueva_farmacare_db_user;

--
-- Name: ventas_id_seq; Type: SEQUENCE; Schema: public; Owner: nueva_farmacare_db_user
--

CREATE SEQUENCE public.ventas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.ventas_id_seq OWNER TO nueva_farmacare_db_user;

--
-- Name: ventas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER SEQUENCE public.ventas_id_seq OWNED BY public.ventas.id;


--
-- Name: ajustes_inventario id; Type: DEFAULT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.ajustes_inventario ALTER COLUMN id SET DEFAULT nextval('public.ajustes_inventario_id_seq'::regclass);


--
-- Name: clientes id; Type: DEFAULT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.clientes ALTER COLUMN id SET DEFAULT nextval('public.clientes_id_seq'::regclass);


--
-- Name: compras id; Type: DEFAULT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.compras ALTER COLUMN id SET DEFAULT nextval('public.compras_id_seq'::regclass);


--
-- Name: detalle_compra id; Type: DEFAULT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.detalle_compra ALTER COLUMN id SET DEFAULT nextval('public.detalle_compra_id_seq'::regclass);


--
-- Name: dispositivos_medicos id; Type: DEFAULT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.dispositivos_medicos ALTER COLUMN id SET DEFAULT nextval('public.dispositivos_medicos_id_seq'::regclass);


--
-- Name: entradas id; Type: DEFAULT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.entradas ALTER COLUMN id SET DEFAULT nextval('public.entradas_id_seq'::regclass);


--
-- Name: inventario id; Type: DEFAULT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.inventario ALTER COLUMN id SET DEFAULT nextval('public.inventario_id_seq'::regclass);


--
-- Name: medicamentos id; Type: DEFAULT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.medicamentos ALTER COLUMN id SET DEFAULT nextval('public.medicamentos_id_seq'::regclass);


--
-- Name: no_hay id; Type: DEFAULT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.no_hay ALTER COLUMN id SET DEFAULT nextval('public.no_hay_id_seq'::regclass);


--
-- Name: productos id; Type: DEFAULT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.productos ALTER COLUMN id SET DEFAULT nextval('public.productos_id_seq'::regclass);


--
-- Name: proveedores id; Type: DEFAULT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.proveedores ALTER COLUMN id SET DEFAULT nextval('public.proveedores_id_seq'::regclass);


--
-- Name: salidas id; Type: DEFAULT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.salidas ALTER COLUMN id SET DEFAULT nextval('public.salidas_id_seq'::regclass);


--
-- Name: usuarios id; Type: DEFAULT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.usuarios ALTER COLUMN id SET DEFAULT nextval('public.usuarios_id_seq'::regclass);


--
-- Name: ventas id; Type: DEFAULT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.ventas ALTER COLUMN id SET DEFAULT nextval('public.ventas_id_seq'::regclass);


--
-- Data for Name: ajustes_inventario; Type: TABLE DATA; Schema: public; Owner: nueva_farmacare_db_user
--

COPY public.ajustes_inventario (id, producto_id, tipo_producto, cantidad_ajustada, motivo, fecha_ajuste, usuario_id) FROM stdin;
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: nueva_farmacare_db_user
--

COPY public.alembic_version (version_num) FROM stdin;
e22adf2dd6da
\.


--
-- Data for Name: clientes; Type: TABLE DATA; Schema: public; Owner: nueva_farmacare_db_user
--

COPY public.clientes (id, rfc, nombre, telefono, direccion, email, contacto, telefono_contacto, fecha_creacion, fecha_modificacion) FROM stdin;
1	QFM12112212	Quifamesa	999999999	merida yucatana	Sin dato	Luis	Sin dato	\N	\N
\.


--
-- Data for Name: compras; Type: TABLE DATA; Schema: public; Owner: nueva_farmacare_db_user
--

COPY public.compras (id, fecha_compra, proveedor_id, total, usuario_id, folio_factura) FROM stdin;
2	2025-09-02 04:40:58.268614	1	2877.45	1	B137329
4	2025-09-02 17:08:13.747723	1	2180.58	1	B137331
5	2025-09-02 17:18:19.687665	1	1765.11	1	B137332
6	2025-09-02 17:37:09.302766	1	2179.2599999999998	1	B137328
7	2025-09-02 17:48:26.302765	1	3231.72	1	B137327
8	2025-09-02 19:56:44.219675	1	2177.0099999999993	1	B137324
\.


--
-- Data for Name: detalle_compra; Type: TABLE DATA; Schema: public; Owner: nueva_farmacare_db_user
--

COPY public.detalle_compra (id, compra_id, producto_id, cantidad, precio_unitario, precio_sin_iva, importe, descuento, iva) FROM stdin;
107	7	96	3	20.37	20.37	61.11	0	0
108	7	97	3	58.57	58.57	175.71	0	0
109	7	98	3	7.6	7.6	22.799999999999997	0	0
110	7	99	3	21.12	21.12	63.36	0	0
111	7	100	3	30	30	90	0	0
112	7	101	3	34.43	34.43	103.28999999999999	0	0
113	7	102	3	70.12	70.12	210.36	0	0
114	7	103	3	45.58	45.58	136.74	0	0
115	7	104	3	165.6	165.6	496.79999999999995	0	0
116	7	105	3	80.35	80.35	241.04999999999998	0	0
117	7	106	3	22.13	22.13	66.39	0	0
118	7	107	3	30.12	30.12	90.36	0	0
119	7	108	3	38.56	38.56	115.68	0	0
120	7	109	3	28.6	28.6	85.80000000000001	0	0
121	7	110	3	114.46	114.46	343.38	0	0
122	7	111	3	43.28	43.28	129.84	0	0
123	7	112	3	30.8	30.8	92.4	0	0
124	7	1	3	14.75	12.72	51.33	0	16
125	7	113	3	12.5	12.5	37.5	0	0
126	7	114	3	127.63	127.63	382.89	0	0
127	7	115	3	32.56	32.56	97.68	0	0
128	7	116	3	24.83	24.83	74.49	0	0
129	7	117	3	5	5	15	0	0
130	7	118	3	15.92	15.92	47.76	0	0
5	4	29	3	62.48	53.86	187.44	0	16
6	4	30	3	24.62	21.22	73.86	0	16
7	4	31	3	21	18.1	63	0	16
8	4	32	3	21	18.1	63	0	16
9	4	33	3	18.6	16.03	55.800000000000004	0	16
10	4	34	3	47.06	40.57	141.18	0	16
11	4	35	3	22.45	19.35	67.35	0	16
12	4	36	3	21.16	18.24	63.480000000000004	0	16
13	4	37	3	37.1	31.98	111.30000000000001	0	16
14	4	39	3	61.5	53.02	184.5	0	16
15	4	38	3	55.5	47.84	166.5	0	16
16	4	40	3	31.83	27.44	95.49	0	16
17	4	41	3	8.25	7.11	24.75	0	16
18	4	42	3	15.87	13.68	47.61	0	16
19	4	43	3	16.37	14.11	49.11	0	16
20	4	44	3	19.1	16.47	57.300000000000004	0	16
21	4	45	3	34.68	29.9	104.03999999999999	0	16
22	4	46	3	27.06	23.33	81.17999999999999	0	16
23	4	47	3	24.83	21.41	74.49	0	16
24	4	48	3	42	36.21	126	0	16
25	4	49	3	41	35.34	123	0	16
26	4	50	3	29.6	25.52	88.80000000000001	0	16
27	4	51	3	27.77	23.94	83.31	0	16
28	4	52	3	16.03	13.82	48.09	0	16
50	6	5	3	9	7.76	27	0	16
51	6	74	3	64	55.17	192	0	16
52	6	75	3	30.75	26.51	92.25	0	16
53	6	76	3	24.88	21.45	74.64	0	16
54	6	77	3	24.75	21.34	74.25	0	16
55	6	78	3	17	14.66	51	0	16
56	6	79	3	41.22	35.53	123.66	0	16
57	6	80	3	62.88	54.21	188.64000000000001	0	16
58	6	81	3	35.12	30.28	105.35999999999999	0	16
59	6	82	3	6.25	5.39	18.75	0	16
60	6	83	3	11.37	9.8	34.11	0	16
61	6	84	3	30	25.86	90	0	16
62	6	85	3	61.62	53.12	184.85999999999999	0	16
63	6	86	3	69.82	60.19	209.45999999999998	0	16
64	6	88	3	31.03	26.75	93.09	0	16
65	6	87	3	25.6	22.07	76.80000000000001	0	16
66	6	89	3	31.66	27.29	94.98	0	16
67	6	90	3	38.5	33.19	115.5	0	16
68	6	91	3	11.6	10	34.8	0	16
69	6	92	3	39.87	34.37	119.60999999999999	0	16
70	6	93	3	12	10.34	36	0	16
71	6	94	3	21.25	18.32	63.75	0	16
72	6	95	3	26.25	22.63	78.75	0	16
\.


--
-- Data for Name: dispositivos_medicos; Type: TABLE DATA; Schema: public; Owner: nueva_farmacare_db_user
--

COPY public.dispositivos_medicos (id, codigo_barras, nombre_comercial, nombre_comun, laboratorio, presentacion, iva, precio_venta, stock, fecha_modificacion, descuento, activo) FROM stdin;
1	75011251253628	FLEBOTEK	VENOCLISIS	PISA	EQUIPO PARA VENOCLISIS	16	93.96	0	2025-09-02 08:48:30.664295	10	t
2	7506256700112	VASO DE COPRO	VASO ESTERIL	INSUTEC	P 120 ML	16	12.53	0	2025-09-02 16:07:10.580964	10	t
\.


--
-- Data for Name: entradas; Type: TABLE DATA; Schema: public; Owner: nueva_farmacare_db_user
--

COPY public.entradas (id, compra_id, producto_id, tipo_producto, cantidad, importe_unitario, importe_antes_iva, iva_porcentaje, valor_iva, importe_total) FROM stdin;
\.


--
-- Data for Name: inventario; Type: TABLE DATA; Schema: public; Owner: nueva_farmacare_db_user
--

COPY public.inventario (id, producto_id, tipo_producto, cantidad, inventario_valor, punto_reorden, cantidad_faltante, fecha_modificacion) FROM stdin;
\.


--
-- Data for Name: medicamentos; Type: TABLE DATA; Schema: public; Owner: nueva_farmacare_db_user
--

COPY public.medicamentos (id, codigo_barras, nombre_comercial, nombre_generico, laboratorio, presentacion, grupo, iva, precio_venta, stock, fecha_modificacion, descuento, activo, punto_reorden, fecha_creacion) FROM stdin;
1	785120753530	ASPIRINA	Acido Acetilsalicilico	BAYER	Tabletas 400 mg C/35	V	0	78	2	2025-09-01 05:01:54.169798	\N	\N	\N	\N
4	7501008491966	LESACLOR	Aciclovir	BAYER	Tabletas 400 mg C/35	IV	0	68	3	2025-09-01 05:01:54.513788	\N	\N	\N	\N
7	7502001160026	BUSCONET	METAMIZOL SODICO / HIOSCINA	SONS	250 MG, 10 MG C/10 TABS	Medicamento IV	0	130	0	2025-09-01 23:06:09.753876	35	t	10	2025-09-01 23:06:09.753866
6	7502227871348	CRAZTRONIN	Azitromicina	RAAM	500 MG C/3 TAB	Medicamento antibiótico	0	168.01	0	2025-09-01 23:23:35.848155	50	t	10	2025-09-01 23:02:07.145533
8	7502208894557	CEFTRIAXONA	CEFTRIAXONA	BRULUAGSA	1G IM C/1 AMP	Medicamento antibiótico	0	215.6	0	2025-09-01 23:27:27.574191	45	t	10	2025-09-01 23:27:27.574171
9	7503000422627	CEFALVER	CEFALEXINA	MAVER	250 MG / 5 ML C/90 ML SUSP	Medicamento antibiótico	0	113.4	0	2025-09-01 23:31:01.491499	30	t	10	2025-09-01 23:31:01.491477
10	7503000422863	CEFALVER	CEFALEXINA	MAVER	500 MG C/12 CAPS	Medicamento antibiótico	0	119.7	0	2025-09-01 23:32:55.338908	30	t	10	2025-09-01 23:32:55.338892
11	0785118753979	VIKROL	CLARITROMICINA	MAVI	500 MG C/10 TABS	Medicamento antibiótico	0	211.9	0	2025-09-01 23:35:15.70273	35	t	10	2025-09-01 23:35:15.702713
12	7501537161163	BRUBIOL	CIPROFLOXACINO	BRULUAGSA	500 MG C/10 TABS	Medicamento antibiótico	0	77.22	0	2025-09-01 23:39:32.377112	35	t	10	2025-09-01 23:39:32.377093
13	7502208894854	BRUCAP	CAPTOPRIL	BRULUAGSA	25 MG C/30 TABS	Medicamento IV	0	46.2	0	2025-09-01 23:45:29.326952	30	t	10	2025-09-01 23:45:29.326942
14	7501537102982	CELESBITAN	BETAMETASONA	BRULUAGSA	8 MG/2ML C/1 AMP	Medicamento IV	0	56.88	0	2025-09-01 23:50:22.762998	28	t	10	2025-09-01 23:50:22.762983
15	7501258205863	VISERTRAL	CETIRIZINA	SERRAL	10 MG  C/10 TABS	Medicamento IV	0	134.38	0	2025-09-01 23:54:24.980746	35	t	10	2025-09-01 23:54:24.980733
16	7501349027817	CIPROFLOXACINO	CIPROFLAXINA	AMSA	3MG C/ 5ML GOTS	Medicamento antibiótico	0	137.2	0	2025-09-02 00:00:10.436871	60	t	10	2025-09-02 00:00:10.436854
18	7502256040517	DANKIAL-B	BUDESONIDA	DANKEL	0.250 MG C/5 AMP P/NEB	Medicamento IV	0	267.4	0	2025-09-02 00:11:58.008398	30	t	10	2025-09-02 00:11:58.008382
19	7501349020788	CLINDAMICINA	CLINDAMICINA	AMSA	300 MG C/16 CAPS	Medicamento antibiótico	0	149.1	0	2025-09-02 00:15:41.704039	30	t	10	2025-09-02 00:15:41.704021
20	7502009741050	FASICLOR	CEFACLOR	MAVER	250 MG/5 ML C/75 ML POLVO	Medicamento antibiótico	0	285.6	0	2025-09-02 00:19:53.03158	30	t	10	2025-09-02 00:19:53.031563
21	7502211781189	BROMICOF	BROMHEXINA	LOEFFLER	160 MG C/100 ML SOL	Medicamento IV	0	98.28	0	2025-09-02 00:24:06.14507	28	t	10	2025-09-02 00:22:57.096252
22	7503002773178	IPRASUAVELIN	BROMURO DE IPRATROPIO/ SALBUTAMOL	SUANCA	0.5 MG/2.5 MG/2.5 ML C/10 AMPS	Medicamento IV	0	319	0	2025-09-02 00:33:45.790095	50	t	10	2025-09-02 00:33:45.790069
23	7502211781059	BROMICOF INF	BROMHEXINA	LOEFFLER	80 MG/100 ML SOL 	Medicamento IV	0	80.85	0	2025-09-02 00:35:21.655348	30	t	10	2025-09-02 00:35:21.655324
24	0785118752347	KROBICIN	CLARITROMICINA	MAVI	250 MG/5ML SUSP C/60 ML	Medicamento IV	0	331.5	0	2025-09-02 00:38:52.933026	35	t	10	2025-09-02 00:38:52.933004
25	7501573906346	RETIRIX	CETIRIZINA	BIOMEP	100 MG/100 ML SOL C/50 ML	Medicamento IV	0	156	0	2025-09-02 00:41:13.109104	40	t	10	2025-09-02 00:41:13.109092
26	7501258210393	AZITROMICINA	Azitromicina	SERRAL	200 MG/5 ML SUS C/15 ML	Medicamento antibiótico	0	220.8	0	2025-09-02 00:42:55.035657	40	t	10	2025-09-02 00:42:55.035638
27	0785118754235	ARTROBEN	BENCIDAMIDA	MAVI	45 MG/30 ML SOL C/30 ML	Medicamento IV	0	97.65	0	2025-09-02 00:44:34.534056	40	t	10	2025-09-02 00:44:34.534038
28	7503000422498	REDALIP	BEZAFIBRATO	MAVER	200 MG C/30 TABS	Medicamento IV	0	105	0	2025-09-02 00:46:07.850154	30	t	10	2025-09-02 00:46:07.850131
17	7503002772799	SUANTROLIN	BROMURO DE IPRATROPIO	SUANCA	25 MG /100 ML C/20 ML SOL P/NEBUL	Medicamento IV	0	280.83	2	2025-09-02 04:51:56.991247	54	t	10	2025-09-02 00:05:58.667033
132	7501349025424	TELMISARTAN	TELMISARTAN	AMSA	40 MG C/14 TABS	Medicamento IV	0	134.4	0	2025-09-03 13:48:17.770552	60	t	10	2025-09-02 15:54:35.204978
133	7501349020009	TRAMADOL	TRAMADOL	AMSA	100 MG/2 ML SOL INY C/5 AMP	Medicamento IV	0	105.7	0	2025-09-03 13:48:18.08695	30	t	10	2025-09-02 15:58:43.394434
134	7501825300946	ESPABION	TRIMEBUTINA	DEGORTS	200 MG C/40 TABS	Medicamento IV	0	330.9	0	2025-09-03 13:48:18.434364	50	t	10	2025-09-02 16:01:00.667951
135	7501825300373	ESPABION	TRIMEBUTINA	DEGORTS	2 G/100 ML SUSP C/100 ML	Medicamento IV	0	156.5	0	2025-09-03 13:48:18.752765	50	t	10	2025-09-02 16:03:00.174437
136	7501825300366	ESPABION PED	TRIMEBUTINA	DEGORTS	2 G/100 ML SUSP GOTAS C/30 ML	Medicamento IV	0	116.14	0	2025-09-03 13:48:19.074575	35	t	10	2025-09-02 16:05:08.277128
5	7501573910428	OCRIX	Glibenclamida	BIOMEP	Tabletas 5 mg. C/50	Medicamento IV	0	63	3	2025-09-02 17:37:09.909501	50	\N	\N	\N
137	0785118754259	SUPRATEX	LEVODROPROPIZINA	MAVI	600 MG/100 ML SOL C/120 ML	Medicamento IV	0	149.8	0	2025-09-03 13:48:19.395225	30	t	10	2025-09-02 16:09:06.774121
138	7502009742149	EXALVER PED	GUAIFENESINA/FENILEFRINA/DEXTROMETORFANO	MAVER	5.00 G/0.25 G/0.5 G/100 ML SOL GOTAS C/30 ML	Medicamento IV	0	65.1	0	2025-09-03 13:48:19.715494	30	t	10	2025-09-02 16:12:47.603042
139	7503001008615	VALCLAN	AMOXICILINA/AC CLAVULANICO	WANDEL	200 MG/28.5 MG/5 ML SUSP P/40 ML	Medicamento antibiótico	0	120.6	0	2025-09-03 13:48:20.06605	40	t	10	2025-09-02 16:14:28.793056
53	7501258203593	LONIXER	CLONIXINATO DE LISINA	SERRAL	125 MG C/10 TABS	Medicamento IV	0	93.61	0	2025-09-03 14:37:51.774605	30	t	10	2025-09-02 06:15:29.823738
54	7501258203586	LONIXER	CLONIXINATO DE LISINA	SERRAL	250 MG C/10 TABS	Medicamento IV	0	137.9	0	2025-09-03 14:37:52.107193	30	t	10	2025-09-02 06:16:52.72606
55	7501573906407	LOZAMIR-V	CLOTRIMAZOL	BIOMEP	2.0% CAJA C/TUBO 20 G, 3 APLICADORES	Medicamento IV	0	112.7	0	2025-09-03 14:37:52.437327	30	t	10	2025-09-02 06:19:38.362702
56	7501349027824	DEFLAZACORT	DEFLAZACORT	AMSA	6 MG C/20 TABS	Medicamento IV	0	175	0	2025-09-03 14:37:52.765262	30	t	10	2025-09-02 06:21:30.538831
57	7502009745881	BENNET	DESLORATADINA	MAVER	5 MG C/10 TABS	Medicamento IV	0	107.1	0	2025-09-03 14:37:53.086851	30	t	10	2025-09-02 06:23:27.845296
58	7501537102975	BLOTAMIN	DESLORATADINA	BRULUART	50 MG/100 ML SOL C/120 ML	Medicamento IV	0	94.5	0	2025-09-03 14:37:53.411369	30	t	10	2025-09-02 06:26:48.649978
59	7501349029668	DEXAMETASONA/NEOMICINA	DEXAMETASONA/NEOMICINA	AMSA	1 MG/3.5 MG/1 ML GOTS OFT	Medicamento antibiótico	0	77	0	2025-09-03 14:37:53.737497	30	t	10	2025-09-02 06:30:41.437698
67	7502227871416	RAAMFEN	DIFENIDOL	RAAM	25 MG C/30 TABS	Medicamento IV	0	39.54	0	2025-09-03 14:37:56.626545	30	t	10	2025-09-02 06:49:07.075523
68	7502001162549	DIPHAFEN	DIFENIDOL	SONS	40 MG/2 ML SOL INY C/2 AMP	Medicamento IV	0	116.2	0	2025-09-03 14:37:56.947592	30	t	10	2025-09-02 06:50:36.53474
74	7501349020412	HIERRO DEXTRAN	HIERRO DEXTRAN	AMSA	100 MG/2 ML C/3 AMP	Medicamento IV	0	117.6	3	2025-09-02 17:37:10.272613	30	t	10	2025-09-02 07:17:22.544954
75	7501349024045	HIOSCINA	HIOSCINA	AMSA	20 MG/1 ML C/3 AMP	Medicamento IV	0	63	3	2025-09-02 17:37:10.701747	30	t	10	2025-09-02 07:19:06.374348
76	7501349028654	HIPROMELOSA	HIPROMELOSA	AMSA	5% C/10 ML GOTAS OFT	Medicamento IV	0	87.5	3	2025-09-02 17:37:11.060856	30	t	10	2025-09-02 07:20:52.25635
77	7502208894571	AFLENO	IBUPROFENO	BRULUAGSA	100 MG/5 ML SOL C/120 ML	Medicamento IV	0	75.6	3	2025-09-02 17:37:11.420486	30	t	10	2025-09-02 07:22:26.762131
78	7502009747274	DOLVER	IBUPROFENO	MAVER	600 MG C/10 TABS	Medicamento IV	0	65.1	3	2025-09-02 17:37:11.78328	30	t	10	2025-09-02 07:24:15.436983
79	7502223112384	FIDOIN-Q	IBUPROFENO	QUIMPHARMA	40 MG/ML SUSP C/15 ML GTS	Medicamento IV	0	117.6	3	2025-09-02 17:37:12.159125	30	t	10	2025-09-02 07:26:06.651822
80	7502001162426	ARDOSONS	INDOMETACINA/BETAMETASONA/METOCARBAMOL	SONS	25 MG/0.75 MG/215 MG C/20 CAPS	Medicamento IV	0	270	3	2025-09-02 17:37:12.515148	40	t	10	2025-09-02 07:28:14.075869
81	7501349020979	KETOPROFENO	KETOPROFENO	AMSA	100 MG C/15 CAPS	Medicamento IV	0	94.5	3	2025-09-02 17:37:12.882632	30	t	10	2025-09-02 07:29:31.681595
82	7502009740244	LOROTEC	KETOROLACO	MAVER	10 MG  C/10 TABS	Medicamento IV	0	58.8	3	2025-09-02 17:37:13.247762	30	t	10	2025-09-02 07:30:51.98825
83	7501349024267	KETOROLACO	KETOROLACO	AMSA	30 MG/ML C/3 AMP	Medicamento IV	0	103.2	3	2025-09-02 17:37:13.620778	40	t	10	2025-09-02 07:32:38.084915
84	7502227874202	ORDEGAN	KETOROLACO/TRAMADOL	RAAM	10 MG/25 MG C/10 CAPS	Medicamento IV	0	199.7	3	2025-09-02 17:37:13.988363	40	t	10	2025-09-02 07:34:14.141121
85	7501349028395	LEVOCETIRIZINA	LEVOCETIRIZINA	AMSA	5 MG C/10 TABS	Medicamento IV	0	140	3	2025-09-02 17:37:14.396035	30	t	10	2025-09-02 07:39:57.935225
86	7501478316073	BOCETIX	LEVOCETIRIZINA	VITAE	0.5 MG/ML SOL C/150 ML	Medicamento IV	0	234	3	2025-09-02 17:37:14.765831	40	t	10	2025-09-02 07:41:41.695076
88	7502225092486	CINA	LEVOFLOXACINO	LANDSTEINER	750 MG C/7 TABS	Medicamento antibiótico	0	171	3	2025-09-02 17:37:15.155599	40	t	10	2025-09-02 07:45:23.211014
87	7502225092479	CINA	LEVOFLOXACINO	LANDSTEINER	500 MG C/7 TABS	Medicamento antibiótico	0	191.92	3	2025-09-02 17:37:15.518346	40	t	10	2025-09-02 07:44:12.957338
119	7503001007649	WAMINDEL PED	PARACETAMOL	WANDEL	100 MG/ML SOL C/15 ML GOTAS	Medicamento IV	0	44	0	2025-09-03 13:48:13.549041	20	t	10	2025-09-02 15:24:55.315416
120	7503027446248	DIVELGEL	PINAVERIO/DIMETICONA	PROGELA	100 MG/300 MG C/16 CAPS	Medicamento IV	0	236.25	0	2025-09-03 13:48:13.879084	25	t	10	2025-09-02 15:27:40.023252
121	7501349025967	PREGABALINA	PREGABALINA	AMSA	75 MG C/14 CAPS	Medicamento IV	0	204.69	0	2025-09-03 13:48:14.202123	30	t	10	2025-09-02 15:28:59.517775
122	7502006920038	FARMIVER 	QUINFAMIDA/ALBENDAZOL	FARMACOS CONTINENTALES	150 MG/200 MG C/2 TABS	Medicamento IV	0	86.1	0	2025-09-03 13:48:14.521919	30	t	10	2025-09-02 15:31:49.429801
113	7502216792555	OMEPRAZOL	OMEPRAZOL	ULTRA	20 MG C/14 CAPS	Medicamento IV	0	107.4	0	2025-09-02 08:49:45.582436	40	t	10	2025-09-02 08:49:45.582414
114	0780083149857	TAVIDEN-FLU	OSELTAMIVIR	COLLINS	75 MG C/10 CAPS	Medicamento IV	0	475	0	2025-09-02 08:51:22.316795	50	t	10	2025-09-02 08:51:22.316776
115	0780083144302	COLLIFRIN AD	OXIMETAZOLINA	COLLINS	0.05% SOL GOTAS NASALES	Medicamento IV	0	117.11	0	2025-09-02 08:52:48.702841	30	t	10	2025-09-02 08:52:48.702822
116	7502209810211	OXOTUSIN	OXOLAMINA	AVITUS	1.0 G/100 ML SOL 118 ML	Medicamento IV	0	86.4	0	2025-09-02 08:54:30.77308	20	t	10	2025-09-02 08:54:30.773061
117	7502208894960	PORTEM	PARACETAMOL	BRULUART	500 MG C/10 TABS	Medicamento IV	0	18.48	0	2025-09-02 08:55:28.182496	30	t	10	2025-09-02 08:55:28.182477
118	7503001007663	WAMINDEL	PARACETAMOL	WANDEL	3.2 G/100 ML SOL INF C/120 ML	Medicamento IV	0	77	0	2025-09-02 08:57:34.656895	30	t	10	2025-09-02 08:57:34.656876
96	7501349022126	METAMIZOL SODICO	METAMIZOL SODICO	AMSA	1 G/2 ML C/3 AMP	Medicamento IV	0	38.5	3	2025-09-02 17:48:26.902959	30	t	10	2025-09-02 08:07:40.909707
97	0785118754204	MAVIGLIN	METFORMINA/GLIBENCLAMIDA	MAVI	500 MG/5 MG C/60 TABS	Medicamento IV	0	171.36	3	2025-09-02 17:48:27.270557	40	t	10	2025-09-02 08:09:34.478609
98	7502208892638	DIPRASID	METOCLOPRAMIDA	BRULUAGSA	10 MG C/20 TABS	Medicamento IV	0	25.2	3	2025-09-02 17:48:27.797442	30	t	10	2025-09-02 08:14:10.449975
99	7501349024151	METOCLOPRAMIDA	METOCLOPRAMIDA	AMSA	10 MG/2 ML C/6 AMP	Medicamento IV	0	77	3	2025-09-02 17:48:28.161439	30	t	10	2025-09-02 08:15:29.476328
100	7501075713176	LAMBLIT	METRONIDAZOL	NOVAG	500 MG C/30 TABS	Medicamento IV	0	51	3	2025-09-02 17:48:28.515879	15	t	10	2025-09-02 08:17:37.533456
101	7502227875506	ONTRONON	MONTELUKAST	RAAM	5 MG C/20 TABS MASTICABLES	Medicamento IV	0	253	3	2025-09-02 17:48:28.874077	50	t	10	2025-09-02 08:19:27.090257
102	7502009744440	VALTROVER G	MONTELUKAST	MAVER	4 MG C/10 SOBRES	Medicamento IV	0	198.9	3	2025-09-02 17:48:29.235041	35	t	10	2025-09-02 08:21:22.576256
123	7502006921950	FARMIVER PED	QUINFAMIDA/ALBENDAZOL	FARMACOS CONTINENTALES	100 MG/200 MG SUSP C/10 ML	Medicamento IV	0	71.4	0	2025-09-03 13:48:14.845051	30	t	10	2025-09-02 15:35:58.723816
124	7502006921967	FARMIVER INF	QUINFAMIDA/ALBENDAZOL	FARMACOS CONTINENTALES	100 MG/400 MG SUSP C/10 ML	Medicamento IV	0	73.5	0	2025-09-03 13:48:15.169957	30	t	10	2025-09-02 15:37:46.187023
125	7502006921974	FARMIVER JR	QUINFAMIDA/ALBENDAZOL	FARMACOS CONTINENTALES	200 MG/400 MG SUSP C/20 ML	Medicamento IV	0	79.8	0	2025-09-03 13:48:15.488884	30	t	10	2025-09-02 15:39:12.349052
126	7502227874110	ACTIRAAM	SILDENAFIL	RAAM	50 MG C/4 TABS	Medicamento IV	0	123.3	0	2025-09-03 13:48:15.814148	70	t	10	2025-09-02 15:42:08.42322
127	7501125100116	SOLUCION CS	CLORURO DE SODIO 0.9%	PISA	SOL C/250 ML	Medicamento IV	0	34.44	0	2025-09-03 13:48:16.135444	5	t	10	2025-09-02 15:44:40.718048
128	7501125100246	SOLUCION HT	SOLUCION HARTMANN	PISA	SOL C/500 ML	Medicamento IV	0	70.09	0	2025-09-03 13:48:16.457111	5	t	10	2025-09-02 15:46:48.722012
129	7503000422283	BACTIVER	SULFAMETOXAZOL/TRIMETOPRIMA	MAVER	800 MG/160 MG C/14 TABS	Medicamento antibiótico	0	84	0	2025-09-03 13:48:16.782136	30	t	10	2025-09-02 15:48:32.562006
130	7501537102067	SOLTRIM	SULFAMETOXAZOL/TRIMETOPRIMA	BRULUART	400 MG/ 200 MG/5 ML SUSP C/120 ML	Medicamento IV	0	58.08	0	2025-09-03 13:48:17.105918	20	t	10	2025-09-02 15:50:27.659126
131	7502227872192	FEDPROS	TAMSULOSINA	RAAM	0.4 MG C/20 CAPS	Medicamento IV	0	234.91	0	2025-09-03 13:48:17.448759	80	t	10	2025-09-02 15:52:58.259277
29	7501349028791	ACICLOVIR	Aciclovir	AMSA	400 MG C/35 TABS	Medicamento IV	0	168	3	2025-09-02 17:08:14.376481	30	t	10	2025-09-02 04:59:15.366273
30	7502227871317	ARRAMPROL	ALOPURINOL	RAAM	300 MG C/20 TABS	Medicamento IV	0	77	3	2025-09-02 17:08:14.795189	30	t	10	2025-09-02 05:03:27.954816
31	7501537165475	OXOLBRUL AD	AMBROXOL/DETROMETORFANO	BRULUART	225 MG/225 MG/100 ML SOL C/120 ML	Medicamento IV	0	48.51	3	2025-09-02 17:08:15.161523	30	t	10	2025-09-02 05:06:36.520304
32	7502009740275	COBADEX INF	AMBROXOL/DETROMETORFANO	MAVER	150 MG/113 MG/100 ML SOL C/120 ML	Medicamento IV	0	81.9	3	2025-09-02 17:08:15.51945	30	t	10	2025-09-02 05:10:15.830493
33	7501478316066	NAVIFLEXOL	AMBROXOL/DETROMETORFANO	VITAE	400 MG/400 MG/100 ML SOL C/30 ML GTS	Medicamento IV	0	65.8	3	2025-09-02 17:08:15.881803	30	t	10	2025-09-02 05:12:39.364543
34	0785118754242	SUPRATEX DAC	AMBROXOL/LEVODROPROPIZINA	MAVI	300 MG/600 MG/100 ML SOL C/120 ML	Medicamento IV	0	137.4	3	2025-09-02 17:08:16.244139	40	t	10	2025-09-02 05:15:14.267437
35	7502009741005	LARITOL EX	LORATADINA/AMBROXOL	MAVER	5 MG/30 MG C/10 TABS	Medicamento IV	0	79.2	3	2025-09-02 17:08:16.610879	40	t	10	2025-09-02 05:19:27.815595
36	0780083146214	LOVARIN EX	LORATADINA/AMBROXOL	COLLINS	100 MG/600 MG/100 ML SOL C/120 ML	Medicamento IV	0	100.04	3	2025-09-02 17:08:17.008372	35	t	10	2025-09-02 05:21:47.871706
37	7501825301578	BRONAR	LORATADINA/AMBROXOL	DEGORTS	100 MG/600 MG/100 ML SOL C/30 ML GTS	Medicamento IV	0	114.52	3	2025-09-02 17:08:17.389189	35	t	10	2025-09-02 05:24:10.988519
39	7502003381153	CONNEXUS AD	AMBROXOL/OXELADINA	RAYERE	225 MG/200 MG/100 ML SOL C/120 ML	Medicamento IV	0	172.2	3	2025-09-02 17:08:17.756009	30	t	10	2025-09-02 05:30:02.200108
38	7502003381146	CONNEXUS INF	AMBROXOL/OXELADINA	RAYERE	115 MG/100 MG/100 ML SOL C/120 ML	Medicamento IV	0	155.4	3	2025-09-02 17:08:18.14714	30	t	10	2025-09-02 05:26:20.94461
40	7501075723830	ATROXOLAM	AMBROXOL/TEOFILINA	NOVAG	7.0 MG/1.5 MG/ML SOL C/150 ML	Medicamento IV	0	136.22	3	2025-09-02 17:08:18.517691	30	t	10	2025-09-02 05:32:06.966403
41	7501349020740	AMIKACINA	AMIKACINA	AMSA	100 MG/2 ML C/1 AMP	Medicamento antibiótico	0	31.5	3	2025-09-02 17:08:18.878677	30	t	10	2025-09-02 05:34:22.833516
42	7501349021440	AMIKACINA	AMIKACINA	AMSA	500 MG/2 ML C/1 AMP	Medicamento antibiótico	0	70.7	3	2025-09-02 17:08:19.249965	30	t	10	2025-09-02 05:37:33.179663
43	7502208892232	DIMOPEN	AMOXICILINA	BRULUAGSA	500 MG C/12 CAPS	Medicamento antibiótico	0	63	3	2025-09-02 17:08:19.613815	30	t	10	2025-09-02 05:39:20.644918
44	7501349021839	AMOXICILINA	AMOXICILINA	AMSA	500 MG/5 ML SUSP 	Medicamento antibiótico	0	70	3	2025-09-02 17:08:19.978711	30	t	10	2025-09-02 05:41:08.800797
45	7502208892195	CLAVIPEN	AMOXICILINA/AC CLAVULANICO	BRULUAGSA	500 MG/125 MG C/10 TABS	Medicamento antibiótico	0	105	3	2025-09-02 17:08:20.379971	30	t	10	2025-09-02 05:44:29.349275
46	7502208892133	CLAVIPEN	AMOXICILINA/AC CLAVULANICO	BRULUAGSA	250 MG/62.5 MG/5 ML SUSP P/60 ML	Medicamento antibiótico	0	105	3	2025-09-02 17:08:20.741379	30	t	10	2025-09-02 05:46:46.001632
47	7502208892348	CLAVIPEN	AMOXICILINA/AC CLAVULANICO	BRULUAGSA	125 MG/31.25 MG/5 ML SUSP P/60 ML	Medicamento antibiótico	0	92.4	3	2025-09-02 17:08:21.106257	30	t	10	2025-09-02 05:49:23.931563
48	7502208892645	CLAVIPEN 12H	AMOXICILINA/AC CLAVULANICO	BRULUAGSA	875 MG/125 MG C/10 TABS	Medicamento antibiótico	0	147	3	2025-09-02 17:08:21.46844	30	t	10	2025-09-02 05:51:34.576335
49	7503001009414	VALCLAN 12H	AMOXICILINA/AC CLAVULANICO	WANDEL	600 MG/42.9 MG/5 ML SUSP P/50 ML	Medicamento antibiótico	0	199.5	3	2025-09-02 17:08:21.85533	30	t	10	2025-09-02 05:54:09.411083
50	7503001007182	VALCLAN 12 H JR	AMOXICILINA/AC CLAVULANICO	WANDEL	400 MG/57 MG/5 ML SUSP P/60 ML	Medicamento antibiótico	0	151.8	3	2025-09-02 17:08:22.229735	40	t	10	2025-09-02 05:56:28.840623
51	7502208892751	BRUPEN	AMPICILINA	BRULUAGSA	500 MG C/20 CAPS	Medicamento antibiótico	0	90.3	3	2025-09-02 17:08:22.596397	30	t	10	2025-09-02 05:58:02.373619
52	7501349024526	ATORVASTATINA	ATORVASTATINA	AMSA	20 MG C/10 TABS	Medicamento IV	0	144.9	3	2025-09-02 17:08:22.959538	30	t	10	2025-09-02 06:00:04.41371
60	7502004401409	DEXNE NASAL	FENILEFRINA/DEXAMETASONA/NEOMICINA	OFFENBACH	1 MG/3.5 MG/2.5 MG/1.0 ML GOTAS NASAL	Medicamento antibiótico	0	107.25	0	2025-09-03 14:37:54.062613	35	t	10	2025-09-02 06:34:23.178879
61	7502004401508	DEXNE OTICO	DEXAMETASONA/NEOMICINA/LIDOCAINA	OFFENBACH	1.0 MG/3.5 MG/15.0 MG/1.0 ML GOTAS OTICO	Medicamento antibiótico	0	120.9	0	2025-09-03 14:37:54.393001	35	t	10	2025-09-02 06:36:26.90773
62	7501573905417	TROMEFEN INF	DEXTROMETORFANO/GUAIFENESINA	BIOMEP	100 MG/1500 MG/100 ML SOL C/120 ML	Medicamento IV	0	79.3	0	2025-09-03 14:37:54.73519	35	t	10	2025-09-02 06:39:00.262628
63	7501573905431	TROMEFEN AD	DEXTROMETORFANO/GUAIFENESINA	BIOMEP	150 MG/2000 MG/100 ML SOL C/120 ML	Medicamento IV	0	87.5	0	2025-09-03 14:37:55.192714	30	t	10	2025-09-02 06:41:15.922183
64	7501537102845	NEDICLON	DICLOFENACO	BRULUART	100 MG C/20 TABS	Medicamento IV	0	41.3	0	2025-09-03 14:37:55.561988	30	t	10	2025-09-02 06:43:58.432097
65	7501125155376	DICLOFENACO	DICLOFENACO	PISA	75 MG/3 ML SOL INY C/2 AMP.	Medicamento IV	0	48.61	0	2025-09-03 14:37:55.904954	30	t	10	2025-09-02 06:45:34.139134
66	7502208891907	BUTIMAXIL	DICLOXACILINA	BRULUAGSA	250 MG/5 ML SUSP P/60 ML	Medicamento antibiótico	0	71.4	0	2025-09-03 14:37:56.30795	30	t	10	2025-09-02 06:47:23.468952
89	7501349020771	LICOMICINA	LINCOMICINA	AMSA	300 MG/ML SOL INY C/6 AMP	Medicamento antibiótico	0	129.5	3	2025-09-02 17:37:15.883253	30	t	10	2025-09-02 07:47:47.516582
90	7502009740848	LINCOVER	LINCOMICINA	MAVER	600 MG/2ML SOL INY C/3 AMP	Medicamento antibiótico	0	109.2	3	2025-09-02 17:37:16.25491	35	t	10	2025-09-02 07:49:07.927246
91	7502009746239	ERISPAN COMPUESTO	LORATADINA/BETAMETASONA	MAVER	5.00 MG/0.25 MG C/10 TABS	Medicamento IV	0	77.7	3	2025-09-02 17:37:16.752863	30	t	10	2025-09-02 07:50:58.487341
92	7502009744129	ERISPAN COMPUESTO	LORATADINA/BETAMETASONA	MAVER	100 MG/5 MG/100 ML SOL C/60 ML	Medicamento IV	0	121.8	3	2025-09-02 17:37:17.121588	30	t	10	2025-09-02 07:52:10.380573
93	7501349028159	LOSARTAN	LOSARTAN	AMSA	50 MG C/30 COMP	Medicamento IV	0	84	3	2025-09-02 17:37:17.499872	30	t	10	2025-09-02 07:53:56.439352
94	7502240450711	PUNAB	LOSARTAN	WERMAR	100 MG C/15 TABS	Medicamento IV	0	181.06	3	2025-09-02 17:37:17.862698	50	t	10	2025-09-02 07:55:46.532483
95	7502227876848	OFELICON	MELOXICAM/METOCARBAMOL	RAAM	15 MG/215 MG C/10 CAPS	Medicamento IV	0	114.94	3	2025-09-02 17:37:18.2216	30	t	10	2025-09-02 07:57:02.62175
103	7501349024991	MONTELUKAST	MONTELUKAST	AMSA	10 MG C/20 COMP	Medicamento IV	0	264.6	3	2025-09-02 17:48:29.59753	65	t	10	2025-09-02 08:23:07.966539
104	7501125155758	VITAFUSIN	MULTIVITAMINICO	PISA	AMPULA CON LIOFILIZADO Y AMPOLLETA DE 5 ML	Medicamento IV	0	266.42	3	2025-09-02 17:48:29.957005	15	t	10	2025-09-02 08:26:05.125082
105	7506386100011	DACTRICARE	MUPIROCINA	LOEFFLER	2 % C/20 MG X G CREMA	Medicamento antibiótico	0	232.1	3	2025-09-02 17:48:30.328452	45	t	10	2025-09-02 08:28:16.176809
106	0780083144807	FAZOLIN	NAFAZOLINA	COLLINS	1 MG/ML C/15 ML SOL OFT GOTAS	Medicamento IV	0	96.98	3	2025-09-02 17:48:30.690856	35	t	10	2025-09-02 08:30:02.723332
107	7502227879610	DUET FLEXENOL NF	NAPROXENO/PARACETAMOL	RAAM	257 MG/300 MG C/16 TABS	Medicamento IV	0	89.6	3	2025-09-02 17:48:31.045912	20	t	10	2025-09-02 08:35:40.528345
108	7501537103354	BRUNADOL INF	NAPROXENO/PARACETAMOL	BRULUART	125 MG/100 MG/5 ML C/100 ML	Medicamento IV	0	100.8	3	2025-09-02 17:48:31.403719	30	t	10	2025-09-02 08:37:33.518854
109	7501825300618	NEOKAP-LF	CAOLIN/NEOMICINA/PECTINA	DEGORTS	0.71 G/20 G/1.0 G/100 ML SUSP C/90 ML	Medicamento antibiótico	0	135.67	3	2025-09-02 17:48:31.771777	30	t	10	2025-09-02 08:40:10.979454
110	7501089809490	ESKAPAR 	NIFUROXAZIDA	ARMSTRONG	200 MG C/16 CAPS	Medicamento antibiótico	0	209	3	2025-09-02 17:48:32.130672	5	t	10	2025-09-02 08:42:33.903649
111	7501825304555	BRAXIGORT	NIFUROXAZIDA	DEGORTS	4.4 G/100 ML SUSP C/90 ML	Medicamento antibiótico	0	182.01	3	2025-09-02 17:48:32.484405	30	t	10	2025-09-02 08:44:10.426647
112	7501825300823	SURONIT	NITROFURANTOINA	DEGORTS	100 MG C/12 TABS	Medicamento antibiótico	0	120.4	3	2025-09-02 17:48:32.853269	30	t	10	2025-09-02 08:46:06.135218
69	7501573900221	VEXOTIL	ENALAPRIL	BIOMEP	10 MG  C/10 TABS	Medicamento IV	0	52.5	0	2025-09-03 14:37:57.267249	30	t	10	2025-09-02 06:52:07.25513
70	0785118752477	UREZOL	FENAZOPIRIDINA	MAVI	100 MG C/20 TABS	Medicamento IV	0	124.95	0	2025-09-03 14:37:57.590541	30	t	10	2025-09-02 06:53:56.768815
71	7501349012943	FLUCONAZOL	FLUCONAZOL	AMSA	150 MG C/1 CAPS	Medicamento IV	0	56	0	2025-09-03 14:37:57.915372	30	t	10	2025-09-02 06:55:27.096207
72	7502001161351	GENKOVA	GENTAMICINA	SONS	80 MG/2 ML C/5 AMP	Medicamento antibiótico	0	162.5	0	2025-09-03 14:37:58.248526	35	t	10	2025-09-02 06:57:48.147454
73	7501349026094	GENTAMICINA	GENTAMICINA	AMSA	160 MG/2 ML C/5 AMP 	Medicamento antibiótico	0	201.4	0	2025-09-03 14:37:58.6086	35	t	10	2025-09-02 06:59:21.268482
\.


--
-- Data for Name: no_hay; Type: TABLE DATA; Schema: public; Owner: nueva_farmacare_db_user
--

COPY public.no_hay (id, nombre, tipo, descripcion, fecha_creacion, fecha_modificacion) FROM stdin;
\.


--
-- Data for Name: productos; Type: TABLE DATA; Schema: public; Owner: nueva_farmacare_db_user
--

COPY public.productos (id, nombre, descripcion, stock, precio, proveedor_id, fecha_creacion) FROM stdin;
\.


--
-- Data for Name: proveedores; Type: TABLE DATA; Schema: public; Owner: nueva_farmacare_db_user
--

COPY public.proveedores (id, nombre, rfc, direccion, telefono, email, contacto, telefono_contacto, fecha_creacion, fecha_modificacion) FROM stdin;
1	QUIMICOS Y FARMACOS DE MEXICO	QFM86101BL0	C. 37 483B MERIDA CENTRO, YUCATAN CP 97000	9999263645	VENTAS@QUIFAMESA.COM.MX	\N	\N	\N	2025-09-02 01:03:09.040301
\.


--
-- Data for Name: salidas; Type: TABLE DATA; Schema: public; Owner: nueva_farmacare_db_user
--

COPY public.salidas (id, venta_id, producto_id, cantidad, importe_unitario, importe_antes_iva, iva_porcentaje, valor_iva, importe_total, fecha, producto_tipo, cliente_id, usuario_id, eliminada) FROM stdin;
\.


--
-- Data for Name: usuarios; Type: TABLE DATA; Schema: public; Owner: nueva_farmacare_db_user
--

COPY public.usuarios (id, nombre, rol, "contraseña", fecha_creacion, fecha_modificacion, activo) FROM stdin;
1	admin	Administrador	scrypt:32768:8:1$0xxY1QZuA8C8C1r5$7b1d2b1f0016232dad162b5a249e123fce2e80940492c0b807c9b61baa30fda83d055ffdc8e42d941d6925c262982dd90eac6d2231fc9852c2163340a289a958	2025-08-29 19:03:30.770553	\N	\N
2	victoria iste	cajero	scrypt:32768:8:1$JBT7m7JdME4cSiwC$135f05701624853e0797f66f656464e14ff1543efc5903f58b8ac438c9b48a0cf0e86ba789831358515c2b897d0c2d5a8daed00dbe19af2cca6167021772b393	2025-08-30 16:12:31.783589	\N	\N
\.


--
-- Data for Name: ventas; Type: TABLE DATA; Schema: public; Owner: nueva_farmacare_db_user
--

COPY public.ventas (id, fecha, cliente_id, total, usuario_id) FROM stdin;
1	2025-08-30 20:15:03.689559	\N	0	1
2	2025-08-30 20:15:17.445249	\N	0	1
3	2025-08-30 20:39:17.530684	\N	0	1
4	2025-08-30 20:55:02.828066	1	0	1
5	2025-08-30 20:55:38.257477	\N	0	1
6	2025-08-31 23:28:22.890634	\N	0	1
7	2025-08-31 23:28:46.06995	\N	0	1
8	2025-08-31 23:30:04.405135	\N	0	1
\.


--
-- Name: ajustes_inventario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nueva_farmacare_db_user
--

SELECT pg_catalog.setval('public.ajustes_inventario_id_seq', 1, false);


--
-- Name: clientes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nueva_farmacare_db_user
--

SELECT pg_catalog.setval('public.clientes_id_seq', 1, true);


--
-- Name: compras_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nueva_farmacare_db_user
--

SELECT pg_catalog.setval('public.compras_id_seq', 8, true);


--
-- Name: detalle_compra_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nueva_farmacare_db_user
--

SELECT pg_catalog.setval('public.detalle_compra_id_seq', 193, true);


--
-- Name: dispositivos_medicos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nueva_farmacare_db_user
--

SELECT pg_catalog.setval('public.dispositivos_medicos_id_seq', 2, true);


--
-- Name: entradas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nueva_farmacare_db_user
--

SELECT pg_catalog.setval('public.entradas_id_seq', 1, false);


--
-- Name: inventario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nueva_farmacare_db_user
--

SELECT pg_catalog.setval('public.inventario_id_seq', 1, false);


--
-- Name: medicamentos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nueva_farmacare_db_user
--

SELECT pg_catalog.setval('public.medicamentos_id_seq', 139, true);


--
-- Name: no_hay_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nueva_farmacare_db_user
--

SELECT pg_catalog.setval('public.no_hay_id_seq', 1, false);


--
-- Name: productos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nueva_farmacare_db_user
--

SELECT pg_catalog.setval('public.productos_id_seq', 1, false);


--
-- Name: proveedores_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nueva_farmacare_db_user
--

SELECT pg_catalog.setval('public.proveedores_id_seq', 1, true);


--
-- Name: salidas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nueva_farmacare_db_user
--

SELECT pg_catalog.setval('public.salidas_id_seq', 1, false);


--
-- Name: usuarios_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nueva_farmacare_db_user
--

SELECT pg_catalog.setval('public.usuarios_id_seq', 2, true);


--
-- Name: ventas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nueva_farmacare_db_user
--

SELECT pg_catalog.setval('public.ventas_id_seq', 8, true);


--
-- Name: ajustes_inventario ajustes_inventario_pkey; Type: CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.ajustes_inventario
    ADD CONSTRAINT ajustes_inventario_pkey PRIMARY KEY (id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: clientes clientes_pkey; Type: CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.clientes
    ADD CONSTRAINT clientes_pkey PRIMARY KEY (id);


--
-- Name: clientes clientes_rfc_key; Type: CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.clientes
    ADD CONSTRAINT clientes_rfc_key UNIQUE (rfc);


--
-- Name: compras compras_pkey; Type: CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.compras
    ADD CONSTRAINT compras_pkey PRIMARY KEY (id);


--
-- Name: detalle_compra detalle_compra_pkey; Type: CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.detalle_compra
    ADD CONSTRAINT detalle_compra_pkey PRIMARY KEY (id);


--
-- Name: dispositivos_medicos dispositivos_medicos_codigo_barras_key; Type: CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.dispositivos_medicos
    ADD CONSTRAINT dispositivos_medicos_codigo_barras_key UNIQUE (codigo_barras);


--
-- Name: dispositivos_medicos dispositivos_medicos_pkey; Type: CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.dispositivos_medicos
    ADD CONSTRAINT dispositivos_medicos_pkey PRIMARY KEY (id);


--
-- Name: entradas entradas_pkey; Type: CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.entradas
    ADD CONSTRAINT entradas_pkey PRIMARY KEY (id);


--
-- Name: inventario inventario_pkey; Type: CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.inventario
    ADD CONSTRAINT inventario_pkey PRIMARY KEY (id);


--
-- Name: medicamentos medicamentos_codigo_barras_key; Type: CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.medicamentos
    ADD CONSTRAINT medicamentos_codigo_barras_key UNIQUE (codigo_barras);


--
-- Name: medicamentos medicamentos_pkey; Type: CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.medicamentos
    ADD CONSTRAINT medicamentos_pkey PRIMARY KEY (id);


--
-- Name: no_hay no_hay_pkey; Type: CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.no_hay
    ADD CONSTRAINT no_hay_pkey PRIMARY KEY (id);


--
-- Name: productos productos_pkey; Type: CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.productos
    ADD CONSTRAINT productos_pkey PRIMARY KEY (id);


--
-- Name: proveedores proveedores_pkey; Type: CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.proveedores
    ADD CONSTRAINT proveedores_pkey PRIMARY KEY (id);


--
-- Name: proveedores proveedores_rfc_key; Type: CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.proveedores
    ADD CONSTRAINT proveedores_rfc_key UNIQUE (rfc);


--
-- Name: salidas salidas_pkey; Type: CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.salidas
    ADD CONSTRAINT salidas_pkey PRIMARY KEY (id);


--
-- Name: usuarios usuarios_nombre_key; Type: CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_nombre_key UNIQUE (nombre);


--
-- Name: usuarios usuarios_pkey; Type: CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_pkey PRIMARY KEY (id);


--
-- Name: ventas ventas_pkey; Type: CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.ventas
    ADD CONSTRAINT ventas_pkey PRIMARY KEY (id);


--
-- Name: ajustes_inventario ajustes_inventario_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.ajustes_inventario
    ADD CONSTRAINT ajustes_inventario_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuarios(id);


--
-- Name: compras compras_proveedor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.compras
    ADD CONSTRAINT compras_proveedor_id_fkey FOREIGN KEY (proveedor_id) REFERENCES public.proveedores(id);


--
-- Name: compras compras_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.compras
    ADD CONSTRAINT compras_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuarios(id);


--
-- Name: detalle_compra detalle_compra_compra_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.detalle_compra
    ADD CONSTRAINT detalle_compra_compra_id_fkey FOREIGN KEY (compra_id) REFERENCES public.compras(id);


--
-- Name: detalle_compra detalle_compra_producto_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.detalle_compra
    ADD CONSTRAINT detalle_compra_producto_id_fkey FOREIGN KEY (producto_id) REFERENCES public.medicamentos(id);


--
-- Name: entradas entradas_compra_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.entradas
    ADD CONSTRAINT entradas_compra_id_fkey FOREIGN KEY (compra_id) REFERENCES public.compras(id);


--
-- Name: productos productos_proveedor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.productos
    ADD CONSTRAINT productos_proveedor_id_fkey FOREIGN KEY (proveedor_id) REFERENCES public.proveedores(id);


--
-- Name: salidas salidas_cliente_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.salidas
    ADD CONSTRAINT salidas_cliente_id_fkey FOREIGN KEY (cliente_id) REFERENCES public.clientes(id);


--
-- Name: salidas salidas_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.salidas
    ADD CONSTRAINT salidas_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuarios(id);


--
-- Name: salidas salidas_venta_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.salidas
    ADD CONSTRAINT salidas_venta_id_fkey FOREIGN KEY (venta_id) REFERENCES public.ventas(id);


--
-- Name: ventas ventas_cliente_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.ventas
    ADD CONSTRAINT ventas_cliente_id_fkey FOREIGN KEY (cliente_id) REFERENCES public.clientes(id);


--
-- Name: ventas ventas_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nueva_farmacare_db_user
--

ALTER TABLE ONLY public.ventas
    ADD CONSTRAINT ventas_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuarios(id);


--
-- Name: DEFAULT PRIVILEGES FOR SEQUENCES; Type: DEFAULT ACL; Schema: -; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres GRANT ALL ON SEQUENCES TO nueva_farmacare_db_user;


--
-- Name: DEFAULT PRIVILEGES FOR TYPES; Type: DEFAULT ACL; Schema: -; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres GRANT ALL ON TYPES TO nueva_farmacare_db_user;


--
-- Name: DEFAULT PRIVILEGES FOR FUNCTIONS; Type: DEFAULT ACL; Schema: -; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres GRANT ALL ON FUNCTIONS TO nueva_farmacare_db_user;


--
-- Name: DEFAULT PRIVILEGES FOR TABLES; Type: DEFAULT ACL; Schema: -; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres GRANT ALL ON TABLES TO nueva_farmacare_db_user;


--
-- PostgreSQL database dump complete
--

\unrestrict uC0eJn7b3amIgfdSEPppS8KNq8Jatpc8W7lJCROayD6DOBUU6yCYJyxTzhb2mlM

