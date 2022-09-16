# QUANTCONNECT.COM - Democratizing Finance, Empowering Individuals.
# Lean Algorithmic Trading Engine v2.0. Copyright 2014 QuantConnect Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from AlgorithmImports import *
from System import *

### <summary>
### Regression algorithm illustrating how to request history data for different data mapping modes.
### </summary>
class HistoryWithDifferentDataMappingModeRegressionAlgorithm(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2013, 10, 6)
        self.SetEndDate(2014, 1, 1)
        self._continuousContractSymbol = self.AddFuture(Futures.Indices.SP500EMini, Resolution.Daily).Symbol

    def OnEndOfAlgorithm(self):
        dataMappingModes = [DataMappingMode(x) for x in Enum.GetValues(DataMappingMode)]
        historyResults = [
            self.History([self._continuousContractSymbol], self.StartDate, self.EndDate, Resolution.Daily, dataMappingMode=dataMappingMode)
                .droplevel(0, axis=0)
                .loc[self._continuousContractSymbol]
                .close
            for dataMappingMode in dataMappingModes
        ]

        if any(x.size != historyResults[0].size for x in historyResults):
            raise Exception("History results bar count did not match")

        # Check that close prices at each time are different for different data mapping modes
        for j in range(historyResults[0].size):
            closePrices = set(historyResults[i][j] for i in range(len(historyResults)))
            if len(closePrices) != len(dataMappingModes):
                raise Exception("History results close prices should have been different for each data mapping mode at each time")
