from os_ import OS
from proglang import ProgLang

OS_TO_PROGLANGS = {
    OS.CPM: frozenset({ProgLang.ASM, ProgLang.PLM}),
    OS.NETBSD: frozenset({ProgLang.ASM, ProgLang.C}),
    OS.PCDOS: frozenset({ProgLang.ASM, ProgLang.C}),
}
