from os_ import OS
from platform_ import Platform


os_to_platforms = {
    OS.CPM: frozenset({Platform.I8080, Platform.I8085, Platform.I8086, Platform.M68K, Platform.Z80, Platform.Z8K}),
    OS.NETBSD: frozenset({Platform.ALPHA, Platform.ARM, Platform.M68K, Platform.MIPS, Platform.PARISC, Platform.SUPERH, Platform.VAX, Platform.X86, Platform.RISCV}),
    OS.PCDOS: frozenset({Platform.X86}),
}
