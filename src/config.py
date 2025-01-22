from utils.column_filter import ColumnFilter, Operation

# Column filters for our EIA860 files
# Drop FERC columns for now
EIA860_COLUMN_FILTERS = {
    "1___Utility_Y2023.xlsx": ColumnFilter(
        Operation.KEEP,
        [
            "Utility ID",
            "Street Address",
            "City",
            "State",
            "Zip",
            "Entity Type",
        ],
        [("Utility ID", "Utility Name")],
    ),
    "2___Plant_Y2023.xlsx": ColumnFilter(
        Operation.DROP,
        [
            "Utility Name",
            "Plant Name",
            "Balancing Authority Name",
            "Sector Name",
            "FERC Cogeneration Status",
            "FERC Cogeneration Docket Number",
            "FERC Small Power Producer Status",
            "FERC Small Power Producer Docket Number",
            "FERC Exempt Wholesale Generator Status",
            "FERC Exempt Wholesale Generator Docket Number",
            "Transmission or Distribution System Owner"
        ],
        [
            ("Plant Code", "Plant Name"),
            ("Balancing Authority Code", "Balancing Authority Name"),
            ("Sector", "Sector Name"),
            ("Transmission or Distribution System Owner ID", "Transmission or Distribution System Owner")
        ],
    ),
}

EIA860_ZIP_FILE = "data/raw/eia860_data.zip"

# Filename pattern for EIA860 data
EIA860_FILENAME_PATTERN = r"\d+_.*_Y\d{4}.xlsx"
