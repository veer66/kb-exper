(def oses [{:name "CP/M"
            :inception 1974
            :platforms #{:I8080 :I8085 :I8086 :M68K :Z80 :Z8K}
            :proglangs=#{:ASM, :PLM}}
           {:name "NetBSD"
            :inception 1993
            :platforms #{:ALPHA, :ARM, :M68K, :MIPS, :PARISC, :SUPERH, :VAX, :X86, :RISCV}
            :proglangs #{:ASM, :C}}
           {:name "PC-DOS"
            :inception 1981,
            :platforms #{:X86}
            :proglangs=#{:ASM, :C}}])

(defn name-inception-to-str [{:keys [name inception]}]
  (str name "@" inception))

(println (map name-inception-to-str oses))
