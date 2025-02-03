import subprocess, os, sys, pymediainfo

# Build ffmpeg and ffprobe from source
# or download at https://www.gyan.dev/ffmpeg/builds/
# (MT builds, Windows-only)
# or download at https://ffmpeg.org//download.html
# (MT builds, cross-platform)
# or download at https://github.com/btbn/ffmpeg-builds/releases
# (MD builds, cross-platform)
# or download at https://mega.nz/file/TAlnSJhC#u58yn-9baEduAXW2dDXLz8YAc_72DC8E0u9J1Wmr6WI
# (MT builds, Windows-only)
# Only 'bin' folder content needed

# All tools are suggested to be placed to script folder

targetFolder = 'C:\\Users\\admin\\Downloads\\nfsmw\\bonus\\flac'
outputFolder = 'C:\\Users\\admin\\Downloads\\nfsmw\\bonus\\mp3'
targetBitrate = '320k'
ffmpegfname = 'ffmpeg.exe'
ffprobefname = 'ffprobe.exe'

birateList = [ '64k',
               '128k',
               '192k',
               '256k',
               '320k' ]

# A python class definition for printing formatted text on terminal.
# Initialize TextFormatter object like this:
# >>> cprint = TextFormatter()
#
# Configure formatting style using .cfg method:
# >>> cprint.cfg('r', 'y', 'i')
# Argument 1: foreground(text) color
# Argument 2: background color
# Argument 3: text style
#
# Print formatted text using .out method:
# >>> cprint.out("Hello, world!")
#
# Reset to default settings using .reset method:
# >>> cprint.reset()

class TextFormatter:
    COLORCODE = {
        'k': 0,  # black
        'r': 1,  # red
        'g': 2,  # green
        'y': 3,  # yellow
        'b': 4,  # blue
        'm': 5,  # magenta
        'c': 6,  # cyan
        'w': 7   # white
    }
    FORMATCODE = {
        'b': 1,  # bold
        'f': 2,  # faint
        'i': 3,  # italic
        'u': 4,  # underline
        'x': 5,  # blinking
        'y': 6,  # fast blinking
        'r': 7,  # reverse
        'h': 8,  # hide
        's': 9,  # strikethrough
    }


    # constructor
    def __init__(self):
        self.reset()


    # function to reset properties
    def reset(self):
        # properties as dictionary
        self.prop = {'st': None, 'fg': None, 'bg': None}
        return self


    # function to configure properties
    def cfg(self, fg, bg=None, st=None):
        # reset and set all properties
        return self.reset().st(st).fg(fg).bg(bg)


    # set text style
    def st(self, st):
        if st in self.FORMATCODE.keys():
            self.prop['st'] = self.FORMATCODE[st]
        return self


    # set foreground color
    def fg(self, fg):
        if fg in self.COLORCODE.keys():
            self.prop['fg'] = 30 + self.COLORCODE[fg]
        return self


    # set background color
    def bg(self, bg):
        if bg in self.COLORCODE.keys():
            self.prop['bg'] = 40 + self.COLORCODE[bg]
        return self


    # formatting function
    def format(self, string):
        w = [self.prop['st'], self.prop['fg'], self.prop['bg']]
        w = [str(x) for x in w if x is not None]
        # return formatted string
        return '\x1b[%sm%s\x1b[0m' % (';'.join(w), string) if w else string


    # output formatted string
    def out(self, string):
        print(self.format(string))


def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))


def isAudio(filepath: str):
    if not os.path.exists(filepath):
        return False
    fileInfo = pymediainfo.MediaInfo.parse(filepath)
    for track in fileInfo.tracks:
        if 'Audio' == track.track_type:
            return True
    return  False


def checkBitrate(bitrate: str):
    if len(bitrate) == 0:
        return  None
    if bitrate.isdigit():
        if bitrate in birateList:
            return True
        else:
            return False
    else:
        brlower = bitrate.lower()
        brdigit = brlower
        if brdigit[-1] == 'k':
            brdigit = brdigit[:-1]
            if brdigit.isdigit():
                if (brdigit + 'k') in birateList:
                    return True
                else:
                    return False
            else:
                return None
        else:
            if brdigit.isdigit():
                if (brdigit + 'k') in birateList:
                    return True
                else:
                    return False
            else:
                return None


def listFilesInFolderByExt(folderpath: str, fileext: str = '.flac',
                           fullfilenames: bool = True):
    colorprint = TextFormatter()
    colorprint.cfg('y', 'k', 'b')
    if folderpath == '':
        colorprint.out('PATH TO FOLDER IS EMPTY')
        return None
    if not os.path.exists(folderpath):
        colorprint.out('PATH TO FOLDER DOES NOT EXIST')
        return None
    filenames = []
    for root, dirs, files in os.walk(folderpath):
        for filename in files:
            if os.path.splitext(filename)[1] == fileext:
                if fullfilenames:
                    filenames.append(os.path.join(root, filename))
                else:
                    filenames.append(filename)
    return filenames


