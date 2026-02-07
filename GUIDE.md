# 🎮 Pixel Hero - Programmier-Guide für Kids

Willkommen zum Pixel Hero Code! Wir haben den Code so umgebaut, dass du ihn super einfach verstehen und erweitern kannst. 

## 📂 Wo finde ich was?

- **`src/sprites.py`**: Hier wohnen alle "Lebewesen" und Objekte im Spiel (Spieler, Gegner, Plattformen).
- **`src/settings.py`**: Hier kannst du das Spiel tunen (Geschwindigkeit, Schwerkraft, Farben).
- **`src/states/play_state.py`**: Hier wird das Level gebaut. Hier kannst du neue Plattformen platzieren!

---

## 🚀 Aufgaben für dich

### 1. Ein neues Level bauen
Öffne `src/states/play_state.py` und suche nach der Methode `_setup_level`.
Dort findest du Listen für `level_platforms` und `level_enemies`.

**Versuch mal:**
- Füge eine neue Plattform hinzu: `(x, y, breite, höhe)`
- Setze einen neuen Gegner: `(x, y, laufweite)`

### 2. Den Spieler schneller machen
Gehe in die `src/settings.py` und ändere den Wert von `PLAYER_SPEED` oder `PLAYER_JUMP_FORCE`.
Aber Vorsicht: Wenn du zu hoch springst, fliegst du aus dem Bild!

### 3. Einen neuen Gegner-Typ erfinden
In `src/sprites.py` kannst du die Klasse `Enemy` kopieren und eine neue Klasse `FastEnemy` erstellen.
Ändere dort einfach die `self.speed`.

---

## 🛠️ Wie man das Spiel startet
Gib einfach diesen Befehl in dein Terminal ein:
```bash
python run.py
```

Viel Spaß beim Coden! 🕹️✨
