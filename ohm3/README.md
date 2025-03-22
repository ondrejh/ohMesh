# Stanice s Raspberry PI pico ohM3

Dalším mým pokusem s Meshtastikem je stanice postavená na základě Raspberry PI Pico s kontrolérem RP2040. LoRa konektivitu zde zajišťuje modul SX1262. Stanice je zatím postavená na nepájivé desce, breadboardu, takže jsem jí dal pracovní název BreadTastic Pico (ne, není to Ostravsky, bez diakritiky).

- [ ] doplnit schéma zapojení SX1262
- [ ] doplnit schéma zapojení BME280
- [ ] přidat displej

![ohm3 s čidlem BME280](../www/img/ohm3_bme280.jpg)

## Připojení čidla BME280

K původnímu zapojení jsem se nejdřív pokoušel hledat správné piny pro připojení snímačů prostředí. Zdá se, že v oficiálním FW pro Meshtastic na Raspberry PI Pico není I2C pro telemetrii podporováno. Nebo prostě nevím jak. Rozhodl jsem se tedy přistoupit úpravě FW.

Připojil jsem snímač na piny 6 a 7, kam je možné namapovat I2C1. Tyto piny jsem exlicitně uvedl ve variantě pro překlad a firmware si zkompiloval sám. Postup kompilace je uvedený na webu [meshtastic.org](https://meshtastic.org/docs/development/firmware/build/), takže uvedu jen body.

### Úprava FW aby podporoval moduly I2C

- instalace Visual Studio Code s doplňkem PlatformIO
- stažení githubového repozitáře s fimwarem
- výběr cílového zařízení rpipico
- úprava souboru variant.h, přidání I2C pinů
- kompilace a upload

#### Úprava souboru variant.h

Za poznámku o defaultních I2C pinech (4/5) jsem přidal definici pinů I2C_SDA, I2C_SCL, I2C_SDA1 a I2C_SCL1. Asi by stačilo přidat jen ty s jedničkou, ale teď mám alespoň jistotu, až budu chtít třeba přidat displej.

```code
// default I2C pins:
// SDA = 4
// SCL = 5

// Redefine I2C0 pins to avoid collision with UART1/Serial2.
#define I2C_SDA 4
#define I2C_SCL 5

// Redefine Waveshare UPS-A/B I2C_1 pins:
#define I2C_SDA1 6
#define I2C_SCL1 7

// Recommended pins for SerialModule:
// txd = 8
// rxd = 9
```

#### Upload firmwaru

Projek ve Visual Studiu předpokládá nahrávání FW pomocí debugovacího rozhraní, které ale nemám - ještě jsem ho nepotřeboval. Naštěstí se při překladu vytvoří i soubor firmware.u2f, který se nahrává do zařízení jako na flash disk. Tak jak je to ve všech návodech pro začátečníky.

### Zapnutí Telemetrie

Snímače na I2C nezačnou samy od sebe pracovat, je třeba je zapnout tzv. Modul Telemetrie. Ve webovém rozhraní [Meshtastic Web](https://client.meshtastic.org/) se mi to bohužel nedařilo, takže uvedu postup pro Meshtastick Python CLI.

```code
python3 -m meshtastic --set telemetry.environment_measurement_enabled true
```

Někdy je třeba uvést port, protože Python CLI nemůže stanici najít, ale tentokrát to vyšlo.

Takhle to pak vypadá, když takovou stanici vidí jiná stanice (tentokrát šlo o mou vysílačku ohM2).

![ohm3 hodnoty z čidla BME280](../www/img/ohm3_environment_values_bme280.jpg)

Pokračování příště.
