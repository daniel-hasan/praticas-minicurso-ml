from abc import abstractmethod
from .resultado import Resultado
import pandas as pd
from sklearn.base import ClassifierMixin, RegressorMixin

from typing import List,Union
class MetodoAprendizadoDeMaquina:

    @abstractmethod
    def eval(self,df_treino:pd.DataFrame, df_data_to_predict:pd.DataFrame, col_classe:str) -> Resultado:
        raise NotImplementedError
