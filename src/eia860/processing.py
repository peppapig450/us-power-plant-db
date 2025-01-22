import pandas as pd

from utils.column_filter import ColumnFilter, Operation
from utils.lookup_tables import generate_lookup_tables


def process_dataframe_with_filters(
    df: pd.DataFrame, column_filter: ColumnFilter, mappings_dir: str = "data/mappings"
) -> pd.DataFrame:
    """
    Processes a DataFrame using the specified column filters and generates lookup tables.

    Args:
        df: The pandas DataFrame to process.
        column_filter: The ColumnFilter specifying columns to KEEP, DROP, and generate lookup tables for.
        mappings_dir: The directory where lookup tables should be saved.

    Returns:
        The filtered DataFrame.

    Raises:
        ValueError: If an invalid operation type is provided.
    """
    # Validate columns exist before processing
    missing_columns = [col for col in column_filter.columns if col not in df.columns]
    if missing_columns:
        print(f"Warning: Columns not found in DataFrame: {missing_columns}")

    # Generate lookup tables
    generate_lookup_tables(df, column_filter.lookup_table_mappings, mappings_dir)

    # Apply column filtering
    match column_filter.operation:
        case Operation.KEEP:
            print(f"Keeping columns: {column_filter.columns}")
            return df[list(set(column_filter.columns) & set(df.columns))]
        case Operation.DROP:
            print(f"Dropping columns: {column_filter.columns}")
            return df.drop(columns=column_filter.columns, errors="ignore")
        case _:
            raise ValueError(f"Invalid operation type: {column_filter.operation}")
