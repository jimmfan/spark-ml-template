from impala.dbapi import connect

def construct_insert_query(table_name, columns):
    """Construct an INSERT query based on table name and column names."""
    # Dynamically create column and placeholder strings
    columns_str = ', '.join(columns)  # Column names separated by commas
    placeholders_str = ', '.join(['%s'] * len(columns))  # Placeholder for each column
    query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders_str})"
    return query


def get_kudu_table_schema(impala_host, impala_port, kudu_table_name):
    # Connect to Impala
    conn = connect(host=impala_host, port=impala_port)
    cursor = conn.cursor()

    # Execute DESCRIBE statement
    cursor.execute(f'DESCRIBE {kudu_table_name}')

    # Fetch and print column names and data types
    columns = cursor.fetchall()

    table_schema = {
         col[0]: col[1] for col in columns
    }
    conn.close()

    return table_schema

