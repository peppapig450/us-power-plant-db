from utils.filtering import ColumnFilter, Operation

# Column filters for our EIA860 files
EIA860_COLUMN_FILTERS = {
    "1___Utility_Y2023.xlsx": ColumnFilter(
        Operation.KEEP,
        [
            "Utility ID",
            "Utility Name",
            "Street Address",
            "City",
            "State",
            "Zip",
            "Entity Type",
        ],
    ),
    "2___Plant_Y2023.xlsx": ColumnFilter(
        Operation.DROP,
        [
            "Utility Name",
            "Plant Name"
        ],
    ),
}

EIA860_ZIP_FILE = "data/raw/eia860_data.zip"

# Filename pattern for EIA860 data
EIA860_FILENAME_PATTERN = r"\d+_.*_Y\d{4}.xlsx"