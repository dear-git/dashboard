CREATE TABLE public.bms (
    id SERIAL PRIMARY KEY,
    substation VARCHAR(255),
    substation_code VARCHAR(10),
    area VARCHAR(50),
    state_of_charge NUMERIC(5, 2),
    -- SoC (%)
    state_of_health NUMERIC(5, 2),
    -- SoH (%)
    current_per_string NUMERIC(10, 3),
    voltage_per_string NUMERIC(10, 3),
    voltage_per_cell NUMERIC(10, 3),
    temperature_per_cell NUMERIC(10, 3),
    internal_resistance_per_cell NUMERIC(10, 3),
    ambient_temperature NUMERIC(10, 3),
    recorded_at TIMESTAMP DEFAULT NOW()
);