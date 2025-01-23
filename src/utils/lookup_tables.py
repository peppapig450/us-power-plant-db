import json
from pathlib import Path

import pandas as pd

# TODO: add google style docstrings
def create_lookup_table(
    df: pd.DataFrame,
    key_column: str,
    value_column: str,
    output_filename: str,
    mappings_path: Path,
) -> None:
    """
    Creates a lookup table and saves it to a JSON file.

    Args:
        df: The pandas DataFrame.
        key_column: The column to use as keys in the lookup table.
        value_column: The column to use as values in the lookup table.
        output_filename: The name of the JSON file to save the lookup table.
        mappings_path: The Path object where lookup tables are saved.
    """
    try:
        lookup_series = df.drop_duplicates(subset=key_column).set_index(key_column)[
            value_column
        ]
        lookup_dict = lookup_series.to_dict()

        filepath = mappings_path / output_filename
        filepath.write_text(json.dumps(lookup_dict, indent=2))
        
        print(f"Lookup table saved to: {filepath}")
    except KeyError as e:
        print(f"Error: Missing column in DataFrame: {e}")
    except Exception as e:
        print(f"Unexpected error while creating lookup table: {e}")


def load_lookup_table(
    filename: str, mappings_dir: str = "data/mappings"
) -> dict | None:
    """
    Loads a lookup table from a JSON file.

    Args:
        filename: The name of the JSON file to load.
        mappings_dir: The directory where lookup tables are stored.

    Returns:
        A dictionary representing the lookup table, or None if an error occurs.
    """
    filepath = Path(mappings_dir) / filename

    if not filepath.exists():
        print(f"Error: Lookup file {filename} not found.")
        return None

    try:
        return json.loads(filepath.read_text())
    except json.JSONDecodeError as e:
        print(f"Error decoding  JSON from {filename}: {e}")
        return None


def generate_lookup_tables(
    df: pd.DataFrame,
    lookup_table_mappings: list[tuple[str, str]] | None,
    mappings_dir: str = "data/mappings",
) -> None:
    """
    Generates lookup tables for a DataFrame based on a list of key-value column mappings.

    Args:
        df: The pandas DataFrame.
        lookup_table_mappings: A list of (key_column, value_column) tuples for lookup tables.
        mappings_dir: The directory where lookup tables should be saved.
    """
    if lookup_table_mappings is None:
        return # Early exit if no lookup table to create
    
    mappings_path = Path(mappings_dir)

    for key_column, value_column in lookup_table_mappings:
        if key_column in df.columns and value_column in df.columns:
            output_filename = f"{key_column}_to_{value_column}_lookup.json"
            create_lookup_table(
                df, key_column, value_column, output_filename, mappings_path
            )
        else:
            print(
                f"Warning: Missing columns for lookup table: {key_column}, {value_column}"
            )
