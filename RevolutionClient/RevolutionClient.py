from RevolutionClient.request_client import RevolutionRequest
from RevolutionClient.ws.RevolutionWS import Socket

class RevolutinClient(Socket):
    def __init__(self, token):
        self.req = RevolutionRequest(token=token)
        self.token = token
        Socket.__init__(self, token=token)
        pass


    def run(self):
        response =  self.req.request("GET", f"/api/connect?token={self.token}")
        return response
    
    def run_handler(self):
        self.connect_ws()
        self.client.wait()

    def send_message(self, chatId: int, message: str):
        body = {
            "type_event": "send_message",
            "chatId": chatId,
            "message": message
        }
        self.send_ws(body)
        #self.req.request("POST", f"/api/{self.token}/chatId={chatId}&message={message}")
        pass