import dagster as dg


@dg.asset
def hello(context: dg.AssetExecutionContext):
    context.log.info("Hello!")


@dg.asset(deps=[hello])
def aakash(context: dg.AssetExecutionContext):
    context.log.info("Aakash!")
