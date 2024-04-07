<br>

**Glue Services Package: In Progress**

<br>

* [Purpose](#purpose)
* [Upcoming](#upcoming)
* [Usage Notes](#usage-notes)
* [Remote Development Environment](#remote-development-environment)
* [Amazon Cloud Settings](#amazon-cloud-settings)

<br>

## Purpose

For programmatically launching Amazon Glue services.  At present

* Crawlers: create, start/launch, delete
* Crawler Databases: delete

<br>


## Upcoming

* A production mode Dockerfile
* The GitHub Actions script, i.e., the continuous integration, delivery, and deployment script, which automatically conducts
  * Code analysis.
  * Amazon Container Registry image registration. 
* GitHub Actions status badges.
* Edits of the succeeding sections.

<br>

## Usage Notes

Amazon Glue service requests are made via the main program

> src/main.py

<br>

At present, this program expects a `parameters.yaml` file within the project's root directory.  Within `parameters.yaml` users define parameter values in relation to a service of interest.  The parameters are 

<br>

| Parameter           | Notes                                                                                                                             | Data Type |
|:--------------------|:----------------------------------------------------------------------------------------------------------------------------------|:----------|
| service             | crawler or database                                                                                                               | string    |
| objective           | create or delete                                                                                                                  | string    |
| crawler_name        | What is the name of<br>the crawler being created<br>or deleted?                                                                   | string    |
| crawler_description | Briefly describe the data<br>being crawled.                                                                                       | string    |
| database_name       | What is the name of the database<br>wherein the crawl results should be<br> stored?  If it does not exist, it will be<br>created. | string    |
| table_prefix        | What prefix should the tables of<br>this crawler have?                                                                            | string    |
| schedule            | The crawler's schedule defined via<br>a cron string.  Exclude if a schedule<br>is not required.                                   | string    |

<br>

**A create crawler example**

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

**A delete database example**

```yaml
parameters:
  'service': 'database'
  'objective': 'delete'
  'database_name': 'particulates'
```

<br>

## Remote Development Environment

For remote, i.e., container, development the python environment's image is built via

```shell
docker build . --file .devcontainer/Dockerfile --tag glue
```

which names the new image `glue`.  Subsequently, use a container/instance of the image `glue` as a development environment via the command


> docker run [--rm](https://docs.docker.com/engine/reference/commandline/run/#:~:text=a%20container%20exits-,%2D%2Drm,-Automatically%20remove%20the) [-i](https://docs.docker.com/engine/reference/commandline/run/#:~:text=and%20reaps%20processes-,%2D%2Dinteractive,-%2C%20%2Di) [-t](https://docs.docker.com/get-started/02_our_app/#:~:text=Finally%2C%20the-,%2Dt,-flag%20tags%20your) [-p](https://docs.docker.com/engine/reference/commandline/run/#:~:text=%2D%2Dpublish%20%2C-,%2Dp,-Publish%20a%20container%E2%80%99s) 127.0.0.1:10000:8888 -w /app --mount \
> &nbsp; &nbsp; type=bind,src="$(pwd)",target=/app glue

wherein   `-p 10000:8888` maps the host port `1000` to container port `8888`.  Note, the container's working environment, i.e., -w, must be inline with this project's top directory.  Get the name of the running instance ``glue`` via

```shell
docker ps --all
```

<br>

## Amazon Cloud Settings

For the Glue Amazon Resource Name

> arn:aws:iam::{account_id}:role/{glue_service_role}

developers must set the Secrets:

| key<br>Secret name | value |
| :--- | :--- |
| GlueServiceRole | glue_service_role |
| AccountIdentifier | account_id |

The class [secret](./src/functions/secret.py) retrieves a secret value, via its key, from Amazon Secrets.

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
