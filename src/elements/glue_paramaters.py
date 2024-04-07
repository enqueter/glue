"""
This is data type S3Parameters
"""
import typing


class GlueParameters(typing.NamedTuple):
    """
    The data type class ⇾ GlueParameters

    Attributes
    ----------

    service
      * crawler or database

    objective
      * create or delete

    crawler_name
      * What is the name of the crawler being created or deleted?

    crawler_description
      * Briefly describe the data being crawled.

    s3_bucket_name
      * The name of the S3 bucket the new crawler will target.

    database_name
      * What is the name of the database<br>wherein the crawl results should be<br> stored?  If
        it does not exist, it will be<br>created.

    table_prefix
      * What prefix should the tables of<br>this crawler have?

    schedule
      * The crawler's schedule defined via<br>a cron string.  Exclude if a schedule<br>is
        not required.

    """

    service: str
    objective: str
    crawler_name: str = None
    crawler_description: str = None
    s3_bucket_name: str = None
    database_name: str = None
    table_prefix: str = None
    schedule: str = None
