:- style_check(-discontiguous).
:- initialization(main).

% CP/M
name(cpm,"CP/M").
inception(cpm,1974).
platform(cpm,i8080).
platform(cpm,i8085).
platform(cpm,i8086).
platform(cpm,m68k).
platform(cpm,z80).
platform(cpm,z8k).
proglang(cpm,asm).
proglang(cpm,plm).

% NetBSD
name(netbsd,"NetBSD").
inception(netbsd,1993).
platform(netbsd,alpha).
platform(netbsd,arm).
platform(netbsd,m68k).
platform(netbsd,mips).
platform(netbsd,parisc).
platform(netbsd,superh).
platform(netbsd,vax).
platform(netbsd,x86).
platform(netbsd,riscv).

% PC-DOS
name(pcdos,"PC-DOS").
inception(pcdos,1981).
platform(pcdos,x86).
proglang(pcdos,asm).
proglang(pcdos,c).

% Rules
main :- forall((name(OS, Name), inception(OS, Year)),
	       format("~w@~w~n", [Name, Year])).
