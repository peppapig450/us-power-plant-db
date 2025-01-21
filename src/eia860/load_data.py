import io
import re
import zipfile

import pandas as pd


def read_zip_from_file_to_dataframe(zip_filepath: str, compiled_regex: re.Pattern[str]):
    """Reads Excel files from a zip archive that match a regex pattern and converts them to DataFrames.

    This function opens a zip file, searches for files matching the provided regex pattern,
    and attempts to read each matching file as an Excel file into a pandas DataFrame.

    Args:
        zip_filepath: String path to the zip file to be processed.
        compiled_regex: Pre-compiled regex pattern object to match against filenames in the zip.

    Returns:
        Dict mapping filenames to their corresponding pandas DataFrames, or None if:
        - The zip file is not found
        - No files match the regex pattern
        - The zip file is corrupted

    Raises:
        No exceptions are raised; all errors are handled internally:
        - FileNotFoundError: Prints error message if zip file doesn't exist
        - BadZipFile: Prints error message if zip file is corrupted
        - ParserError: Prints error message and skips file if Excel parsing fails
        - ValueError: Prints error message and skips file if file is not valid Excel

    Examples:
        >>> import re
        >>> pattern = re.compile(r'\.xlsx$')
        >>> dfs = read_zip_from_file_to_dataframe('data.zip', pattern)
        >>> if dfs:
        ...     for filename, df in dfs.items():
        ...         print(f"Found DataFrame for {filename}")
    """
    try:
        with zipfile.ZipFile(zip_filepath, "r") as zip_ref:
            matching_files = [
                filename
                for filename in zip_ref.namelist()
                if compiled_regex.search(filename)
            ]

            if not matching_files:
                print("No specified files found in the zip archive.")
                return None

            dataframes: dict[str, pd.DataFrame] = {}
            for filename in matching_files:
                with zip_ref.open(filename) as file:
                    try:
                        df = pd.read_excel(
                            io.BytesIO(file.read()), header=1, names=None
                        )
                        dataframes[filename] = df
                    except pd.errors.ParserError as e:
                        print(f"Error parsing file {filename}: {e}")
                        continue
                    except ValueError as e:
                        print(
                            f"ValueError for {filename}: {e}. Check if the file is an Excel file."
                        )
                        continue
            return dataframes
    except FileNotFoundError:
        print(f"Error: Zip file not found at {zip_filepath}")
        return None
    except zipfile.BadZipFile as e:
        print(f"Bad zip file: {e}")
        return None
