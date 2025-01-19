# Generated from hrvatski_turisticki.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,33,100,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,0,1,
        0,1,0,4,0,31,8,0,11,0,12,0,32,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,3,1,
        3,1,3,1,3,1,3,1,3,3,3,48,8,3,1,3,3,3,51,8,3,3,3,53,8,3,1,3,1,3,1,
        3,3,3,58,8,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,
        72,8,5,1,6,1,6,1,6,1,7,3,7,78,8,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,3,9,92,8,9,3,9,94,8,9,1,10,1,10,1,11,1,11,1,11,
        0,0,12,0,2,4,6,8,10,12,14,16,18,20,22,0,3,1,0,9,10,1,0,22,28,1,0,
        30,32,106,0,30,1,0,0,0,2,36,1,0,0,0,4,38,1,0,0,0,6,52,1,0,0,0,8,
        59,1,0,0,0,10,71,1,0,0,0,12,73,1,0,0,0,14,77,1,0,0,0,16,81,1,0,0,
        0,18,93,1,0,0,0,20,95,1,0,0,0,22,97,1,0,0,0,24,31,3,2,1,0,25,31,
        3,4,2,0,26,31,3,8,4,0,27,31,3,12,6,0,28,31,3,16,8,0,29,31,3,18,9,
        0,30,24,1,0,0,0,30,25,1,0,0,0,30,26,1,0,0,0,30,27,1,0,0,0,30,28,
        1,0,0,0,30,29,1,0,0,0,31,32,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,
        33,34,1,0,0,0,34,35,5,0,0,1,35,1,1,0,0,0,36,37,5,1,0,0,37,3,1,0,
        0,0,38,39,5,2,0,0,39,40,3,6,3,0,40,5,1,0,0,0,41,53,5,9,0,0,42,43,
        5,11,0,0,43,53,5,12,0,0,44,53,5,10,0,0,45,47,5,6,0,0,46,48,5,7,0,
        0,47,46,1,0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,49,51,5,8,0,0,50,49,
        1,0,0,0,50,51,1,0,0,0,51,53,1,0,0,0,52,41,1,0,0,0,52,42,1,0,0,0,
        52,44,1,0,0,0,52,45,1,0,0,0,52,53,1,0,0,0,53,54,1,0,0,0,54,57,3,
        20,10,0,55,56,5,29,0,0,56,58,3,22,11,0,57,55,1,0,0,0,57,58,1,0,0,
        0,58,7,1,0,0,0,59,60,5,3,0,0,60,61,3,10,5,0,61,9,1,0,0,0,62,63,5,
        13,0,0,63,72,3,20,10,0,64,65,5,9,0,0,65,66,5,14,0,0,66,72,3,20,10,
        0,67,68,5,5,0,0,68,69,5,9,0,0,69,70,5,14,0,0,70,72,3,20,10,0,71,
        62,1,0,0,0,71,64,1,0,0,0,71,67,1,0,0,0,72,11,1,0,0,0,73,74,5,4,0,
        0,74,75,3,14,7,0,75,13,1,0,0,0,76,78,7,0,0,0,77,76,1,0,0,0,77,78,
        1,0,0,0,78,79,1,0,0,0,79,80,3,20,10,0,80,15,1,0,0,0,81,82,5,15,0,
        0,82,17,1,0,0,0,83,84,5,16,0,0,84,85,5,11,0,0,85,94,5,17,0,0,86,
        87,5,18,0,0,87,94,5,11,0,0,88,89,5,19,0,0,89,91,5,20,0,0,90,92,5,
        21,0,0,91,90,1,0,0,0,91,92,1,0,0,0,92,94,1,0,0,0,93,83,1,0,0,0,93,
        86,1,0,0,0,93,88,1,0,0,0,94,19,1,0,0,0,95,96,7,1,0,0,96,21,1,0,0,
        0,97,98,7,2,0,0,98,23,1,0,0,0,10,30,32,47,50,52,57,71,77,91,93
    ]

