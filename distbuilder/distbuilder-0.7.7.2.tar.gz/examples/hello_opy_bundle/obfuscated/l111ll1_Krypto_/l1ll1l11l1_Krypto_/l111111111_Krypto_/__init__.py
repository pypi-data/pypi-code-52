# coding: utf-8
from sys import version_info as __1l111l_Krypto_
l1lll_Krypto_ = __1l111l_Krypto_[0] == 2
l1l11ll_Krypto_ = 2048
l1l11_Krypto_ = 7
def l1l1111_Krypto_ (l1ll1l1_Krypto_):
    global l1l1l11_Krypto_
    l1111_Krypto_ = ord (l1ll1l1_Krypto_ [-1])
    l11l_Krypto_ = l1ll1l1_Krypto_ [:-1]
    l1l1lll_Krypto_ = l1111_Krypto_ % len (l11l_Krypto_)
    l11ll1_Krypto_ = l11l_Krypto_ [:l1l1lll_Krypto_] + l11l_Krypto_ [l1l1lll_Krypto_:]
    if l1lll_Krypto_:
        l1l_Krypto_ = unicode () .join ([unichr (ord (char) - l1l11ll_Krypto_ - (l11l1_Krypto_ + l1111_Krypto_) % l1l11_Krypto_) for l11l1_Krypto_, char in enumerate (l11ll1_Krypto_)])
    else:
        l1l_Krypto_ = str () .join ([chr (ord (char) - l1l11ll_Krypto_ - (l11l1_Krypto_ + l1111_Krypto_) % l1l11_Krypto_) for l11l1_Krypto_, char in enumerate (l11ll1_Krypto_)])
    return eval (l1l_Krypto_)
l1l1111_Krypto_ (u"ࠣࠤࠥࡔࡷࡵࡶࡪࡦࡨࡷࠥࡧࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮࠯࡬ࡲࡩ࡫ࡰࡦࡰࡧࡩࡳࡺࠠࡪࡰࡷࡩࡷ࡬ࡡࡤࡧࠣࡸࡴࠦࡴࡩࡧࠣࡶࡦࡴࡤࡰ࡯ࠣࡲࡺࡳࡢࡦࡴࠣ࡫ࡪࡴࡥࡳࡣࡷࡳࡷࡹࠊࡴࡷࡳࡴࡱ࡯ࡥࡥࠢࡥࡽࠥࡼࡡࡳ࡫ࡲࡹࡸࠦ࡯ࡱࡧࡵࡥࡹ࡯࡮ࡨࠢࡶࡽࡸࡺࡥ࡮ࡵ࠱ࠦࠧࠨ੥")
__revision__ = l1l1111_Krypto_ (u"ࠤࠧࡍࡩࠪࠢ੦")
import os as l1111111l1_Krypto_
if l1111111l1_Krypto_.name == l1l1111_Krypto_ (u"ࠪࡴࡴࡹࡩࡹࠩ੧"):
    from l111ll1_Krypto_.l1ll1l11l1_Krypto_.l111111111_Krypto_.l1lll11l1ll_Krypto_ import new
elif l1111111l1_Krypto_.name == l1l1111_Krypto_ (u"ࠫࡳࡺࠧ੨"):
    from l111ll1_Krypto_.l1ll1l11l1_Krypto_.l111111111_Krypto_.l1lll11ll11_Krypto_ import new
elif hasattr(l1111111l1_Krypto_, l1l1111_Krypto_ (u"ࠬࡻࡲࡢࡰࡧࡳࡲ࠭੩")):
    from l111ll1_Krypto_.l1ll1l11l1_Krypto_.l111111111_Krypto_.fallback import new
else:
    raise ImportError(l1l1111_Krypto_ (u"ࠨࡎࡰࡶࠣ࡭ࡲࡶ࡬ࡦ࡯ࡨࡲࡹ࡫ࡤࠣ੪"))