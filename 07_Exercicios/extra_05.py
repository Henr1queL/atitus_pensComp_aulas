def status_aluno(notas):
     a = int(imput("Colouqe a primeira nota"))
b = int(imput("Coloque a segunda nota"))
c = int(imput("Colouque a terceira nota"))
d = int(imput("Colouqe a quarta nota"))

media = (a + b + c + d) / 4

if media >= 7:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")

assert status_aluno([10, 10, 10, 10])
assert status_aluno([10, None, 10, 10])

assert not status_aluno([10, 5, None, 5])
assert not status_aluno([5, 5, 5, 5])
assert not status_aluno([0, 0, 0, 0])
