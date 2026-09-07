from os_ import OS
from platform import Platform


os_to_platforms = {
    OS.CPM: {Platform.I8080, Platform.I8085, Platform.I8086, Platform.M68K, Platform.Z80, Platform.Z8K},
    OS.NETBSD: {Platform.ALPHA, Platform.ARM, Platform.M68K, Platform.MIPS, Platform.PARISC, Platform.SUPERH, Platform.VAX, Platform.X86, Platform.RISCV},
    OS.PCDOS: {Platform.X86},
}
