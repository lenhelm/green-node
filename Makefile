setup_graph:
	docker pull neo4j
	docker run -d \
		   --publish=7474:7474 --publish=7687:7687 \
		   --volume=$${HOME}/neo4j/data:/data neo4j
	echo "Neo4j running on http://localhost:7474/"
