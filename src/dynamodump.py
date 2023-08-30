"""Dumps DynamoDB to a comma separated value (CSV) file."""

import boto3
import pandas as pd
from boto3.dynamodb.types import TypeDeserializer

import log
from args import parser

logger = log.setup_logger()


def from_dynamodb_to_json(item: dict[str, any]) -> dict[str, any]:
    """Convert DynamoDB JSON to python native types."""
    ddb_json_desrializer = TypeDeserializer()

    return {k: ddb_json_desrializer.deserialize(value=v) for k, v in item.items()}


def get_records(table_name: str) -> list[dict[str, any]]:
    """Scan provided table and returns deserialized data."""
    logger.info("Retrieving records from %s table.", table_name)

    records = scan_paginator.paginate(TableName=table_name).build_full_result()["Items"]

    logger.debug("%s table has %s records.", table_name, len(records))
    logger.debug("Deserializing items retrieved from %s table.", table_name)

    deserialized_items: list[dict[str, any]] = []
    for record in records:
        deserialized_items.append(from_dynamodb_to_json(record))

    logger.info("Deserialized items retrieved from %s table successfully.", table_name)
    return deserialized_items


def dump(items: list[dict[str, any]], table_name: str):
    """Dump deserilized records to a CSV file."""
    file_name: str = table_name + ".csv"
    items_df = pd.DataFrame(items)

    logger.debug("Converted deserilized items to a Pandas DataFrame.")

    items_df.to_csv(file_name, index=cli_args.index)
    logger.info("Dumped %s successfully to %s file.", table_name, file_name)


if __name__ == "__main__":
    cli_args = parser.parse_args()

    logger.debug("Establishing session for '%s' CLI profile.", cli_args.profile)
    session = boto3.session.Session(profile_name=cli_args.profile)

    dynamodb_client = session.client("dynamodb", region_name=cli_args.region)
    scan_paginator = dynamodb_client.get_paginator("scan")

    for table in cli_args.tables:
        logger.info("Operating on %s table.", table)

        items = get_records(table_name=table)
        dump(items, table)

    logger.info("Dumped %s table(s) to CSV successfully.", cli_args.tables)
