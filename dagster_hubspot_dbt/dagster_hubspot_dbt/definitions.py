from dagster import Definitions
from dagster_dbt import DbtCliResource
from .assets import hubspot_dbt_assets
from .project import hubspot_dbt_project
from .schedules import schedules

defs = Definitions(
    assets=[hubspot_dbt_assets],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=hubspot_dbt_project,target="prod"),
    },
)