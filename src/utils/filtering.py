from enum import StrEnum
from typing import NamedTuple


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


class ColumnFilter(NamedTuple):
    """Defines a filter configuration for DataFrame column operations.

    A NamedTuple that combines an operation (keep/drop) with a list of column names,
    providing a structured way to specify column filtering operations on DataFrames.

    Attributes:
        operation: An Operation enum specifying whether to keep or drop columns.
        columns: A list of column names (strings) to which the operation applies.

    Examples:
        >>> filter = ColumnFilter(Operation.KEEP, ["name", "age", "salary"])
        >>> filter.operation
        <Operation.KEEP: 'keep'>
        >>> filter.columns
        ['name', 'age', 'salary']
    """

    operation: Operation
    columns: list[ColumnName]
