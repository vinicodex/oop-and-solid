class Alarm:

    def __init__(self, status:bool) -> None:
        self.__status = status
    

    def get_status(self) -> None:
        return self.__status
    
    def set_status(self, valor: bool) -> None:
        if isinstance(valor, bool):
            self.__status = valor