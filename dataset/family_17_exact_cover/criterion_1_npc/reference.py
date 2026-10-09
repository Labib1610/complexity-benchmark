import sys, os
_d = os.path.dirname(os.path.abspath(__file__))
while _d != os.path.dirname(_d):
    if os.path.isdir(os.path.join(_d, "tools")) and os.path.isdir(os.path.join(_d, "dataset")):
        sys.path.insert(0, os.path.join(_d, "tools")); break
    _d = os.path.dirname(_d)
import family17_exactcover as M
text=sys.stdin.read()
sys.stdout.write(M.x3c_reference(text))
