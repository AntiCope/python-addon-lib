import mcapi
from mcapi.utils import chat
from libs.socket_interpreter import ThreadedTCPServer, RequestPythonREPL
import threading

class RemotePython(mcapi.Module):
    def __init__(self):
        self.init("remote-python", "Create python interpreter server.")
    
    def on_activate(self):
        self.server = ThreadedTCPServer(("127.0.0.1", 2000), RequestPythonREPL)
        self.server.daemon_threads = False
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()
        chat.info("Server started on port 2000.")
    
    def on_deactivate(self):
        chat.info("Closing server.")
        self.server.server_close()
        self.server.shutdown()
        self.server_thread.join()
        
        

py = RemotePython()