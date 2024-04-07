<br>

**Interacting with Amazon Glue**

<br>

### Introduction

This example provides the Amazon Glue service requests 

* Crawlers: create, start/launch, delete
* Crawler Databases: delete

<br>

In line with every compute service interaction with Amazon Web Services, this example depends on an Amazon Resource Name. 
Herein, the resource name pattern is:

> arn:aws:iam::{account_id}:role/{glue_service_role}

<br>

This example expects the Amazon Secrets settings

| expects           | for               |
|:------------------|:------------------|
| GlueServiceRole   | glue_service_role |
| AccountIdentifier | account_id        |


The settings should encode the true values.  The class [secret](./src/functions/secret.py) retrieves a secret value, via 
its key, from Amazon Secrets.

<br>


### Execution

Execution is via

> src/main.py parameters.yml

<br>

Wherein `parameters.yaml` encodes the expected service parameters:

<table style="width: 80%; border: 0; border-spacing: 5px; margin-left: 35px">
  <colgroup>
      <col span="1" style="width: 23.5%;">
      <col span="1" style="width: 43.5%;">
      <col span="1" style="width: 13.0%;">
  </colgroup>
  <thead><tr style="text-align: left"><th>parameter</th><th>notes</th><th>data type</th></tr></thead>
  <tr>
    <td>service</td> <td>crawler or database </td> <td>string</td></tr>
  <tr>
    <td>objective</td> <td>create or delete</td> <td>string</td></tr>
  <tr>
    <td>crawler_name</td> <td>What is the name of the crawler being created<br>or deleted?</td> <td>string</td></tr>
  <tr>
    <td>crawler_description</td> <td>Briefly describe the data being crawled.</td> <td>string</td></tr>
  <tr>
    <td>database_name</td> 
    <td>What is the name of the database wherein the crawl results should be stored?  If it does 
        not exist, it will be created.</td>
    <td>string</td></tr>
  <tr>
    <td>s3_bucket_name</td> 
    <td>The name of the S3 bucket the new crawler will target.</td>
    <td>string</td></tr>
  <tr>
    <td>table_prefix</td> 
    <td>What prefix should the tables of this crawler have? </td>
    <td>string</td></tr>
  <tr>
    <td>schedule</td> 
    <td>The crawler's schedule defined via a cron string.  Exclude if a schedule is not required.</td>
    <td>string</td></tr>
</table>

<br>

<details><summary><b>Example:</b><i>create crawler</i></summary>

```yaml
parameters:
  'service': 'crawler'
  'objective': 'create'
  'crawler_name': 'pollutants'
  'crawler_description': 'This crawler crawls the Amazon S3 pollutants data.'
  'database_name': 'particulates'
  'table_prefix': 'pol_'
  'schedule': "cron(0 1 ? * SAT#2 *)"
```

</details>

<br>

<details><summary><b>Example:</b><i>delete database</i></summary>

```yaml
parameters:
  'service': 'database'
  'objective': 'delete'
  'database_name': 'particulates'
```

</details>

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
