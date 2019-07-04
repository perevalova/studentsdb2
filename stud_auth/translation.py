from modeltranslation.translator import translator, TranslationOptions
from stud_auth.models import StProfile


class StProfileTranslationOptions(TranslationOptions):
    fields = ('photo', 'mobile_phone', 'passport', 'city', 'street', 'house',)

translator.register(StProfile, StProfileTranslationOptions)