# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from protos import service_pb2 as protos_dot_service__pb2

GRPC_GENERATED_VERSION = '1.69.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in protos/service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class AIStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.chat = channel.stream_stream(
                '/ai.AI/chat',
                request_serializer=protos_dot_service__pb2.ChatRequest.SerializeToString,
                response_deserializer=protos_dot_service__pb2.ChatReply.FromString,
                _registered_method=True)


class AIServicer(object):
    """Missing associated documentation comment in .proto file."""

    def chat(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'chat': grpc.stream_stream_rpc_method_handler(
                    servicer.chat,
                    request_deserializer=protos_dot_service__pb2.ChatRequest.FromString,
                    response_serializer=protos_dot_service__pb2.ChatReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ai.AI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ai.AI', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class AI(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def chat(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/ai.AI/chat',
            protos_dot_service__pb2.ChatRequest.SerializeToString,
            protos_dot_service__pb2.ChatReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
