def construct_insert_query(table_name, columns):
    """Construct an INSERT query based on table name and column names."""
    # Dynamically create column and placeholder strings
    columns_str = ', '.join(columns)  # Column names separated by commas
    placeholders_str = ', '.join(['%s'] * len(columns))  # Placeholder for each column
    query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders_str})"
    return query