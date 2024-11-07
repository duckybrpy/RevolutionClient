from socketio import Client
from RevolutionClient.utils.constants import host, port

class WebsocketHandler:
    def __init__(self):
        self.handlers = {}
        pass

    def on_message(self):
        def wrapper(func):
            self.handlers["message"] = func
            return func
        return wrapper
    
    def on_user_join(self):
        def wrapper(func):
            self.handlers["on_user_join"] = func
            return func
        return wrapper
        
    
    def send(self, data):
        event_name = data.get("type_socket")
        
        del data["type_socket"]
        del data["token"]

        handler_function = self.handlers[event_name]
        if callable(handler_function):
            handler_function(data)

    

class Socket(WebsocketHandler):
    def __init__(self, token = None):
        super().__init__()
        self.client = Client()
        self.token = token
        self.status = ""

        @self.client.on("events")
        def events(data):
            self.send(data)

        @self.client.event
        def connect():
            self.status = "ON"
            self.client.emit("client_connect", {"token": self.token})
            pass

        @self.client.event
        def disconnect():
            self.status = "OFF"
            pass

        @self.client.on("clientSid")
        def teste(data):
            sid = data["sid"]


    def send_ws(self, body: dict = {}):
        self.client.emit("ws_func", body)
        pass

    def connect_ws(self):
        url_ws = f"ws://{host}:{port}/"
        self.client.connect(url_ws)