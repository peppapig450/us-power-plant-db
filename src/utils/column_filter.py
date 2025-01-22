from dataclasses import dataclass
from enum import StrEnum


class Operation(StrEnum):
    """Specifies whether to keep or drop columns when working with pandas DataFrames.

    This enumeration defines the possible operations that can be performed on DataFrame
    columns, allowing either selection (keeping) or removal (dropping) of specified columns.

    Attributes:
        KEEP: Retain only the specified columns in the DataFrame.
        DROP: Remove the specified columns from the DataFrame.

    Examples:
        >>> operation = Operation.KEEP
        >>> operation == "keep"
        True
        >>> operation = Operation.DROP
        >>> operation == "drop"
        True
    """

    KEEP = "keep"
    DROP = "drop"


# Type alias for column names for readability
type ColumnName = str


@dataclass(frozen=True)
class ColumnFilter:
    """Defines a filter configuration for DataFrame column operations.

    A dataclass that combines an operation (keep/drop) with a list of column names,
    providing a structured way to specify column filtering operations on DataFrames.

    Attributes:
        operation: An Operation enum specifying whether to keep or drop columns.
        columns: A list of column names (strings) to which the operation applies.
        lookup_table_mappings: A list of tuples, where each tuple contains two strings
            representing (key_column, value_column) pairs for lookup table operations.

    Examples:
        >>> filter = ColumnFilter(Operation.KEEP, ["name", "age", "salary"])
        >>> filter.operation
        <Operation.KEEP: 'keep'>
        >>> filter.columns
        ['name', 'age', 'salary']
    """

    operation: Operation
    columns: list[ColumnName]
    lookup_table_mappings: list[tuple[str, str]]  # List of (key_column, value_column)
