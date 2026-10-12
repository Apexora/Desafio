# Ejecutar dentro de la carpeta imagenes/ :  python verificar_imagenes.py
import json, os
ok = {e["file"] for e in json.load(open("imagenes.json", encoding="utf-8"))}
reales = {f for f in os.listdir(".") if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".gif"))}
print("En el JSON pero NO en la carpeta (corregir el nombre):", sorted(ok - reales) or "ninguna")
print("En la carpeta pero NO en el JSON (agregar):", sorted(reales - ok) or "ninguna")
