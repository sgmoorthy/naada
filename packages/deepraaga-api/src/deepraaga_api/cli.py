import argparse

from deepraaga_api.serve import app


def main():
    parser = argparse.ArgumentParser(description="Run the DeepRaaga API Server")
    parser.add_argument("--port", type=int, default=8000, help="Port to run the API on")
    parser.add_argument("--host", type=str, default="localhost", help="Host address")
    args = parser.parse_args()

    app.run(host=args.host, port=args.port, debug=True)

if __name__ == "__main__":
    main()
