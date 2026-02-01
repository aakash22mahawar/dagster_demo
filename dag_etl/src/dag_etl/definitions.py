from dagster import Definitions
from dag_etl.defs.data_assets import (
    create_dirty_data,
    clean_data,
    load_cleaned_data,
)

defs = Definitions(
    assets=[
        create_dirty_data,
        clean_data,
        load_cleaned_data,
    ]
)
