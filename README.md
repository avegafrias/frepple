[![Continous integration](https://github.com/frePPLe/frepple/actions/workflows/ubuntu24.yml/badge.svg)](https://github.com/frePPLe/frepple/actions/workflows/ubuntu24.yml)

# frePPLe fork for Partes Industriales Laguna

## Building the image

From the top of the repo:
```
docker build -f frepple.dockerfile -t frepple:9.16.0 .
```

## Starting the database and frePPLe containers

```
docker run --name=db -d --rm -e POSTGRES_USER=frepple -e POSTGRES_PASSWORD=frepple \
       -e POSTGRES_DB=frepple -e PGHOST=127.0.0.1 -e PGPORT=5432 --network=host    \
       -v $PWD/data:/var/lib/postgresql/data postgres:16 postgres -c log_statement=all

docker run --name=frepple -d --rm -e POSTGRES_USER=frepple -e POSTGRES_HOST=localhost \
       -e POSTGRES_PORT=5432 --network=host frepple:9.16.0
```

---

# frePPLe original README

## Open source supply chain planning

FrePPLe is an easy-to-use and easy-to-implement open source **demand forecasting** and
**advanced planning and scheduling** tool for manufacturing companies.

When spreadsheets doesn't suffice any longer to adequately plan and schedule your production, frePPLe allows an easy and cost-efficient way to generate a more optimized plan.

FrePPLe implements time series forecasting algorithms to analyze the sales history and compute the forecasted sales for the future.

FrePPLe implements production planning and scheduling algorithms based on best practices such as **theory of constraints** (ie *plan around the bottleneck*), **pull-based planning** (ie *start production as late as possible and directly triggered by demand*) and **lean manufacturing** (ie *avoid intermediate delays and inventory*).

## Download

The software can be downloaded in the following formats:

* Ubuntu 24 .deb package on https://github.com/frePPLe/frepple/releases/
* Docker container on https://github.com/orgs/frePPLe/packages/container/package/frepple-community
* Source tarball or zip file from https://github.com/frePPLe/frepple/releases/
* Documentation zip file from https://github.com/frePPLe/frepple/releases/

## Documentation

Visit [https://frepple.com](https://frepple.com) for documentation, screencasts and build instructions.

## License

The *Community Edition* is released under the [MIT licence](https://opensource.org/license/mit/).

The *Enterprise Edition* can be purchased from frePPLe bv. It provides additional functionality
and professional support.

The *Cloud Edition* provides provides the same capabilities as the Enterprise Edition, but is
hosted as a service in the cloud: fully supported and maintained by frePPLe bv.
