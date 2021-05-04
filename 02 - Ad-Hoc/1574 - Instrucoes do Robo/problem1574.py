def movimentarRobo(posicaoAtual, instrucaoAtual):  
    return moveRight(posicaoAtual) if instrucaoAtual == "RIGHT" else moveLeft(posicaoAtual)

def alterarInstrucao(instrucoes, instrucaoAtual, index):
    instIndex = instrucaoAtual[8:]
    inst = instrucoes[int(instIndex) - 1]
    instrucoes[index] = inst
    return instrucoes

def moveRight(posicao):
    return posicao + 1        

def moveLeft(posicao):
    return posicao - 1

t = int(input())

for i in range(t):
    instrucoes = []
    posicao = 0
    n = int(input())
    for j in range(n):
        inst = input()
        instrucoes.append(inst)
        if (inst == "LEFT" or inst == "RIGHT"):
            posicao = movimentarRobo(posicao, inst)
        else:
            instrucoes = alterarInstrucao(instrucoes, inst, j)        
            posicao = movimentarRobo(posicao, instrucoes[j])

    print(posicao)
