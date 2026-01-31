from dagster import Definitions
from my_project.defs.hello import hello, aakash

defs = Definitions(
    assets=[hello, aakash],
)
