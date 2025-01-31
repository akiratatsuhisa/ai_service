from concurrent import futures
import json
import logging
from typing import Iterator

import grpc

from ai import DeepSeekService
from protos import service_pb2, service_pb2_grpc

import os

# Load configuration from the config.json file
with open("config.json", "r") as f:
    config = json.load(f)

# Set the Hugging Face cache directory environment variable
os.environ["HF_HOME"] = config["HF_HOME"]

# Set the port number for the gRPC server from the configuration
port = config["PORT"]

# Set the model name for the AI service from the configuration
model_name = config["MODEL_NAME"]


class AIServicer(service_pb2_grpc.AIServicer):
    def chat(self, request_iterator: Iterator[service_pb2.ChatRequest], context):
        service = DeepSeekService(model_name)

        for request in request_iterator:
            messsage = service.excute(request.message)
            yield service_pb2.ChatReply(message=messsage)


def serve():
    # Create a gRPC server with a thread pool executor
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Add the AI service to the server
    service_pb2_grpc.add_AIServicer_to_server(AIServicer(), server)

    # Bind the server to an insecure port
    server.add_insecure_port("[::]:" + port)

    # Start the server to listen for incoming requests
    server.start()

    # Print a message indicating that the server has started
    print("Server started, listening on " + port)

    # Wait for the server to be explicitly terminated
    server.wait_for_termination()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Add the AI service to the server
    service_pb2_grpc.add_AIServicer_to_server(AI(), server)

    # Bind the server to an insecure port
    server.add_insecure_port("[::]:" + port)

    # Start the server to listen for incoming requests
    server.start()

    # Print a message indicating that the server has started
    print("Server started, listening on " + port)

    # Wait for the server to be explicitly terminated
    server.wait_for_termination()


if __name__ == "__main__":
    # Configure the logging module to output basic information
    logging.basicConfig()

    # Call the serve function to start the gRPC server
    serve()
