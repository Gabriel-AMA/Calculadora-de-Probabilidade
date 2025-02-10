import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def teste(dificuldade):
    _1d12 = np.ones(12) / 12
    _2d12 = np.convolve(_1d12, _1d12)
    #print(_2d12)
    resultado = {}
    resultado["Sucesso"] = 0
    resultado["Falha"] = 0
    resultado["Sucesso Parcial"] =0
    resultado["Sucesso Normal"] = 0
    resultado["Falha Normal"] = 0
    resultado["Sucesso Excep."] = _2d12[0]
    resultado["Sucesso Crít."] = ((1/12)**2)*5
    resultado["Falha Colos."] = _2d12[-1]
    resultado["Falha Crít."] = ((1/12)**2)*5

    for i in range(1,13):
      _2d12[(i*2)-2]-=(1/12)**2
    #print(_2d12)


    for i in range(1, 25):
      if i > dificuldade:
        resultado["Sucesso Normal"] += _2d12[i - 2]
      if i < dificuldade:
        resultado["Falha Normal"] += _2d12[i - 2]
      if i == dificuldade:
        resultado["Sucesso Parcial"] += _2d12[i - 2]

    resultado["Sucesso"] = resultado["Sucesso Normal"]+resultado["Sucesso Crít."]+resultado["Sucesso Excep."]
    resultado["Falha"] = resultado["Falha Normal"] + resultado["Falha Colos."]+resultado["Falha Crít."]


    return resultado