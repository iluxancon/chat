from apistar import App, Route, types, validators                              
import requests
#import find
#finder = find
chat_messages = []

class ChatMessage(types.Type):
    username = validators.String()
    message =  validators.String()


def add_message_to_chat(chat_message: ChatMessage):
    chat_messages.append(chat_message)
    return {"status": "OK"}


def return_chat_messages():
    return chat_messages


routes = [
    Route('/chat',method='POST', handler=add_message_to_chat),
    Route('/chat',method='GET', handler=return_chat_messages)
]



class CORSMiddleware(App):
    """Add Cross-origin resource sharing headers to every request."""

    def __init__(self, origin="*", **kwargs):
        super().__init__(**kwargs)
        self.origin = origin

    def __call__(self, environ, start_response):
        def add_cors_headers(status, headers, exc_info=None):
            headers.append(("Access-Control-Allow-Origin", self.origin))
            headers.append(
                ("Access-Control-Allow-Headers", "Origin, Content-Type, Authorization")
            )
            headers.append(("Access-Control-Allow-Credentials", "true"))
            headers.append(("Access-Control-Allow-Methods", "GET, PUT, POST, DELETE"))

            return start_response(status, headers)

        if environ.get("REQUEST_METHOD") == "OPTIONS":
            add_cors_headers("200 OK", [("Content-Type", "text/plain")])
            return [b"200 OK"]

        return super().__call__(environ, add_cors_headers)


app = CORSMiddleware(origin="*", routes=routes)


if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True)