######### SCRIPT #########
if __name__ == "__main__":
    colorprint = TextFormatter()
    colorprint.cfg('r', 'k', 'b')
    if len(targetFolder) == 0 or targetFolder is None:
        if len(sys.argv) > 1:
            if os.path.exists(sys.argv[1]):
                targetFolder = sys.argv[1]
            else:
                colorprint.out('SPECIFIED TARGET FOLDER PATH DOES NOT EXIST')
                systemExitCode = 1
                sys.exit(systemExitCode)
        else:
            colorprint.out('STRING SPECIFYING TARGET FOLDER PATH NOT PROVIDED')
            systemExitCode = 2
            sys.exit(systemExitCode)
    else:
        if not os.path.exists(targetFolder):
            if len(sys.argv) > 1:
                if os.path.exists(sys.argv[1]):
                    targetFolder = sys.argv[1]
                else:
                    colorprint.out('SPECIFIED TARGET FOLDER OATH DOES NOT EXIST')
                    systemExitCode = 1
                    sys.exit(systemExitCode)
            else:
                colorprint.out('STRING SPECIFYING TARGET FOLDER PATH NOT PROVIDED')
                systemExitCode = 2
                sys.exit(systemExitCode)
    if len(outputFolder) == 0 or outputFolder is None:
        if len(sys.argv) > 1:
            if os.path.exists(sys.argv[2]):
                outputFolder = sys.argv[2]
            else:
                colorprint.out('SPECIFIED OUTPUT FOLDER PATH DOES NOT EXIST')
                systemExitCode = 3
                sys.exit(systemExitCode)
        else:
            colorprint.out('STRING SPECIFYING OUTPUT FOLDER PATH NOT PROVIDED')
            systemExitCode = 4
            sys.exit(systemExitCode)
    else:
        if not os.path.exists(outputFolder):
            if len(sys.argv) > 2:
                if os.path.exists(sys.argv[2]):
                    outputFolder = sys.argv[2]
                else:
                    colorprint.out('SPECIFIED OUTPUT FOLDER PATH DOES NOT EXIST')
                    systemExitCode = 3
                    sys.exit(systemExitCode)
            else:
                colorprint.out('STRING SPECIFYING OUTPUT FOLDER NOT PROVIDED')
                systemExitCode = 4
                sys.exit(systemExitCode)
    if len(targetBitrate) == 0 or targetBitrate is None:
        if len(sys.argv) > 3:
            targetBitrate = sys.argv[3]
        else:
            colorprint.out('TARGET BITRATE NOT SPECIFIED')
            systemExitCode = 5
            sys.exit(systemExitCode)
    else:
        if targetBitrate.endswith('k'):
            try:
                ttrbr = int(targetBitrate[:-1])
            except ValueError:
                colorprint.out('INCORRECT BITRATE SPECIFIED')
                systemExitCode = 6
                sys.exit(systemExitCode)
        else:
            try:
                ttrbr = int(targetBitrate)
            except ValueError:
                colorprint.out('INCORRECT BITRATE SPECIFIED')
                systemExitCode = 6
                sys.exit(systemExitCode)
    brlow = targetBitrate.lower()
    brtesttres = checkBitrate(brlow)
    if brtesttres is None:
        colorprint.out('INCORRECT STRING SPECIFYING BITRATE')
        systemExitCode = 7
        sys.exit(systemExitCode)
    else:
        if not brtesttres:
            colorprint.out('INCORRECT BITRATE VALUE. ALLOWED VALUES: ' +
                           ', '.join(birateList))
            systemExitCode = 8
            sys.exit(systemExitCode)
    scriptdir = get_script_path()
    ffmpegfname = scriptdir + os.path.sep + ffmpegfname
    ffprobefname = scriptdir + os.path.sep + ffprobefname
    if not os.path.exists(ffmpegfname):
        colorprint.out('FFMPEG BINARY FILE NOT FOUND')
        systemExitCode = 9
        sys.exit(systemExitCode)
    filleList = listFilesInFolderByExt(targetFolder)
    if len(filleList) == 0 or filleList is None:
        colorprint.out('COULD NOT GET TARGET FILE LIST')
        systemExitCode = 10
        sys.exit(systemExitCode)
    convcount = 0
    outfname = ''
    for file in filleList:
        outfname = outputFolder + os.path.sep + \
                    '.'.join((file.split(os.path.sep))[-1].split('.')[:-1]) + '.mp3'
        arglist = [ ffmpegfname,
                    '-y',
                    '-i',
                    file,
                    '-ab',
                    brlow,
                    '-map_metadata',
                    '0',
                    '-id3v2_version',
                    '3',
                    outfname ]
        subprocess.run(arglist)
        if isAudio(outfname):
            convcount += 1
    if len(filleList) == convcount:
        print('Done. All files (' + str(convcount) + ') successfully converted.')
    else:
        print('Done. Converted ' + str(convcount) + ' off ' + str(len(filleList)) + ' files.')