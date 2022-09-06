from pydatafront.decorator import textea_export


def triple(x: int):  # this function should NOT be hosted
    return x * 3


@textea_export("/triple_plus",
               x={
                   "treat_as": "column"
               }, )  # use all default settings
def triple_plus(x: int):  # this function should be hosted at redstone.textea.io/USER_NAME/PROJECT_NAME/FUNCTION_NAME
    return triple(x) + 1