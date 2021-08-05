import os, shutil, time

ProfilePath = os.path.expanduser('~')
directory = os.path.join(ProfilePath, 'AppData', 'Local', 'TheAscent', 'Saved', 'SaveGames')
filename = r'SaveProfiles.sav'
t = 3600 # seconds between checks


def periodic_backup_check():
    SaveFile = os.path.join(directory, filename)
    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(SaveFile)
    print('Current file mod time: ' + str(mtime))
    NewDir = os.path.join(directory, str(mtime))
    if os.path.isdir(NewDir):
        print('Backup already exists')
    else:
        print('Creating backup')
        os.mkdir(NewDir)
        shutil.copyfile(SaveFile, os.path.join(NewDir, filename))


def main():
    while True:
        periodic_backup_check()
        time.sleep(t)


if __name__ == '__main__':
    main()
