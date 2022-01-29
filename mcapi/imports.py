from meteordevelopment.meteorclient.systems.modules import Modules
from baritone.api import BaritoneAPI
from meteordevelopment.meteorclient.MeteorClient import mc

modules = Modules.get()

baritone_api = BaritoneAPI.getProvider().getPrimaryBaritone()

def baritone(command):
    # execute baritone commands
    baritone_api.getCommandManager().execute(command)