import os
import subprocess

class Docker_Configuration:
    def __init__(self):
        self.LLM_Framework = "llama_model.py"
        self.Server_Administration = "server_administration.py"
        self.In_Network_Configuration = True

    def setup_docker(self):
        # Create Dockerfile
        with open("Dockerfile", "w") as file:
            file.write("FROM ubuntu:latest\n")
            file.write("RUN apt-get update && apt-get install -y xonsh\n")
            file.write(f"COPY ./{self.LLM_Framework} /app/\n")
            file.write(f"COPY ./{self.Server_Administration} /app/\n")
            file.write("WORKDIR /app\n")
            file.write("CMD [\"xonsh\"]\n")

        # Build Docker image
        subprocess.run(["docker", "build", "-t", "llm_framework", "."])

        # Run Docker container in-network
        if self.In_Network_Configuration:
            subprocess.run(["docker", "run", "--network=host", "llm_framework"])

if __name__ == "__main__":
    docker_config = Docker_Configuration()
    docker_config.setup_docker()