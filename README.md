# The Coffee Bar App 
The Python application auto-instrumented by [OpenTelemetry-Python].

## Content
* `dockerization`'s directory contains docker-compose files
* `src`'s directory contains sources of the application
    * application client called `the-coffee-lover` is responsible for making coffee orders
    * `the-coffee-bar` is accepting the orders
    * `the-coffee-machine` is preparing coffee (sometimes by lack of ingredients is not providing coffee)
    * `the-cashdesk` responsible for simple accounting and queries on the PostgreSQL DB
* `Pipfile`'s file is used for environment preparation and installation
* `setup.py`'s file describe all dependencies needed to install the application

## Prerequisities
* Installed [pipenv] 
* Running span collector - [jaeger]
* Running PostgreSQL DB (configuration script can be found in `dockerization/postgres/init.sql`)
* Installed [docker-compose] (optional)

## How to build?
* To build locally running application, go to the root directory of the application and execute the command:
    ```bash
    pipenv lock --pre
    pipenv install --system
    ```
* To build docker image run:
    ```bash
    docker build -t sumo/python-the-coffee-bar-app .
    ```
    
## Usage
For each of the application `the-coffe-lover`, `the-coffee-bar`, `the-coffee-machine` and `the-cashdesk` please execute `opentelemetry-auto-instrumentation python app_name -h`, e.g. `opentelemetry-auto-instrumentation python the-coffee-bar -h`. Configuration to the application can be provided by config file - example config file can be found in `src/config/config.yaml` or by application arguments.
```
usage: the_coffee_bar.py [-h] [-H HOST] [-P PORT] [-ch COFFEEMACHINE_HOST]
                         [-cp COFFEEMACHINE_PORT] [-mh CASHDESK_HOST]
                         [-mp CASHDESK_PORT] [-c CONFIG] [-ah AGENT_HOST]
                         [-ap AGENT_PORT] [-sn SERVICE_NAME] [-l LOG_LEVEL]

The Coffee Bar v0.0.1

optional arguments:
  -h, --help            show this help message and exit
  -H HOST, --host HOST  HTTP Server Host
  -P PORT, --port PORT  HTTP Server Port
  -ch COFFEEMACHINE_HOST, --coffeemachine-host COFFEEMACHINE_HOST
                        Coffe Machine Host
  -cp COFFEEMACHINE_PORT, --coffeemachine-port COFFEEMACHINE_PORT
                        Coffee Machine Port
  -mh CASHDESK_HOST, --cashdesk-host CASHDESK_HOST
                        Cashdesk Host
  -mp CASHDESK_PORT, --cashdesk-port CASHDESK_PORT
                        Cashdeks Port
  -c CONFIG, --config CONFIG
                        Configuration file path
  -ah AGENT_HOST, --agent-host AGENT_HOST
                        Tracing Agent Host
  -ap AGENT_PORT, --agent-port AGENT_PORT
                        Tracing Agent Port
  -sn SERVICE_NAME, --service-name SERVICE_NAME
                        Service Name
  -l LOG_LEVEL, --log-level LOG_LEVEL
                        Application log level

```


# Contact
In case of any issues please contact Mateusz 'mat' Rumian @ mrumian@sumologic.com


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [pipenv]: <https://pypi.org/project/pipenv/>
   [jaeger]: <https://www.jaegertracing.io/docs/1.18/getting-started/#all-in-one>
   [docker-compose]: <https://docs.docker.com/compose/install/>
   [OpenTelemetry-Python]: <https://opentelemetry-python.readthedocs.io/en/stable/examples/auto-instrumentation/README.html>
