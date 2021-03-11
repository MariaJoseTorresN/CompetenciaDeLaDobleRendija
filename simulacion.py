import clasicoACuantico as cAc

def probabilisticSimulator():
    unClick = cAc.multiplesRendijasClasicoProbabilistico(2, 3, 1)
    dosClicks = cAc.multiplesRendijasClasicoProbabilistico(2, 3, 2)
    tresClicks = cAc.multiplesRendijasClasicoProbabilistico(2, 3, 3)
    print(unClick)
    print(dosClicks)
    print(tresClicks)
    cAc.diagramaProbabilistico(unClick[1])
    cAc.diagramaProbabilistico(dosClicks[1])
    cAc.diagramaProbabilistico(tresClicks[1])

def quantumSimulator():
    unClick = cAc.multiplesRendijasCuantico(2,3,1)
    dosClicks = cAc.multiplesRendijasCuantico(2,3,2)
    tresClicks = cAc.multiplesRendijasCuantico(2,3,3)
    print(unClick)
    print(dosClicks)
    print(tresClicks)
    cAc.diagramaCuantico(unClick[1])
    cAc.diagramaCuantico(dosClicks[1])
    cAc.diagramaCuantico(tresClicks[1])

