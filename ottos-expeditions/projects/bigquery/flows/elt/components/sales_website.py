import ibis
import local_code.transform as T

from ascend.resources import ref, transform, test


@transform(
    inputs=[
        ref(
            "read_sales_website",
            reshape={"time": {"column": "timestamp", "granularity": "day"}},
        )
    ],
    materialized="table",
    tests=[test("not_null", column="timestamp")],
)
def sales_website(read_sales_website: ibis.Table, context) -> ibis.Table:
    sales_website = T.clean(read_sales_website)
    return sales_website
