# RGΦ Stage B2 en Google Colab — runbook transaccional

## Estado material

Google Drive vuelve a disponer de almacenamiento suficiente y se ha preparado una superficie persistente de ejecución. Sin embargo, el checkpoint exacto de `t=185` todavía no aparece en Drive ni en la Biblioteca accesible.

La custodia histórica localizada contiene el checkpoint real de profundidad 85, **no** la frontera Stage A de tiempo 185. Esos objetos no son intercambiables.

## Carpeta preparada en Drive

- base: `RGPHI_TAU5_217_CUSTODIA_2026-09-29/RGPHI_STAGE_B2_COLAB_2026-11-11`;
- entrada: `checkpoint_t185/cur`;
- trabajo transaccional: `work`;
- recibos: `receipts`;
- notebook: `notebooks/RGPHI_STAGE_B2_COLAB.ipynb`.

URL base:

`https://drive.google.com/drive/folders/1KBBKkgdpYT0VBbECf5fkJn_bg92kDmFs`

## Entrada canónica requerida

- 128 ficheros `b0000.bin` … `b0127.bin`;
- 2.462.600.671 estados;
- 19.700.805.368 bytes;
- 8 bytes por registro;
- manifiesto SHA-256
  `dbd2f4adda52315e05261b9328c03f8a44d2a31b8e293f3dd3ff7b80b3d2a6b7`.

## Orden vinculante

1. transferir los 128 buckets exactos a `checkpoint_t185/cur/`;
2. abrir el notebook en Colab;
3. montar Drive y fijar el commit `98dcb9650ad559594b71a9c2957859a07f49ace6`;
4. ejecutar inventario rápido;
5. ejecutar auditoría estructural completa;
6. ejecutar smoke y determinismo;
7. ejecutar sólo el piloto `185→186`;
8. revisar coste, espacio y manifest de `level_186`;
9. reanudar a `211` únicamente tras aceptar el piloto.

## Persistencia y claims

El `work-root` reside en Drive. Un nivel incompleto termina en `.tmp`; un nivel aceptado queda en `level_XXX/` y se reutiliza en la siguiente sesión.

- `HIT` entre 186 y 211: nuevo upper bound exacto;
- `NO_HIT_THROUGH_211`: permite concluir `tau5=212`;
- piloto o interrupción: no cambia el canon.

No se autoriza reconstrucción, sustitución sintética ni uso del checkpoint histórico de profundidad 85.
