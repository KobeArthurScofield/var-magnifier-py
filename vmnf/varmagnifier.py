# VaLueMagNifier
# Main module

__errTable = {
    "debg": [0, "Debug", "Debug: "],
    "info": [1, "Info", "Info: "],
    "warn": [2, "Warning", "Warning: "],
    "erro": [3, "Error", "Error: "],
    "fatl": [4, "Fatal", "Fatal: "]
} # Errors List

__textHeader = "[VMNF]"

def __TextJoint(*texts):
    buffer = ""
    for text in texts:
        buffer = buffer.__add__(str(text))
    return buffer

def __AddHeader(*text):
    buffer = __textHeader
    for content in text:
        buffer = __TextJoint(buffer, content)
    return buffer

def __MsgPacker(message):
    buffer = ""
    if (isinstance(message, (str))):
        buffer = __TextJoint(buffer, message)
    else:
        for unit in message:
            buffer = __TextJoint(buffer, unit, " ")
    return buffer

def ConLogVar(*object):
    """
    Log any amounts of variables into the console window.
    """
    vHeader = "Variable: "
    buffer = vHeader
    for content in object:
        buffer = __TextJoint(buffer, type(content), content, "\t")
    print(__AddHeader(buffer))
    return 0

def ConLogMsg(*message):
    """
    Log any messages into the console window.
    """
    vHeader = "Message: "
    print(__AddHeader(__TextJoint(vHeader, __MsgPacker(message))))
    return 0

def __ConLogErr(err, *message):
    vHeader = err[2]
    print(__AddHeader(__TextJoint(vHeader, __MsgPacker(message))))
    return 0

def __PathTrim(path):
    if (path[0] == '"') or (path[0] == "'"):
        path = path[1:]
    if (path[-1] == '"') or (path[-1] == "'"):
        path = path[:-1]
    return path

def __PathConvert(path):
    if (isinstance(path, (str))):
        return __PathTrim(path)
    if (isinstance(path, (tuple))):
        buffer = []
        for object in path:
            if (isinstance(object, (str))):
                buffer.append(__PathTrim(object))
            else:
                __ConLogErr(__errTable.get("warn"), "Not a string object found in the path tuple.")
        if (not(buffer.__sizeof__()) == False):
            return buffer
        else:
            __ConLogErr(__errTable.get("erro"), "No path found in the given tuple.")
            return ""
    if (not(isinstance(path, (str, tuple)))):
        __ConLogErr(__errTable.get("erro"), "Path only accept string or tuple.")
        return ""

def __FlushLog(path, buffer):
    logf = open(path, OpenTextMode = "a+t", encoding = "utf-8")
    logf.write(__AddHeader(buffer))
    logf.close()
    return 0

def __OutputLog(path, buffer):
    if (not(path == "")):
        if(isinstance(path, (str))):
            __FlushLog(path, buffer)
        if(isinstance(path, (tuple))):
            for pathp in path:
                __FlushLog(pathp, buffer)
        return 0
    else:
        __ConLogErr(__errTable.get("erro"), "No path found for log output.")
        return -1

def FilLogVar(path, *object):
    """
    Log any variable once into file.
    Format is FilLogVar(path, *objects)
    path can be a string indicating to the file path, or a tuple of strings meaning several file path.
    """
    vHeader = "Variable: "
    buffer = vHeader
    for content in object:
        buffer = __TextJoint(buffer, type(content), content, "\t")
    logPath = __PathConvert(path)
    __OutputLog(logPath, buffer)
    return 0

def FilLogMsg(path, *message):
    """
    Log any messages once into file.
    Format is FilLogMsg(path, *message)
    path can be a string indicating to the file path, or a tuple of strings meaning several file path.
    """
    vHeader = "Message: "
    __OutputLog(__PathConvert(path), __TextJoint(vHeader, __MsgPacker(message)))
    return 0
