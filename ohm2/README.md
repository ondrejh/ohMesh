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

- [Heltec V3 (Aliexpress)](https://www.aliexpress.com/item/1005007383620718.html?spm=a2g0o.order_list.order_list_main.171.3e601802HxDH7p)
- [LiPo článek (Aliexpress)](https://www.aliexpress.com/item/1005007850868686.html?spm=a2g0o.order_list.order_list_main.111.3e601802HxDH7p)

### Volitelně

- [GPS modul (Aliexpress)](https://www.aliexpress.com/item/32832919409.html?spm=a2g0o.order_list.order_list_main.151.3e601802HxDH7p)
- [Vypínač (Aliexpress)](https://www.aliexpress.com/item/10000003088863.html?spm=a2g0o.order_list.order_list_main.136.1b5a1802tNyZ4L)

Modul Heltec V3 je třeba vybrat správnou frekvenci 868MHz a také variantu bez krabičky a s anténou a pigtailem.

# Galerie stavby

![Materiál](../www/img/010_parts_needed.jpg)
![Příprava vodičů na připojení GPS modulu](../www/img/020_solder_wires_to_heltec_v3.jpg)
![Montáž vypínače](../www/img/030_mount_switch.jpg)
![Montáž antény](../www/img/040_mount_antena_pigtail.jpg)
![Umístění desky Heltec V3](../www/img/050_insert_heltec_v3.jpg)
![Umístění antény GPS](../www/img/060_insert_gps_antena.jpg)
![Rozmístění vodičů zespodu desky](../www/img/070_bottom_wire_harness.jpg)
![Podlepení GPS modulu kaptonovou páskou](../www/img/080_capton_tape.jpg)
![Vložení GPS modulu a zakrácení vodičů](../www/img/090_insert_gps_trim_wires.jpg)
![Připájení GPS modulu](../www/img/100_solder_wires_to_gps.jpg)
![Připojení antény LoRa](../www/img/110_connect_lora_antena.jpg)
![Připojení GPS antény](../www/img/120_connect_gps_antena.jpg)
![Příprava předního krytu](../www/img/130_prepare_front_cover.jpg)
![Vložení předního krytu](../www/img/140_insert_front_cover.jpg)
![Příprava baterie](../www/img/150_prepare_battery.jpg)
![Připájení baterie](../www/img/160_solder_battery_to_switch.jpg)
![Hotová stanice](../www/img/170_meshtastic_build.jpg)
![Hotová stanice](../www/img/171_meshtastic_build.jpg)
![Hotová stanice](../www/img/172_meshtastic_build.jpg)
![Hotová stanice](../www/img/173_meshtastic_build.jpg)
![Hotová stanice](../www/img/174_meshtastic_build.jpg)
