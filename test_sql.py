def create_batch_in_db(connection_pool, type):
  value = BATCH_VALUE if type == "batch" else SALESFORCE_VALUE
  query = f"INSERT INTO {SCHEMA}.{BATCH_TABLE} (lable, misc_dick) VALUES ('{value}', 1)"
