from pangeamt_nlp.processor.base.validator_base import ValidatorBase
from pangeamt_nlp.utils.lang_detector import LangDetector
from pangeamt_nlp.seg import Seg


class LanguageChecker(ValidatorBase):
    NAME = "language_checker"

    DESCRIPTION_TRAINING = """
        Remove pair of sentence if the language does not match with src_lang and tgt_lang
    """

    DESCRIPTION_DECODING = """
        Validators do not apply to decoding.
    """

    def __init__(self, src_lang: str, tgt_lang: str) -> None:
        super().__init__(src_lang, tgt_lang)

    def validate(self, seg: Seg) -> bool:
        if len(seg.src.split(' ')) > 3:
            lang_detector = LangDetector()
            src_detection = lang_detector.detect(text=seg.src, hint_language=self.src_lang)
            tgt_detection = lang_detector.detect(text=seg.tgt, hint_language=self.tgt_lang)

            if src_detection != self.src_lang or tgt_detection != self.tgt_lang:
                return False

        return True


