import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class DemoServer(BaseHTTPRequestHandler):

    @staticmethod
    def add_person(self, name: str, age:int):
        personen: list = []
        with open("personen.json", "r") as fh:
            personen: list = json.load(fh)
        personen.append({"name": name, "age": age})
        with open("personen.json", "w") as fh:
            json.dump(personen, fh)

    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("Hello".encode()))

    def do_POST(self):
        self.send_response(200)
        content_length = int(self.headers.get('Content-Length', 0))

        # Read the POST data
        post_data = self.rfile.read(content_length)
        post_data = post_data.decode("utf-8")
        post_data=post_data.split("=")
        post_data=post_data.split("&")
        post_data=post_data.split("=")
        print(f"{post_data=}")
        try:
            add_person(post_data[0],int(post_data[1]))
        except Exception as ex:
            print(f"{ex=}")
        self.send_header("content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(f"{post_data=}".encode()))


# demoserver:DemoServer=DemoServer()
if __name__ == "__main__":
    server: HTTPServer = HTTPServer(("localhost", 8000), DemoServer)
    try:
        server.serve_forever()
    except KeyboardInterrupt as keyex:
        print(f"{keyex=}")


def add_person(name: str, age: int):
    with open("personen.json", "w") as fh:
        personen_dict: list = [{'name': 'Alex'}]
        json.dump(personen_dict, fh)


def get_personen() -> list:
    personen: list = []
    with open("personen.json", "r") as fh:
        personen = json.load(fh)
    return personen


"""
add_person("Alex",12)

"""
# get_personen()
