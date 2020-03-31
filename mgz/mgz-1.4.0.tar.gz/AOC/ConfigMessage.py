# automatically generated by the FlatBuffers compiler, do not modify

# namespace: AOC

import flatbuffers

class ConfigMessage(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsConfigMessage(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConfigMessage()
        x.Init(buf, n + offset)
        return x

    # ConfigMessage
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ConfigMessage
    def MessageIntervalMs(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 1000

    # ConfigMessage
    def UpdateCycles(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 1

def ConfigMessageStart(builder): builder.StartObject(2)
def ConfigMessageAddMessageIntervalMs(builder, messageIntervalMs): builder.PrependUint32Slot(0, messageIntervalMs, 1000)
def ConfigMessageAddUpdateCycles(builder, updateCycles): builder.PrependUint32Slot(1, updateCycles, 1)
def ConfigMessageEnd(builder): return builder.EndObject()
