#emily wang with sanity checks from franz schneider
#circuits, team transistor tunes

def compose(musicstr):
    #returns the PWL string for the current source in the LTspice simulation

    #initialize all the things
    spicestr = ''
    oldnote = ''
    oldt = 0.0
    t = 0.0
    time_unit = 0.13
    rest_time = 0.01
    notelist = musicstr.split()

    #key-value pairs are note: Iin
    notedict = {'':'',
                '--':'0',
                'G3':'7.899u',
                'C4':'10.6u',
                'C#4':'11.19u',
                'D4':'11.76u',
                'D#4':'12.65u',
                'E4':'13.53u',
                'F4':'14u',
                'F#4':'15u',
                'G4':'15.73u',
                'G#4':'17.04u',
                'A4':'18.1u',
                'A#4':'18.7u',
                'B4':'19.8u',
                'C5':'21.2u',
                'C#5':'22.14u',
                'D5':'23.74u',
                'E5':'26.7u',
                'F#5':'29.98u'}

    for note in notelist:
        # print note
        #since the sharp # symbol affects length of note strings
        if note[1] == '#':
            currentnote = note[0:3]
            sharp = True
        else:
            currentnote = note[0:2]
            sharp = False

        #to make the program robust enough to not break when a note is not in our notedict
        try:
            currentIin = notedict[currentnote]
        except:
            print currentnote
            print 'AHHHH'
            print 'not in our note dictionary yo'
            return

        #putting the appropriate length for a note
        if sharp:  
            t += len(note)*time_unit / 3
        elif not sharp: 
            t += len(note)*time_unit / 2
        else:
            print '%s <<< this note is invalid. did you make a typo??' % currentnote
            break

        #the t-.001 parts are there so PWL acts the way we want to in LTSpice
        if oldnote == '':
            oldt = 0;
        spicenote = "%0.3fs %s %0.3fs %s %0.3fs %s %0.3fs %s " % (oldt, notedict[currentnote], t-rest_time-.001, notedict[currentnote], t-rest_time, 0, t-0.001, 0)
        
        #current things become the old things at the end of an iteration
        oldt = t
        oldnote = currentnote

        #building up the result
        spicestr += spicenote

        #for debugging purposes
        # print currentnote
        # print spicenote

    #yay, output
    spicestr = 'PWL(%s)' % spicestr[:-1]
    return spicestr

if __name__ == '__main__':
    pokemonbattlenotes= "D4 D4 A4A4 D4 D4 A#4A#4 D4 D4 A4A4 D4 D4 C#4C#4 D4 D4 A4A4 D4 D4 C#5C#5 D5D5D5D5 D4D4D4D4 C5C5C5C5 C4C4C4C4"
    pokemonbattlespice = compose(pokemonbattlenotes)
    print 'PK Battle: ' + pokemonbattlespice

    pokemoncenternotes = "F4 C4 F4 C5C5 A#4A#4 A4 G4 E4E4E4E4E4E4E4 E4 C4 E4 A4A4 G4G4 E4 F4 A4 D4 E4 F4 E4 D4 C4"
    pokemoncenterspice = compose(pokemoncenternotes)
    print '\n PK Center: ' + pokemoncenterspice

    tetrisnotes = "C#5C#5 G#4 A4 B4B4 A4 G#4 F#4F#4 F#4 A4 C#5C#5 B4 A4 G#4G#4G#4 A4 B4B4 C#5C#5 A4A4 F#4F#4 F#4F#4"
    tetrisspice = compose(tetrisnotes)
    print '\n Tetris: ' + tetrisspice

    zeldanotes = "C4C4C4C4 G3G3G3G3G3G3 C4C4 C4 D4 E4 F4 G4G4G4G4G4G4G4G4G4G4 G4G4 G4 G#4 A#4A#4 C5C5C5C5C5C5C5C5C5C5 C5C5 C5C5 A#4 G#4 A#4A#4A#4 G#4 G4G4G4G4G4G4G4G4G4G4 D#4D#4#4D#4 F4F4 F4 G4 G#4G#4G#4G#4G#4G#4G#4G#4 G4G4 F4F4 D#4D#4 D#4 F4 G4G4G4G4G4G4G4G4 F4F4 D#4D#4 D4D4 D4 E4 F#4F#4F#4F#4F#4F#4F#4F#4 A4A4A4A4 G4G4G4G4 G3 G3 G3 G3 G3G3 G3G3 G3G3 G3G3"
    zeldaspice = compose(zeldanotes)
    print '\n Zelda: ' + zeldaspice

    pokemonthemenotes = "A4 A4 A4 A4A4A4 A4 G4G4 E4 C4C4C4C4 C4 A4A4 A4A4 G4 F4 G4G4 ---- ---- -- F4 A#4A#4 A#4A#4 A#4 A4A4 G4G4 F4F4F4F4 F4 A4A4 A4 G4G4 F4 A4 A4A4A4A4A4A4A4A4"
    pokemonthemespice = compose(pokemonthemenotes)
    print '\n Pokemon Theme: ' + pokemonthemespice