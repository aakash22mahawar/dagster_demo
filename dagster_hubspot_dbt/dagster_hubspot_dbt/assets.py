from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets

from .project import hubspot_dbt_project


@dbt_assets(manifest=hubspot_dbt_project.manifest_path)
def hubspot_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["run"], context=context).stream()
    