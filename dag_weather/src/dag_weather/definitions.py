# definitions.py
from pathlib import Path
import dagster as dg
from dagster import Definitions, define_asset_job
from dagster_dbt import DbtCliResource, DbtProject, dbt_assets

# ETL assets
from dag_weather.defs.weather_assets import weather_raw, weather_loaded


# ------------------------------
# DBT Project Setup
# ------------------------------
dbt_project = DbtProject(
    project_dir=r"C:\Users\aakamaha\PycharmProjects\snowflake_dbt\dagster_demo\dag_weather\dbt_weather_project",
)

profiles_dir = r"C:\Users\aakamaha\.dbt"

dbt_resource = DbtCliResource(
    project_dir=dbt_project,
    profiles_dir=profiles_dir,
    target="prod",
)



# ------------------------------
# DBT Assets (depend on ELT)
# ------------------------------
@dbt_assets(manifest=dbt_project.manifest_path,)
def weather_dbt_assets(
    context: dg.AssetExecutionContext,
    dbt: DbtCliResource,
):
    yield from dbt.cli(["run"], context=context).stream()


# ------------------------------
# Job
# ------------------------------
weather_pipeline_job = define_asset_job(
    name="weather_pipeline",
    selection="*",
)


# ------------------------------
# Definitions
# ------------------------------
defs = Definitions(
    assets=[
        weather_raw,
        weather_loaded,
        weather_dbt_assets,
    ],
    resources={"dbt": dbt_resource},
    jobs=[weather_pipeline_job],
)