class hrvatski_turistickiParser ( Parser ):

    grammarFileName = "hrvatski_turisticki.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'gdje'", "'koliko'", "<INVALID>", 
                     "<INVALID>", "'mogu'", "'li'", "<INVALID>", "'je'", 
                     "'su'", "'se'", "'nalazi'", "<INVALID>", "<INVALID>", 
                     "'hvala'", "'kako'", "<INVALID>", "'predstavi'", "'tko'", 
                     "'si'", "'ti'", "'muzej'", "'hotel'", "'restoran'", 
                     "'konoba'" ]

    symbolicNames = [ "<INVALID>", "POZDRAV", "GDJE", "KOLIKO", "KAKAV", 
                      "KOJA", "MOGU", "LI", "NACI", "JE", "SU", "SE", "NALAZI", 
                      "KOSTA", "CIJENA", "HVALA", "KAKO", "ZOVES", "PREDSTAVI", 
                      "TKO", "SI", "TI", "MUZEJ", "HOTEL", "RESTORAN", "KONOBA", 
                      "KAFIC", "PLAZA", "ATRAKCIJA", "PRIJEDLOG", "GRAD", 
                      "REGIJA", "MJESTO", "WS" ]

    RULE_razgovor = 0
    RULE_pozdravniIzraz = 1
    RULE_gdjeUpit = 2
    RULE_lokacijski_upit = 3
    RULE_kolikoUpit = 4
    RULE_cjenovni_upit = 5
    RULE_kakovUpit = 6
    RULE_opisni_upit = 7
    RULE_zahvalaIzjava = 8
    RULE_imeUpit = 9
    RULE_turisticki_objekt = 10
    RULE_lokacija = 11

    ruleNames =  [ "razgovor", "pozdravniIzraz", "gdjeUpit", "lokacijski_upit", 
                   "kolikoUpit", "cjenovni_upit", "kakovUpit", "opisni_upit", 
                   "zahvalaIzjava", "imeUpit", "turisticki_objekt", "lokacija" ]

    EOF = Token.EOF
    POZDRAV=1
    GDJE=2
    KOLIKO=3
    KAKAV=4
    KOJA=5
    MOGU=6
    LI=7
    NACI=8
    JE=9
    SU=10
    SE=11
    NALAZI=12
    KOSTA=13
    CIJENA=14
    HVALA=15
    KAKO=16
    ZOVES=17
    PREDSTAVI=18
    TKO=19
    SI=20
    TI=21
    MUZEJ=22
    HOTEL=23
    RESTORAN=24
    KONOBA=25
    KAFIC=26
    PLAZA=27
    ATRAKCIJA=28
    PRIJEDLOG=29
    GRAD=30
    REGIJA=31
    MJESTO=32
    WS=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RazgovorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(hrvatski_turistickiParser.EOF, 0)

        def pozdravniIzraz(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hrvatski_turistickiParser.PozdravniIzrazContext)
            else:
                return self.getTypedRuleContext(hrvatski_turistickiParser.PozdravniIzrazContext,i)


        def gdjeUpit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hrvatski_turistickiParser.GdjeUpitContext)
            else:
                return self.getTypedRuleContext(hrvatski_turistickiParser.GdjeUpitContext,i)


        def kolikoUpit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hrvatski_turistickiParser.KolikoUpitContext)
            else:
                return self.getTypedRuleContext(hrvatski_turistickiParser.KolikoUpitContext,i)


        def kakovUpit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hrvatski_turistickiParser.KakovUpitContext)
            else:
                return self.getTypedRuleContext(hrvatski_turistickiParser.KakovUpitContext,i)


        def zahvalaIzjava(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hrvatski_turistickiParser.ZahvalaIzjavaContext)
            else:
                return self.getTypedRuleContext(hrvatski_turistickiParser.ZahvalaIzjavaContext,i)


        def imeUpit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hrvatski_turistickiParser.ImeUpitContext)
            else:
                return self.getTypedRuleContext(hrvatski_turistickiParser.ImeUpitContext,i)


        def getRuleIndex(self):
            return hrvatski_turistickiParser.RULE_razgovor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRazgovor" ):
                listener.enterRazgovor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRazgovor" ):
                listener.exitRazgovor(self)




    def razgovor(self):

        localctx = hrvatski_turistickiParser.RazgovorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_razgovor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 24
                    self.pozdravniIzraz()
                    pass
                elif token in [2]:
                    self.state = 25
                    self.gdjeUpit()
                    pass
                elif token in [3]:
                    self.state = 26
                    self.kolikoUpit()
                    pass
                elif token in [4]:
                    self.state = 27
                    self.kakovUpit()
                    pass
                elif token in [15]:
                    self.state = 28
                    self.zahvalaIzjava()
                    pass
                elif token in [16, 18, 19]:
                    self.state = 29
                    self.imeUpit()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 32 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 884766) != 0)):
                    break

            self.state = 34
            self.match(hrvatski_turistickiParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PozdravniIzrazContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POZDRAV(self):
            return self.getToken(hrvatski_turistickiParser.POZDRAV, 0)

        def getRuleIndex(self):
            return hrvatski_turistickiParser.RULE_pozdravniIzraz

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPozdravniIzraz" ):
                listener.enterPozdravniIzraz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPozdravniIzraz" ):
                listener.exitPozdravniIzraz(self)




    def pozdravniIzraz(self):

        localctx = hrvatski_turistickiParser.PozdravniIzrazContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_pozdravniIzraz)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(hrvatski_turistickiParser.POZDRAV)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GdjeUpitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GDJE(self):
            return self.getToken(hrvatski_turistickiParser.GDJE, 0)

        def lokacijski_upit(self):
            return self.getTypedRuleContext(hrvatski_turistickiParser.Lokacijski_upitContext,0)


        def getRuleIndex(self):
            return hrvatski_turistickiParser.RULE_gdjeUpit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGdjeUpit" ):
                listener.enterGdjeUpit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGdjeUpit" ):
                listener.exitGdjeUpit(self)




    def gdjeUpit(self):

        localctx = hrvatski_turistickiParser.GdjeUpitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_gdjeUpit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(hrvatski_turistickiParser.GDJE)
            self.state = 39
            self.lokacijski_upit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lokacijski_upitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def turisticki_objekt(self):
            return self.getTypedRuleContext(hrvatski_turistickiParser.Turisticki_objektContext,0)


        def JE(self):
            return self.getToken(hrvatski_turistickiParser.JE, 0)

        def SE(self):
            return self.getToken(hrvatski_turistickiParser.SE, 0)

        def NALAZI(self):
            return self.getToken(hrvatski_turistickiParser.NALAZI, 0)

        def SU(self):
            return self.getToken(hrvatski_turistickiParser.SU, 0)

        def MOGU(self):
            return self.getToken(hrvatski_turistickiParser.MOGU, 0)

        def PRIJEDLOG(self):
            return self.getToken(hrvatski_turistickiParser.PRIJEDLOG, 0)

        def lokacija(self):
            return self.getTypedRuleContext(hrvatski_turistickiParser.LokacijaContext,0)


        def LI(self):
            return self.getToken(hrvatski_turistickiParser.LI, 0)

        def NACI(self):
            return self.getToken(hrvatski_turistickiParser.NACI, 0)

        def getRuleIndex(self):
            return hrvatski_turistickiParser.RULE_lokacijski_upit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLokacijski_upit" ):
                listener.enterLokacijski_upit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLokacijski_upit" ):
                listener.exitLokacijski_upit(self)




    def lokacijski_upit(self):

        localctx = hrvatski_turistickiParser.Lokacijski_upitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_lokacijski_upit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.state = 41
                self.match(hrvatski_turistickiParser.JE)
                pass
            elif token in [11]:
                self.state = 42
                self.match(hrvatski_turistickiParser.SE)
                self.state = 43
                self.match(hrvatski_turistickiParser.NALAZI)
                pass
            elif token in [10]:
                self.state = 44
                self.match(hrvatski_turistickiParser.SU)
                pass
            elif token in [6]:
                self.state = 45
                self.match(hrvatski_turistickiParser.MOGU)
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 46
                    self.match(hrvatski_turistickiParser.LI)


                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==8:
                    self.state = 49
                    self.match(hrvatski_turistickiParser.NACI)


                pass
            elif token in [22, 23, 24, 25, 26, 27, 28]:
                pass
            else:
                pass
            self.state = 54
            self.turisticki_objekt()
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 55
                self.match(hrvatski_turistickiParser.PRIJEDLOG)
                self.state = 56
                self.lokacija()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KolikoUpitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KOLIKO(self):
            return self.getToken(hrvatski_turistickiParser.KOLIKO, 0)

        def cjenovni_upit(self):
            return self.getTypedRuleContext(hrvatski_turistickiParser.Cjenovni_upitContext,0)


        def getRuleIndex(self):
            return hrvatski_turistickiParser.RULE_kolikoUpit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKolikoUpit" ):
                listener.enterKolikoUpit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKolikoUpit" ):
                listener.exitKolikoUpit(self)




    def kolikoUpit(self):

        localctx = hrvatski_turistickiParser.KolikoUpitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_kolikoUpit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(hrvatski_turistickiParser.KOLIKO)
            self.state = 60
            self.cjenovni_upit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cjenovni_upitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KOSTA(self):
            return self.getToken(hrvatski_turistickiParser.KOSTA, 0)

        def turisticki_objekt(self):
            return self.getTypedRuleContext(hrvatski_turistickiParser.Turisticki_objektContext,0)


        def JE(self):
            return self.getToken(hrvatski_turistickiParser.JE, 0)

        def CIJENA(self):
            return self.getToken(hrvatski_turistickiParser.CIJENA, 0)

        def KOJA(self):
            return self.getToken(hrvatski_turistickiParser.KOJA, 0)

        def getRuleIndex(self):
            return hrvatski_turistickiParser.RULE_cjenovni_upit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCjenovni_upit" ):
                listener.enterCjenovni_upit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCjenovni_upit" ):
                listener.exitCjenovni_upit(self)




    def cjenovni_upit(self):

        localctx = hrvatski_turistickiParser.Cjenovni_upitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_cjenovni_upit)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.match(hrvatski_turistickiParser.KOSTA)
                self.state = 63
                self.turisticki_objekt()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.match(hrvatski_turistickiParser.JE)
                self.state = 65
                self.match(hrvatski_turistickiParser.CIJENA)
                self.state = 66
                self.turisticki_objekt()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.match(hrvatski_turistickiParser.KOJA)
                self.state = 68
                self.match(hrvatski_turistickiParser.JE)
                self.state = 69
                self.match(hrvatski_turistickiParser.CIJENA)
                self.state = 70
                self.turisticki_objekt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KakovUpitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KAKAV(self):
            return self.getToken(hrvatski_turistickiParser.KAKAV, 0)

        def opisni_upit(self):
            return self.getTypedRuleContext(hrvatski_turistickiParser.Opisni_upitContext,0)


        def getRuleIndex(self):
            return hrvatski_turistickiParser.RULE_kakovUpit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKakovUpit" ):
                listener.enterKakovUpit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKakovUpit" ):
                listener.exitKakovUpit(self)




    def kakovUpit(self):

        localctx = hrvatski_turistickiParser.KakovUpitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_kakovUpit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(hrvatski_turistickiParser.KAKAV)
            self.state = 74
            self.opisni_upit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Opisni_upitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def turisticki_objekt(self):
            return self.getTypedRuleContext(hrvatski_turistickiParser.Turisticki_objektContext,0)


        def JE(self):
            return self.getToken(hrvatski_turistickiParser.JE, 0)

        def SU(self):
            return self.getToken(hrvatski_turistickiParser.SU, 0)

        def getRuleIndex(self):
            return hrvatski_turistickiParser.RULE_opisni_upit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpisni_upit" ):
                listener.enterOpisni_upit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpisni_upit" ):
                listener.exitOpisni_upit(self)




    def opisni_upit(self):

        localctx = hrvatski_turistickiParser.Opisni_upitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_opisni_upit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9 or _la==10:
                self.state = 76
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 79
            self.turisticki_objekt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ZahvalaIzjavaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HVALA(self):
            return self.getToken(hrvatski_turistickiParser.HVALA, 0)

        def getRuleIndex(self):
            return hrvatski_turistickiParser.RULE_zahvalaIzjava

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterZahvalaIzjava" ):
                listener.enterZahvalaIzjava(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitZahvalaIzjava" ):
                listener.exitZahvalaIzjava(self)




    def zahvalaIzjava(self):

        localctx = hrvatski_turistickiParser.ZahvalaIzjavaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_zahvalaIzjava)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(hrvatski_turistickiParser.HVALA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImeUpitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KAKO(self):
            return self.getToken(hrvatski_turistickiParser.KAKO, 0)

        def SE(self):
            return self.getToken(hrvatski_turistickiParser.SE, 0)

        def ZOVES(self):
            return self.getToken(hrvatski_turistickiParser.ZOVES, 0)

        def PREDSTAVI(self):
            return self.getToken(hrvatski_turistickiParser.PREDSTAVI, 0)

        def TKO(self):
            return self.getToken(hrvatski_turistickiParser.TKO, 0)

        def SI(self):
            return self.getToken(hrvatski_turistickiParser.SI, 0)

        def TI(self):
            return self.getToken(hrvatski_turistickiParser.TI, 0)

        def getRuleIndex(self):
            return hrvatski_turistickiParser.RULE_imeUpit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImeUpit" ):
                listener.enterImeUpit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImeUpit" ):
                listener.exitImeUpit(self)




    def imeUpit(self):

        localctx = hrvatski_turistickiParser.ImeUpitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_imeUpit)
        self._la = 0 # Token type
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.match(hrvatski_turistickiParser.KAKO)
                self.state = 84
                self.match(hrvatski_turistickiParser.SE)
                self.state = 85
                self.match(hrvatski_turistickiParser.ZOVES)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.match(hrvatski_turistickiParser.PREDSTAVI)
                self.state = 87
                self.match(hrvatski_turistickiParser.SE)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.match(hrvatski_turistickiParser.TKO)
                self.state = 89
                self.match(hrvatski_turistickiParser.SI)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 90
                    self.match(hrvatski_turistickiParser.TI)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Turisticki_objektContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUZEJ(self):
            return self.getToken(hrvatski_turistickiParser.MUZEJ, 0)

        def HOTEL(self):
            return self.getToken(hrvatski_turistickiParser.HOTEL, 0)

        def RESTORAN(self):
            return self.getToken(hrvatski_turistickiParser.RESTORAN, 0)

        def KONOBA(self):
            return self.getToken(hrvatski_turistickiParser.KONOBA, 0)

        def KAFIC(self):
            return self.getToken(hrvatski_turistickiParser.KAFIC, 0)

        def PLAZA(self):
            return self.getToken(hrvatski_turistickiParser.PLAZA, 0)

        def ATRAKCIJA(self):
            return self.getToken(hrvatski_turistickiParser.ATRAKCIJA, 0)

        def getRuleIndex(self):
            return hrvatski_turistickiParser.RULE_turisticki_objekt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuristicki_objekt" ):
                listener.enterTuristicki_objekt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuristicki_objekt" ):
                listener.exitTuristicki_objekt(self)




    def turisticki_objekt(self):

        localctx = hrvatski_turistickiParser.Turisticki_objektContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_turisticki_objekt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 532676608) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LokacijaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GRAD(self):
            return self.getToken(hrvatski_turistickiParser.GRAD, 0)

        def REGIJA(self):
            return self.getToken(hrvatski_turistickiParser.REGIJA, 0)

        def MJESTO(self):
            return self.getToken(hrvatski_turistickiParser.MJESTO, 0)

        def getRuleIndex(self):
            return hrvatski_turistickiParser.RULE_lokacija

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLokacija" ):
                listener.enterLokacija(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLokacija" ):
                listener.exitLokacija(self)




    def lokacija(self):

        localctx = hrvatski_turistickiParser.LokacijaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_lokacija)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7516192768) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





