# GreenNode

GreenNode helps to analyze suppy chain networks for the most CO2 efficient production process.

Supply chains consist of resources, suppliers, customers, logistic companies and a varity of different transportation vessels. To identify the less CO2 consuming production process can be a daunting task considering the complexity of such networks. Graphs are the most natural representation for networks and smart minds found many algorithms that help to answer different questions


## TODOs

Roadmap:

General:
	Database: Neo4J
	Backend: Docker container
	GUI: Docker container

	- [ ] Makefile (or docker-compose) for start, stop, restart

Database:
	- [ ] Find Neo4J version that supports graph algorithms
	- [ ] Dockerfile for Neo4J
	- [ ] Env file for information about connection

Backend:
	- [ ] Dockerfile for backend
	- [ ] Testdata
	- [ ] Connection with Neo4J
	- [ ] API Upload
	- [ ] Functionality for loading data into database
	- [ ] API Graph algorithms
		- [ ] Shortest paths
		- [ ] Spanning Tree
		- [ ] ...

GUI:
	- [ ] Identify best way for visualisation
	- [ ] Dockerfile for GUI
	- [ ] Show graph
	- [ ] Run graph algorithm
	- [ ] Show result
