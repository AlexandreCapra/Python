class ValidaCpf:
    def __init__(self, string):
        self.cpf = string
        self.cpfLimpo = ""

    def removePontoTraco(self):
        self.cpfLimpo = self.cpf.replace(".", "").replace("-", "")


objCpf = ValidaCpf(input("Digite seu cpf: "))
print((objCpf.cpf))
objCpf.removePontoTraco()
print(objCpf.cpf)
print(objCpf.cpfLimpo)
