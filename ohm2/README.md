# Mobilní stanice ohM2

Mobilní stanice, nebo vysílačka, pro síť Meshtastic. Jejím základem je modul Heltec V3, který je vybaven kontrolérem ESP32, LoRa čipem, nabíjecím obvodem LiPo článku a oled displejem. Modul umí komunikovat přes LoRa, Bluetooth a WiFi.

Elektronika vysílačky je v 3D tištěném pouzdře. Jeho základem je model z Printables. Pro svoje účely jsem na něm udělal drobné úpravy, jiná záda, snížení příliš vystupujícího okénka a zadělání výřezu pro plexi. Autor modelu má bohužel nastaveno nesdílet a nemodifikovat, takže si úpravy nechám pro sebe. Nové díly ale k dispozici dám.
- [ ] doplnit originální model
- [ ] doplnit moje díly

![ohm2 v doku](../www/img/ohm2_v_doku.jpg)

Pro lepší komfort užívání jsem si k vysílačce dodělal nabíjecí dok. Vždy když přijdu z výletu, hodím vysílačku zpět do doku a na příště mám zase nabito. Celou dobu jsem navíc ve spojení. V domě sice moc dobrý signál není, ale spojení mi zajišťuje pevná stanice ohM1 na střeše, za cenu jednoho hopu navíc.
- [ ] doplnit model doku

Kromě základní funkce Meshtastic nodu je zapojení doplněné o GPS čip. To je kvůli možnosti reportovat polohu. Na displeji se pak také ukazuje vzdálenost od ostatních nodů, které mají polohu také zapnutou.

V pouzdře je také docela velký LiPo článek 2000mAh, aby, i přes žravost Heltecu, vydržela vysílačka nějaký čas bez nabíjení.

## Elektronika

- modul Heltec V3
- LiPo článek

### Volitelně

- GPS modul
- [vypínač](https://www.aliexpress.com/item/10000003088863.html?spm=a2g0o.order_list.order_list_main.136.1b5a1802tNyZ4L)
