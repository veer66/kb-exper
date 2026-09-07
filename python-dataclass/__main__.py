from os_ import OS
from platform_ import Platform
from proglang import ProgLang


oses = [
    OS(name="CP/M",
       inception=1974,
       platforms=frozenset({Platform.I8080, Platform.I8085, Platform.I8086, Platform.M68K, Platform.Z80, Platform.Z8K}),
       proglangs=frozenset({ProgLang.ASM, ProgLang.PLM}),
    ),
    OS(name="NetBSD",
       inception=1993,
       platforms=frozenset({Platform.ALPHA, Platform.ARM, Platform.M68K, Platform.MIPS, Platform.PARISC, Platform.SUPERH, Platform.VAX, Platform.X86, Platform.RISCV}),
       proglangs=frozenset({ProgLang.ASM, ProgLang.C}),
    ),
    OS(name="PC-DOS",
       inception=1981,
       platforms=frozenset({Platform.X86}),
       proglangs=frozenset({ProgLang.ASM, ProgLang.C})
    ),
]




