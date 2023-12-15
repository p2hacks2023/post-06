import grpc
import sample_pb2
import sample_pb2_grpc

def run_client():
    # with grpc.insecure_channel('localhost:8080') as ch:
    with grpc.insecure_channel('192.168.11.15:8080') as ch:
        stub = sample_pb2_grpc.GreeterStub(ch)
        reply = stub.SayHello(sample_pb2.HelloRequest(name='atoringo'))
    print("Reply: %s" % reply.message)

if __name__ == '__main__':
    run_client()
