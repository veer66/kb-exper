from os_ import OS
from proglang import ProgLang

os_to_proglangs = {
    OS.CPM: frozenset({ProgLang.ASM, ProgLang.PLM}),
    OS.NETBSD: frozenset({ProgLang.ASM, ProgLang.C}),
    OS.PCDOS: frozenset({ProgLang.ASM, ProgLang.C}),
}
