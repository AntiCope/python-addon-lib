import mcapi
from mcapi.utils import chat
from meteordevelopment.meteorclient.events.entity.player import BreakBlockEvent

def on_break(event):
    print(event)
    chat.info("On Break")
    
mcapi.event_listener(on_break, BreakBlockEvent)
