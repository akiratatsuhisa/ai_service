generate_proto_files() {
    python -m grpc_tools.protoc -Iprotos=./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/service.proto
}

activate_venv_and_run() {
    .venv\\Scripts\\activate
    echo "Using Python interpreter at: $(which python)"
    python main.py
}

case "$1" in
generate)
    generate_proto_files
    ;;
serve)
    activate_venv_and_run
    ;;
*)
    echo "Usage: $0 {generate|serve}"
    exit 1
    ;;
esac
