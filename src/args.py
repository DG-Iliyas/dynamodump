"""Arguments specification."""

import argparse

parser = argparse.ArgumentParser(
    prog="Dump DynamoDB to CSV.",
    description="Exports DynamoDB table records to csv.",
)


parser.add_argument(
    "-p",
    "--profile",
    dest="profile",
    required=True,
    help="AWS CLI Profile Name to connect to the AWS Account.",
)

parser.add_argument(
    "-r",
    "--region",
    dest="region",
    required=True,
    help="AWS Region Name for the DynamoDB table(s).",
)

parser.add_argument(
    "-t",
    "--table-names",
    dest="tables",
    nargs="+",
    required=True,
    help="List of table to be dumped to CSV",
)

parser.add_argument(
    "-i",
    "--add-index",
    dest="index",
    default=False,
    help="Add index column to CSV file.",
)
