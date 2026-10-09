import sys, os
_d = os.path.dirname(os.path.abspath(__file__))
while _d != os.path.dirname(_d):
    if os.path.isdir(os.path.join(_d, "tools")) and os.path.isdir(os.path.join(_d, "dataset")):
        sys.path.insert(0, os.path.join(_d, "tools")); break
    _d = os.path.dirname(_d)
import family21_multiwaycut as M
def validate(input_text, output_text):
    text, out = input_text, output_text
    return M.validate(text,out,two=False)
