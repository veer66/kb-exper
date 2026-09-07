from os_ import OS
from proglang import ProgLang

os_to_proglangs = {
    OS.CPM: {ProgLang.ASM, ProgLang.PLM},
    OS.NETBSD: {ProgLang.ASM, ProgLang.C},
    OS.PCDOS: {ProgLang.ASM, ProgLang.C},
}
