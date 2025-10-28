# fourth.py — doplňte tímto kódem funkci je_tah_mozny

def in_bounds(pos):
    """Vrátí True, pokud je pozice v rozmezí 1..8."""
    r, c = pos
    return 1 <= r <= 8 and 1 <= c <= 8

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

def path_clear(start, end, occupied):
    """
    Kontroluje, že mezi start a end (exkluzivně) není žádná figura.
    Předpokládá, že start a end leží v přímce (horizontálně, vertikálně nebo diagonálně).
    """
    r1, c1 = start
    r2, c2 = end
    dr = sign(r2 - r1)
    dc = sign(c2 - c1)

    # krokujeme od prvního pole za startem až po políčko před endem
    r, c = r1 + dr, c1 + dc
    while (r, c) != (r2, c2):
        if (r, c) in occupied:
            return False
        r += dr
        c += dc
    return True

def je_tah_mozny(figurka, start, cilova_pozice, obsazena):
    """
    figurka: str, jeden z: "pěšec", "jezdec", "věž", "střelec", "dáma", "král"
    start, cilova_pozice: (řádek, sloupec) v rozsahu 1..8
    obsazena: množina tuple pozic, které jsou obsazené (včetně startu)
    Vrací True, pokud je tah možný podle pravidel zadání (bez braní).
    """

    # 1) zkontrolovat hranice šachovnice
    if not in_bounds(cilova_pozice):
        return False

    # 2) cílové pole musí být volné (v úloze bez rozlišování barev neumožňujeme brát)
    if cilova_pozice in obsazena:
        return False

    r0, c0 = start
    rt, ct = cilova_pozice
    dr = rt - r0
    dc = ct - c0
    adr = abs(dr)
    adc = abs(dc)

    # žádný pohyb není pohyb
    if dr == 0 and dc == 0:
        return False

    fig = figurka.lower()

    # PĚŠEC: směr vpřed +1 (bílé). Smí jít 1 políčko vpřed pokud volno, nebo 2 z výchozího řádku 2.
    if fig == "pěšec" or fig == "pěsec":
        # pěšec se pohybuje pouze směrem +řádek (bez braní diagonálně)
        if dc != 0:
            return False
        # jeden krok vpřed
        if dr == 1:
            # cílové pole už je testováno jako volné => stačí True
            return True
        # dva kroky z výchozí pozice (řádek 2)
        if r0 == 2 and dr == 2:
            # zkontrolovat, že pole mezi není obsazeno a cílové je volné (cílové už bylo zkontrolováno)
            mezi = (r0 + 1, c0)
            if mezi in obsazena:
                return False
            return True
        return False

    # JEZDEC
    if fig == "jezdec":
        # L-tvar: (2,1) nebo (1,2)
        if (adr, adc) in ((2, 1), (1, 2)):
            return True
        return False

    # KRÁL
    if fig == "král" or fig == "kral":
        # jeden krok jakýmkoli směrem
        if max(adr, adc) == 1:
            return True
        return False

    # VĚŽ
    if fig == "věž" or fig == "vez" or fig == "vez'":  # různé možné zápisy
        # horizontální nebo vertikální pohyb
        if dr == 0 and dc != 0:
            return path_clear(start, cilova_pozice, obsazena)
        if dc == 0 and dr != 0:
            return path_clear(start, cilova_pozice, obsazena)
        return False

    # STŘELEC
    if fig == "střelec" or fig == "strelec":
        # diagonála: absolutní rozdíly stejné
        if adr == adc:
            return path_clear(start, cilova_pozice, obsazena)
        return False

    # DÁMA
    if fig == "dáma" or fig == "dama":
        # kombinuje věž a střelce
        if (dr == 0 and dc != 0) or (dc == 0 and dr != 0):
            return path_clear(start, cilova_pozice, obsazena)
        if adr == adc:
            return path_clear(start, cilova_pozice, obsazena)
        return False

    # jiná neznámá figura
    return False

