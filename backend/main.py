from server.app import create_app
from server.config import get_api_port


if __name__ == '__main__':
    app = create_app()
    app.run(host="127.0.0.1", port=int(get_api_port()), debug=True)