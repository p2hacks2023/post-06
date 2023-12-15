from concurrent import futures
import grpc
import sample_pb2
import sample_pb2_grpc

class Sample(sample_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        message = "Hello %s." % request.name
        return sample_pb2.HelloReply(message=message)

def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    sample_pb2_grpc.add_GreeterServicer_to_server(Sample(), server)
    server.add_insecure_port('0.0.0.0:8080')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    run_server()
