# Desafio

Sala de Desafíos de Apexora (`index.html`). Un reto nuevo por juego cada día, igual para todos.

## Variedad: cómo se eligen los retos
Cada juego recorre todo su banco en un orden mezclado y no repite nada hasta pasado un tercio del banco
(`rotPick` en `index.html`). Conexiones, Impostor y el tablero del tic tac toe se arman cada día combinando
categorías del lore, así que casi nunca salen dos días iguales.

## Dónde agregar contenido
Todo el contenido nuevo sale del lore y va en **`lore-data.js`**:
- `LORE.cats` → categorías de Conexiones e Impostor (cada una: id, título, «esto es…», familia, miembros, incompatibles).
- `LORE.imp` → preguntas sueltas del Impostor.
- `LORE.words` → palabras del Wordle (solo A–Z, 4 a 8 letras).
- `LORE.lists` → listas del Top 10.
- `LORE.tt` → personajes y condiciones del Apexora tic tac toe.
- `LORE.trivia`, `LORE.vof`, `LORE.quien`, `LORE.crono` → retos extra de esos juegos.

Trivia, V o F, ¿Quién soy?, Cronología y las imágenes siguen en `index.html` / `imagenes/imagenes.json`.

## Perfil y sinfalitas
- El perfil y el login viven en el **Portal**; esta página solo comprueba la cuenta (si no hay sesión, manda al Portal). No hay avatares, barra superior, rachas ni XP/niveles/cofres.
- Cada juego da sinfalitas al terminar, **una vez al día y nunca más de 20** (`SINF_MAX`). Los máximos por juego están en la tabla `SINF` de `index.html`; el factor por pistas/fallos en `RW`. Se entregan con `window.APX.premiar(n, 0)`.
- El botón «Volver al Portal» está arriba a la izquierda; el HUD del Portal se ubica con `--apx-hud-top` / `--apx-hud-bottom` en `apexora-theme.css`.
- Tic tac toe: cada casilla (fila × columna) tiene siempre al menos 2 respuestas posibles (`TT_MINANS`); el generador nunca devuelve un tablero sin verificar.
