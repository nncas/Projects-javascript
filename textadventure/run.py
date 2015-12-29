from player import Player
import world, re, time

timer = 0
player = Player("Mal")
exchange = False
commands = {r'\bALIVE\b': 'isAlive', r'\bINVENTORY\b': 'printInventory', r'\bN\b':'moveNorth', r'\bNORTH\b':'moveNorth', r'\bS\b':'moveSouth', r'\bSOUTH\b':'moveSouth', r'\bE\b':'moveEast', r'\bEAST\b':'moveEast', r'\bW\b':'moveWest', r'\bWEST\b':'moveWest',
 r'\bATTACK\b' : 'attack', r'\bINSULT\b':'insult', r'\bWHERE\b':'whereAmI', r'\bINVESTIGATE\b':'investigate', r'\bUSE\b':'use' }
def run():
    world.load_map()
    global exchange
    global player
    while not player.end:
        #print "Action:\n"
        getInput(True)
        player.checkIfEnded()
                #print res
        if timer > 2 and not exchange:
            print """There is someone calling"""
            player.locationX = 0
            player.locationY = 0
            print """Better check it out, I'm in the pilot cabin... Hello?"""
            time.sleep(2)
            print """CAPTAIN - Firefly Serenity... This is the private salvage
S.S. Walden. Receiving your distress beacon, do you
read?"""
            time.sleep(2)
            getInput(False)
            time.sleep(2)
            print """CAPTAIN - Right. Your mechanical trouble. Compression
coil, you say?"""
            time.sleep(2)
            getInput(False)
            time.sleep(2)
            print """CAPTAIN - Not even the coil? Catalyzer's a nothing
part, Captain."""
            time.sleep(2)
            getInput(False)
            time.sleep(2)
            print """CAPTAIN - It is possible we might have something that'd
do you. We just come from a big salvage job off
Ita Moon. Picked the bones'a half a dozen junk heaps
not unlike the one you're sittin' in.I suppose we could dock, take a look around, see
if there ain't some way we might come to terms.
That's if we have the part --"""
            time.sleep(2)
            getInput(False)
            time.sleep(2)
            print """CAPTAIN - Trouble is... how can I know for certain your
story's true? Ambush could be waiting for me and
my people on the other side."""
            time.sleep(2)
            getInput(False)
            time.sleep(2)
            print """CAPTAIN - (smiles)
I feel like maybe we can do business."""
            time.sleep(2)
            print """(Better go to the cargo bay to receive our guests...)"""
            exchange = True



def getInput(ext):
    global timer
    global player
    userActionRaw = raw_input(":  ")
    userAction = userActionRaw.split(" ")
    params= []
    if len(userAction)>1:
        params = userAction[1:]
    #if re.match("t", userAction):
    for key in commands:
        if re.match(key, userAction[0].upper()) and ext:
            timer +=1
            #print "pasa"
            res = getattr(player, commands[key])(*params)
run()
