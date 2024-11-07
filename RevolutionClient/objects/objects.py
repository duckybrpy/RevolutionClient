class Message:
    def __init__(self, data: dict = {}):
        self.json = data.get("data", {})
        self.content = self.json.get("content", None)
        self.messageId = self.json.get("messageId", None)
        self.chatId = self.json.get("chatId", None)
        self.author = self.Author(self.json.get("author", {}))
        
    class Author:
        def __init__(self, data: dict = {}):
            self.json = data

            self.nickname = self.json.get("nickname", None)
            self.userId = self.json.get("userId")
            pass

        pass