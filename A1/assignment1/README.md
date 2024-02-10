# Assignment 1 Q4
### Building the Docker Image
To build the Docker image, navigate to the root directory of the assignment (`assignment1`) in your terminal and run the following command:

```bash
docker build -t assignment1 .
```

To run the Docker container, execute the following command:

```bash
docker run -it -v servervol:/serverdata assignment1:latest
```
### What method was used to make a volume:
The `-v` flag with the docker run command to create a named volume named servervol
