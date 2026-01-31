from dagster import Definitions, in_process_executor
from .assets import hello, world

defs = Definitions(
    assets=[hello, world],
    executor=in_process_executor,
)
