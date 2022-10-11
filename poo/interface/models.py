import abc


class Usuario:
    def autenticar(self):
        print("autenticado")

class Cliente:
    pass


class Autenticavel(abc.ABC):

    @abc.abstractclassmethod
    def autenticar(self):
        pass

class Autentica():

    def autenticar(self, obj):
        if(isinstance(obj, Autenticavel)):
            print("Correto.")
        else:
            print("nao eh autentivael")


if __name__ == '__main__':
    autenticavel = Autenticavel()

    usuario = Usuario()
    autenticavel.register(usuario)

    autentica = Autentica()
    autentica.autenticar()

