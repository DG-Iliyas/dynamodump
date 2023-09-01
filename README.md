![dynamodump-logo](dynamodump.png)
---
## Introduction
__*dynamodump*__ dumps AWS DynamoDB table contents to a comma separated value file.

---
## Prerequisites
  * AWS CLI
  * Python < 3.9
  * Pip (Python Package Installer)

---
## Installation
  * Clone the repo
  * Navigate to `src/` directory
  * `pipenv shell`
  * `pipenv install`

---

## Usage
  * `python dynamodump --help`
    * -h, --help:  show this help message and exit
    * -p, --profile: AWS CLI Profile Name to connect to the AWS Account.
    * -r,  --region: AWS Region Name for the DynamoDB table(s).
    * -t, --table-names: List of table to be dumped to CSV.
    * -i, --add-index: Add index column to CSV file.
      * By default, set to `False`.
