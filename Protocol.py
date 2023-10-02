class Response:
    state:str = None
    response:tuple = None
    def __init__(self, arg, *kargs) -> None:
        if(arg == "err"):
            self.state = "Error"
        else:
            self.state = "Sucess"
            self.response = kargs

class Execute:
    def dum(self, *args) -> Response:
        pass
    def auth(self, *args) -> Response:
        pass
    def access(self, *args) -> Response:
        pass

class Protocol:
    __prot__:dict = None
    __exe__:Execute = None

    def __init__(self) -> None:
        self.__exe__ = Execute()
        self.__prot__['DUM'] = self.__exe__.dum
        self.__prot__['AUTH']= self.__exe__.auth
        self.__prot__['ACC'] = self.__exe__.access
        # lly
    
    def eval(self, cmd:str) -> Response:
        cmdLst = cmd.split()
        if len(cmdLst) == 0 or (cmdLst[0] not in self.__prot__.keys):
            return Response('err')
        
        return self.__prot__[cmdLst[0]](cmdLst)