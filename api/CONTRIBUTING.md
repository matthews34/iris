## Requirements

This project uses [Docker](https://docker.com) for development,
test and deployment.

Install Docker by following the instructions in one of the following links,
depending on your OS:
- Mac: https://docs.docker.com/docker-for-mac/install/
- Windows: https://docs.docker.com/docker-for-windows/install/
- Ubuntu: https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/
- Debian: https://docs.docker.com/engine/installation/linux/docker-ce/debian/
- Arch Linux: https://wiki.archlinux.org/index.php/Docker

To make the development easier, the project also uses [Docker Compose][3]
to orchestrate multiple containers together.

Install Docker Compose by following the instructions in
https://docs.docker.com/compose/install/.

## Setup

- To set up the api server for development, run:
  ```
  docker-compose up
  ```
  **NOTE:** These commands will **create a Docker image for the Api**,
  and **load the server**. By default, the Data Base will be available at
  `localhost:3000`.

## Running Postgresql through docker

- To run postgres on terminal (if Data Base server is already running), run:
  ```
  docker exec -it iris_db_1 psql -U iris
  ```
- To backup the data base schema into a file (change -s to -a to backup data), run:
  ```
  docker exec iris_db_1 pg_dump -s -U iris > db/<filename>
  ```
- To load a script into data base, run:
  ```
  docker exec -i iris_db_1 psql -U iris < db/<filename>
  ```
