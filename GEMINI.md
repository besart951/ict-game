# GEMINI.md - Pixel Hero with Pro Assets

## Project Overview
"Pixel Hero" has been upgraded to use the full **Kenney Pixel Platformer** asset pack. It now features high-quality character animations, tile-based environments, and professional sound effects.

### Features
- **Pro Graphics:** Character animations (Idle, Walk, Jump), Grass Tiles, Backgrounds, and level decorations (Clouds, Grass tufts).
- **Pro Sounds:** Uses `.ogg` sound effects for jumping, winning, and UI selection.
- **Parallax Background:** Multi-layered scrolling for depth.
- **Improved Game Design:** Better level layout and visual variety.
- **SOLID Clean Code:** Maintained the refactored architecture while integrating assets.

### Key Asset Paths
- **Characters:** `src/assets/Sprites/Characters/Default/`
- **Tiles:** `src/assets/Sprites/Tiles/Default/`
- **Sounds:** `src/assets/Sounds/`
- **Backgrounds:** `src/assets/Sprites/Backgrounds/Default/`

### How to Run
```bash
python run.py
```

### Learning Goals for Students
- **Asset Integration:** How to load and display images and sounds.
- **Animation Systems:** Using timers to switch between sprite frames.
- **Parallax Effect:** Simple math to create a 3D feeling in 2D.
- **Resource Management:** Centralized asset loading in `assets.py`.
