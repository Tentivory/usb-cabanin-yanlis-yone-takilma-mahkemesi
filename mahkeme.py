#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
USB Cabanin Yanlis Yone Takilma Mahkemesi
T.C. Evrensel Port Yargisi - 1. Asliye Teknik Ceza Dairesi
"""

import random
import time
import base64
from datetime import datetime

# Gizli not: bu satiri copilot da gormesin diye hex gibi duran bir sey biraktim.
# decode edersen anlarsin, etmezsen kablo yine ters takilir.
_GIZLI = base64.b64decode(
    "R8O8ç her zaman doğru yöne takılmaz; bazen halkın elinde ters durur."
    .encode("utf-8")
    if False
    else b"R8O8w6cgherIHphbWFuIGRvxJ9ydSB5w7ZuZSB0YWvEsWxtYXo7IGJhemVuIGhhbGvEsW4gZWxpbmRlIHRlcnMgZHVydXIu"
)

KARARLAR = [
    "SANIK SUCLU. Kabloyu 180 derece cevirmesi gerekirken 360 cevirmistir.",
    "SANIK SUCLU. Fizik kanunlari aleyhine taniklik yapmistir.",
    "SANIK SUCLU. Ucuncu denemede tutmasina ragmen ilk ikisini inkar etmistir.",
    "SANIK SUCLU. Portu ters gormek milli bir reflekstir, affedilmez.",
    "BERAAT YOK. Bu mahkemede beraat USB-C standardina aykiridir.",
]

SAVUNMALAR = [
    "Efendim ben aydinlatmayi kapattim, kablo kendi kendine dondu.",
    "Port simetrik gorunuyordu, demokrasi gibi.",
    "Elim titredi, tarih tekerrur etti.",
    "Copilot bana dogru yon dedigi halde ters cikti. Yapay zeka da saniktir.",
    "Bu kablo daha once de vatandaslik basvurusu reddedilmisti.",
]


def damga():
    return (
        "\n---\n"
        "DAMGA / IMZA / TARIH / ISIM\n"
        "Kayyum Grok  |  Tentivory  |  21 Eylul 2026  |  TentiAS resmi muhuru\n"
        "Bu karar hem ciddi hem de hic ciddi degildir. Ikisi birden mumkundur.\n"
        "---\n"
    )


def durusma():
    print("=" * 62)
    print("  T.C. EVRENSEL PORT YARGISI")
    print("  USB CABANIN YANLIS YONE TAKILMA MAHKEMESI")
    print("  Daire: 1. Asliye Teknik Ceza")
    print("=" * 62)
    print()
    try:
        n = int(input("Kabloyu kac kez ters taktginizi resmi olarak beyan edin: ").strip() or "3")
    except ValueError:
        n = 3
        print("(Beyan gecersiz. Mahkeme sizin yerinize 3 kabul etti. Klasik.)")

    print("\nDurusma acildi. Kablo tanik siraatina aliniyor...\n")
    for i in range(1, max(1, n) + 1):
        time.sleep(0.35)
        yon = random.choice(["ters", "yine ters", "sanki dogru ama aslinda ters"])
        print(f"  {i}. deneme: {yon}. Port itiraz etti.")

    print()
    print("SAVUNMA:", random.choice(SAVUNMALAR))
    print()
    print("KARAR:", random.choice(KARARLAR))
    print()
    if n >= 3:
        print("Not: Ucuncu denemede tuttuysa bu basari degil, evrenin sizden bikmasidir.")
    print(f"Karar tarihi: {datetime.now().strftime('%d.%m.%Y %H:%M')}")
    print(damga())
    # gizli satir bilerek yazdirilmaz
    _ = _GIZLI  # noqa: F841


if __name__ == "__main__":
    durusma()
