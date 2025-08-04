import pandas as pd
from sqlalchemy import create_engine, text

# Database connection config
DB_USER = "postgres"
DB_PASS = "aftha3333"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "ecommerce"

# Step 1: Connect to PostgreSQL
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Step 2: Load CSV data
users_df = pd.read_csv("users.csv", parse_dates=["created_at"])
orders_df = pd.read_csv("orders.csv", parse_dates=["created_at", "returned_at", "shipped_at", "delivered_at"])

# Step 3: Insert into DB
users_df.to_sql("users", con=engine, if_exists="append", index=False)
orders_df.to_sql("orders", con=engine, if_exists="append", index=False)
print("Data loaded into PostgreSQL.")

# Step 4: Verify counts
with engine.connect() as conn:
    user_count = conn.execute(text("SELECT COUNT(*) FROM users")).scalar()
    order_count = conn.execute(text("SELECT COUNT(*) FROM orders")).scalar()
    print(f"Users in DB: {user_count}")
    print(f"Orders in DB: {order_count}")

