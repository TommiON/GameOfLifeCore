from Engine.LocalRunner import run_in_local_mode
from Engine.RESTEndPoints import listen_for_requests
from sys import argv

def main():
    if len(argv) > 1:
        run_in_local_mode(config_file_name = argv[1])
    else:
        listen_for_requests()

if __name__ == "__main__":
    main()

