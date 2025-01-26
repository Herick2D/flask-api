CREATE TABLE public.usuarios (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    password VARCHAR(120) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);
