

class RemoteShell:

    _BUFFER_SIZE = 2048

    _BEGIN_FLAG = "####RSHB####"

    _END_FLAG = "####RSHE####"

    _EXIT = "exit"

    _VERBOSE = False