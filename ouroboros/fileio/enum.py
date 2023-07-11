import os, glob, fnmatch

def getDirectoryFiles(path, filter = '*.*', *, subdir = True) -> list[str]:
    # allfiles = []
    if filter == '*.*':
        filter = '*'
    elif not filter.startswith('*'):
        filter = '*' + filter

    if subdir:
        for root, dirs, files in os.walk(path):
            for f in files:
                f = os.path.join(root, f)
                if fnmatch.filter([f], filter) and not os.path.isdir(f):
                    yield f

            # fnmatch.filter([f], filter) and not os.path.isdir(f) and allfiles.append(f)

    else:
        for f in os.listdir(path):
            f = os.path.join(path, f)
            if fnmatch.filter([f], filter) and not os.path.isdir(f):
                yield f
