import googletrans
from esymbol import punctuation


'''
googletrans is 4.0.0
A new version for Increase running speed

Output:
    1. VariableName (which is for class name)
    2. variableName (which if for function name or common variable name)
    3. variable_name(which is for all)

Input:
    All,may include Chinese characters and English alphabet, or other symbols.

What should we do?
    1. Translate Chinese into English
    2. Remove extraneous characters
    3. Match the required format

'''

class Translator:
    def __init__(self,source = 'translate.google.cn'):
        self.source_url = source
        self.transOperator = googletrans.Translator(service_urls=[self.source_url])
    
    def ect(self,chinese_sentence = "你好"):
        return self.transOperator.translate(chinese_sentence).text

class Beautify:
    def __init__(self):
        pass
