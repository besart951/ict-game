# Mein Super OOP Spiel

Ein einfaches Spiel in Python, programmiert mit Objekt-Orientierter Programmierung (OOP).
Ideal für Einsteiger! 🎮

## Projekt-Struktur

```plaintext
mein_spiel/
│
├── run.py              # <--- Hier starten! (python run.py)
├── README.md           # Anleitung
├── pyproject.toml      # Einstellungen für Python/uv
│
└── src/                # Der Quellcode
    ├── game.py         # Die Haupt-Klasse 'Game' (Spiel-Logik)
    ├── main.py         # Start-Funktion
    ├── settings.py     # Einstellungen (Farben, Größe)
    └── sprites.py      # Spieler und Gegner (Klassen)
```

## Installation

Falls du `uv` benutzt:
```bash
uv sync
```

Oder klassisch mit pip:
```bash
pip install pygame
```

## Starten

Ganz einfach im Terminal:

```bash
python run.py
```

Oder mit uv:

```bash
uv run python run.py
```

## Steuerung
- **Pfeiltasten Links/Rechts**: Bewegen
- **Ziel**: Weiche den roten Blöcken aus!

Viel Spaß beim Coden! 🚀