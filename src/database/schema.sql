CREATE TABLE IF NOT EXISTS vehicle_registrations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    registration_date DATE,
    vehicle_category VARCHAR(10),
    vehicle_class VARCHAR(100),
    manufacturer VARCHAR(100),
    state VARCHAR(50),
    rto_code VARCHAR(20),
    fuel_type VARCHAR(50),
    count INTEGER,
    financial_year VARCHAR(10),
    quarter VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS manufacturer_metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    manufacturer VARCHAR(100),
    vehicle_category VARCHAR(10),
    period_type VARCHAR(20),
    period_value VARCHAR(20),
    total_registrations INTEGER,
    market_share_percent DECIMAL(5,2),
    yoy_growth_percent DECIMAL(6,2),
    qoq_growth_percent DECIMAL(6,2)
);
