# automatically generated by the FlatBuffers compiler, do not modify

# namespace: AOC

import flatbuffers

class VictoryPoints(object):
    __slots__ = ['_tab']

    # VictoryPoints
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # VictoryPoints
    def RelicsCaptured(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # VictoryPoints
    def RelicGold(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(4))
    # VictoryPoints
    def TradeProfit(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(8))
    # VictoryPoints
    def TributeReceived(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(12))
    # VictoryPoints
    def TributeSent(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(16))
    # VictoryPoints
    def TotalFood(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(20))
    # VictoryPoints
    def TotalWood(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(24))
    # VictoryPoints
    def TotalGold(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(28))
    # VictoryPoints
    def TotalStone(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(32))
    # VictoryPoints
    def ValueSpentObjects(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(36))
    # VictoryPoints
    def ValueSpentResearch(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(40))
    # VictoryPoints
    def ValueLostUnits(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(44))
    # VictoryPoints
    def ValueLostBuildings(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(48))
    # VictoryPoints
    def ValueCurrentUnits(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(52))
    # VictoryPoints
    def ValueCurrentBuildings(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(56))
    # VictoryPoints
    def ValueObjectsDestroyed(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(60))

def CreateVictoryPoints(builder, relicsCaptured, relicGold, tradeProfit, tributeReceived, tributeSent, totalFood, totalWood, totalGold, totalStone, valueSpentObjects, valueSpentResearch, valueLostUnits, valueLostBuildings, valueCurrentUnits, valueCurrentBuildings, valueObjectsDestroyed):
    builder.Prep(4, 64)
    builder.PrependFloat32(valueObjectsDestroyed)
    builder.PrependFloat32(valueCurrentBuildings)
    builder.PrependFloat32(valueCurrentUnits)
    builder.PrependFloat32(valueLostBuildings)
    builder.PrependFloat32(valueLostUnits)
    builder.PrependFloat32(valueSpentResearch)
    builder.PrependFloat32(valueSpentObjects)
    builder.PrependFloat32(totalStone)
    builder.PrependFloat32(totalGold)
    builder.PrependFloat32(totalWood)
    builder.PrependFloat32(totalFood)
    builder.PrependFloat32(tributeSent)
    builder.PrependFloat32(tributeReceived)
    builder.PrependFloat32(tradeProfit)
    builder.PrependFloat32(relicGold)
    builder.PrependFloat32(relicsCaptured)
    return builder.Offset()
