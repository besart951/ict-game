# Mein super Spiel (Pygame)

Dieses Projekt ist ein einfaches 2D-Spiel-Grundgerüst mit **Python + Pygame**,
extra für Einsteiger:innen ab ca. 13 Jahren.

## Projektstruktur

```plaintext
mein_super_spiel/
│
├── assets/                 # Hier kommen später Bilder und Sounds rein
│   ├── images/
│   └── sounds/
│
├── src/                    # Der Quellcode (Source)
│   ├── __init__.py         # Macht den Ordner als Modul erkennbar
│   ├── main.py             # Startet das Spiel (Game Loop)
│   ├── sprites.py          # Enthält die Klassen (Player, Enemy)
│   └── settings.py         # Farben, Fenstergröße, Speed
│
└── README.md               # Eine kurze Anleitung für die Kids
```

## Starten mit `uv`

1. Abhängigkeiten installieren:
   ```bash
   uv add pygame
   ```

2. Spiel starten:
   ```bash
   uv run python -m src.main
   ```

## Steuerung

- Pfeiltasten: Spieler bewegen

Viel Spaß beim Weiterbauen! 🎮
