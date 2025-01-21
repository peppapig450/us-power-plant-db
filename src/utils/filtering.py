from enum import StrEnum
from typing import NamedTuple

# Enum for specifying whether to keep or drop columns when working with pandas
class Operation(StrEnum):
    """
    Enumeration representing the operation to perform on columns.

    Attributes:
        KEEP: Keep the specified columns.
        DROP: Drop the specified columns.
    """
    KEEP = "keep"
    DROP = "drop"
    
type ColumnName = str

# Named tuple to represent column filter
class ColumnFilter(NamedTuple):
    """
    Represents a filter for selecting or excluding columns in a DataFrame.

    Attributes:
        operation: The operation to perform (KEEP or DROP).
        columns: A list of column names to apply the operation to.
    """
    operation: Operation
    columns: list[ColumnName]