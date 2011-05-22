import sys

# Forcibly insert path for `setup.py build` output, so that we import from the
# ``2to3`` converted sources.  This is an ugly hack, but it saves an enormous
# amount of grief in handling Python 2 and 3.
sys.path.insert(0, 'build/lib')
