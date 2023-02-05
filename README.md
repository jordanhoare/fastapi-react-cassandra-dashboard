
# React, FastAPI & Cassandra


[WIP] The goal of this repo was to expand on my understanding of React for building user interfaces, and learn about the intricacies of Cassandra for use in highly scalable systems of applications.  FastAPI/Python was used to serve CQL queries and routes to React, aswell as kick off a data generator (args: number of records).  This repo follows on from my [CQL study](https://github.com/jordanhoare/cql-study).

Each technology in this repo is containerised into a network, so it is reproducible even without the below mentioned package managers and runtime frameworks.  Simply clone the repo and spin up the docker repo with ```docker-compose build -d --build```.

I based the data modelling and dashboard desing on a hypothetical scenario of a Car Rental company that operates nationwide, allowing for a variety of table and query options. 

<br>

<img src="/docs/dashboard.jpg" alt="Dashboard screenshot" title="Dashboard screenshot">

<br>

## Reproduction

<details>
  <summary>Requirements</summary>

<br>

- [Git](https://git-scm.com/) for command-line interface 
- [Poetry](https://python-poetry.org/docs/) package manager for Python
- [Npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) package manager for JavaScript
- [Node](https://nodejs.org/en/download/) runtime framework for JavaScript
- [Docker](https://docs.docker.com/get-docker/) for developing, shipping, and running applications

</details>

<br>

<details>
  <summary>Reproduction on a local machine</summary>

<br>

- Clone the GitHub repository to an empty folder on your local machine:
    ```
    gh repo clone jordanhoare/fastapi-react-cassandra-dashboard
    ```
- Initialise poetry:
    ```
    cd backend
    poetry install
    ```
- Initialise npm:
    ```
    cd frontend
    npm install
    ```
- Build the docker repo:
    ```
    docker-compose build -d --build
    ```

</details>


<br>

<br>


## CQL Objectives
- [x] CAP & BASE theorem 
- [x] Query first approach to data modelling
- [x] Keyspaces & creation of tables
- [x] Timestamps & time-to-live
- [ ] Secondary indexes
- [x] Partition key(s) 
- [x] Cluster key(s) 
- [x] Cluster & node architecture with replication and hex functions
- [x] Selects & inserts
- [ ] Snitch protocol
- [ ] Gossip protocol
- [x] Concurrency functions
- [ ] Compaction

<br> 

## Dashboard Ideas
For a car rental company dashboard, you can consider the following elements:
Real-time vehicle availability: A visual representation of the number of vehicles available for rent at any given time.

- [ ] Bookings: A chart or graph that displays the number of bookings made over a specified time period.
- [ ] Revenue: A chart or graph that displays the company's revenue over a specified time period.
- [ ] Customer data: A representation of customer data, such as demographics and location, to help the company better understand their customer base.
- [ ] Fleet management: Information on the maintenance, fuel consumption, and overall performance of the vehicles in the company's fleet.
- [ ] Location data: A map showing the locations of the company's vehicles, their availability, and the number of bookings made at each location.
- [ ] Alerts and notifications: Real-time notifications for events such as low fuel levels, upcoming maintenance, and overdue bookings.
