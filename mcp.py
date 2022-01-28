#!/usr/bin/python3

import mido
from mido import Message
from mido import MidiFile
import time

outport = mido.open_output('f_midi:f_midi 16:0')
vel=80

C    = [ Message('note_on', note=60, velocity=vel, time=0),
         Message('note_on', note=64, velocity=vel, time=0),
         Message('note_on', note=67, velocity=vel, time=0),
         Message('note_on', note=72, velocity=vel, time=0) ]

C7   = [ Message('note_on', note=60, velocity=vel, time=0),
         Message('note_on', note=64, velocity=vel, time=0),
         Message('note_on', note=67, velocity=vel, time=0),
         Message('note_on', note=70, velocity=vel, time=0) ]

Cm7  = [ Message('note_on', note=60, velocity=vel, time=0),
         Message('note_on', note=63, velocity=vel, time=0),
         Message('note_on', note=67, velocity=vel, time=0),
         Message('note_on', note=70, velocity=vel, time=0) ]

Cm3  = [ Message('note_on', note=60, velocity=vel, time=0),
         Message('note_on', note=63, velocity=vel, time=0),
         Message('note_on', note=70, velocity=vel, time=0) ]

C_del= [ Message('note_on', note=60, velocity=vel, time=1),
         Message('note_off', note=60),
         Message('note_on', note=64, velocity=vel, time=1),
         Message('note_off', note=64),
         Message('note_on', note=67, velocity=vel, time=1),
         Message('note_off', note=67),
         Message('note_on', note=72, velocity=vel, time=1),
         Message('note_off', note=72) ]

F    = [ Message('note_on', note=65, velocity=vel, time=0),
         Message('note_on', note=69, velocity=vel, time=0),
         Message('note_on', note=72, velocity=vel, time=0),
         Message('note_on', note=77, velocity=vel, time=0) ]

G    = [ Message('note_on', note=67, velocity=vel, time=0),
         Message('note_on', note=71, velocity=vel, time=0),
         Message('note_on', note=74, velocity=vel, time=0),
         Message('note_on', note=79, velocity=vel, time=0) ]



#notes = C

def playnotes(notes):
    print('notes')
    hasoff = False
    for n in notes:
        outport.send(n)
        time.sleep(n.time)
        if n.type == 'note_off':
            hasoff = True
    time.sleep(0.3)
    
    if not hasoff:
        for n in notes:
            outport.send(Message('note_off', note=n.note))
    

def twistknob():
    print('going up')
    for i in range(0,120):
        outport.send(Message('control_change', channel=0, control=9, value=i))
        time.sleep(0.01)
    
    print('going down')
    for i in range(120,0,-1):
        outport.send(Message('control_change', channel=0, control=9, value=i))
        time.sleep(0.01)

        
        
#playnotes(C)
#playnotes(C)
#playnotes(F)
#playnotes(G)
#playnotes(C)

twistknob()
print("Done.")
#while True:
#    k = keyboard.read_key()
#    if k == 'p':
#        playnotes()
#    elif k == 'q':
#        print("Exiting")
#        break
        



#mid = MidiFile('test.mid')

#for msg in mid:
#    time.sleep(msg.time)
#    if not msg.is_meta:
#        outport.send(msg)




#for i, track in enumerate(mid.tracks):
#    print('Trac {}: {}'.format(i, track.name))
#    for msg in track:
#        print(msg)



