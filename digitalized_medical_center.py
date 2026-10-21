"""Gestione centro analisi mediche - OOP + NumPy."""

import numpy as np

# ---------------------------------------------------------------------------
# PARTE 1 - Variabili e tipi di dati
# ---------------------------------------------------------------------------
nome1, cognome1, cf1, eta1, peso1 = "Mario", "Rossi", "RSSMRA80A01H501U", 45, 78.5
analisi1 = ["emocromo", "glicemia", "colesterolo"]

nome2, cognome2, cf2, eta2, peso2 = "Laura", "Bianchi", "BNCLRA90B41F205X", 34, 61.2
analisi2 = ["glicemia", "trigliceridi", "emocromo"]

nome3, cognome3, cf3, eta3, peso3 = "Giuseppe", "Verdi", "VRDGPP65C15L219K", 59, 85.0
analisi3 = ["colesterolo", "glicemia", "creatinina"]


# ---------------------------------------------------------------------------
# PARTE 2 + 4 - Classi
# ---------------------------------------------------------------------------
class Analisi:
    """Singola analisi di laboratorio con valutazione rispetto a un range."""

    # Intervalli di riferimento inventati (min, max)
    RANGE_NORMA = {
        "glicemia": (70, 100),        # mg/dL
        "colesterolo": (125, 200),    # mg/dL
        "trigliceridi": (40, 150),    # mg/dL
        "creatinina": (0.6, 1.3),     # mg/dL
        "emocromo": (4.5, 11.0),      # globuli bianchi x10^3/uL
    }

    def __init__(self, tipo, risultato):
        self.tipo = tipo
        self.risultato = risultato

    def valuta(self):
        """Restituisce 'nella norma', 'basso' o 'alto'."""
        if self.tipo not in self.RANGE_NORMA:
            return "tipo di analisi sconosciuto"
        minimo, massimo = self.RANGE_NORMA[self.tipo]
        if self.risultato < minimo:
            return "basso"
        if self.risultato > massimo:
            return "alto"
        return "nella norma"

    def __str__(self):
        return f"{self.tipo}: {self.risultato} -> {self.valuta()}"


class Paziente:
    def __init__(self, nome, cognome, codice_fiscale, eta, peso,
                 analisi_effettuate, risultati_analisi):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.eta = eta
        self.peso = peso
        self.analisi_effettuate = analisi_effettuate
        self.risultati_analisi = np.array(risultati_analisi, dtype=float)

    def scheda_personale(self):
        return (
            f"Paziente: {self.nome} {self.cognome}\n"
            f"  Codice fiscale: {self.codice_fiscale}\n"
            f"  Età: {self.eta} anni | Peso: {self.peso} kg\n"
            f"  Analisi effettuate: {', '.join(self.analisi_effettuate)}"
        )

    def statistiche_analisi(self):
        """Statistiche NumPy sui risultati del paziente."""
        return {
            "media": float(np.mean(self.risultati_analisi)),
            "minimo": float(np.min(self.risultati_analisi)),
            "massimo": float(np.max(self.risultati_analisi)),
            "deviazione_standard": float(np.std(self.risultati_analisi)),
        }

    def analisi_valutate(self):
        """Lista di oggetti Analisi (tipo + risultato) del paziente."""
        return [Analisi(t, r) for t, r in
                zip(self.analisi_effettuate, self.risultati_analisi)]


class Medico:
    def __init__(self, nome, cognome, specializzazione):
        self.nome = nome
        self.cognome = cognome
        self.specializzazione = specializzazione

    def visita_paziente(self, paziente):
        print(f"Il dott. {self.nome} {self.cognome} ({self.specializzazione}) "
              f"visita il paziente {paziente.nome} {paziente.cognome}.")


# ---------------------------------------------------------------------------
# PARTE 3 - NumPy: un esame su 10 pazienti
# ---------------------------------------------------------------------------
def esempio_numpy():
    glicemia_10 = np.array([88, 95, 102, 110, 79, 92, 98, 125, 85, 90])
    print("=== PARTE 3 - Glicemia su 10 pazienti ===")
    print(f"Valori:               {glicemia_10}")
    print(f"Media:                {np.mean(glicemia_10):.2f}")
    print(f"Massimo:              {np.max(glicemia_10)}")
    print(f"Minimo:               {np.min(glicemia_10)}")
    print(f"Deviazione standard:  {np.std(glicemia_10):.2f}")
    print()


# ---------------------------------------------------------------------------
# PARTE 5 - Programma principale
# ---------------------------------------------------------------------------
def main():
    esempio_numpy()

    medici = [
        Medico("Anna", "Neri", "Cardiologia"),
        Medico("Paolo", "Gallo", "Endocrinologia"),
        Medico("Elena", "Costa", "Medicina interna"),
    ]

    pazienti = [
        Paziente(nome1, cognome1, cf1, eta1, peso1, analisi1, [7.2, 92, 185]),
        Paziente(nome2, cognome2, cf2, eta2, peso2, analisi2, [105, 160, 6.8]),
        Paziente(nome3, cognome3, cf3, eta3, peso3, analisi3, [230, 118, 1.5]),
        Paziente("Chiara", "Esposito", "SPSCHR95D50A662Z", 29, 55.0,
                 ["glicemia", "emocromo", "trigliceridi"], [82, 5.9, 95]),
        Paziente("Luca", "Romano", "RMNLCU72E10D612W", 52, 92.3,
                 ["colesterolo", "glicemia", "trigliceridi", "creatinina"],
                 [215, 108, 175, 1.1]),
    ]

    print("=== SCHEDE PAZIENTI ===")
    for p in pazienti:
        print(p.scheda_personale())
        print()

    print("=== VISITE ===")
    for i, p in enumerate(pazienti):
        medici[i % len(medici)].visita_paziente(p)
    print()

    print("=== STATISTICHE ANALISI ===")
    for p in pazienti:
        s = p.statistiche_analisi()
        print(f"{p.nome} {p.cognome}")
        print(f"  Media: {s['media']:.2f} | Min: {s['minimo']:.2f} | "
              f"Max: {s['massimo']:.2f} | Dev. std: {s['deviazione_standard']:.2f}")
        for a in p.analisi_valutate():
            print(f"    - {a}")
        print()


if __name__ == "__main__":
    main()