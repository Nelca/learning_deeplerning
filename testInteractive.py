import inspect
import pdb

def handle_stackframe_without_leak():
    frame = inspect.currentframe()

    pdb.set_trace()

    try:
        print(frame)

    # do something with the frame
    finally:
        del frame



handle_stackframe_without_leak()
