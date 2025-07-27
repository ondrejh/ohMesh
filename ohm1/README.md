# ohM1

Statická stanice na bázi Heltec V3. Navíc má snímač prostředí BME280 a napájecí obvod aby mohla být připojená na 12V.

![ohM1 na střeše](www/img/ohm1_na_strese.jpg)

Zařízení je v provozu od prosince 2024. Mělo to být dočasné řešení, něco jako pokus, ale zatím jsem s tím spokojený.

# Update a servis po půl roce

Po více jak půl roce provozu jsem se rozhodl updatovat FW. Aktuální verze (červenec 2025) je 2.6.11 a na stanici byl FW 2.5.. Shodou okolností se po vydatné bouřce přestal hlási senzor, takže dolů se menší servis hodí.

Prvním problémem bylo sundání stanice ze střechy. Malinkaté závitové vložky M3 to v kombinaci s rezivými příliš dlouhými šrouby nedaly a až na jednu se protočily. Jiné nářadí než imbus jsem na střeše neměl (typicky), takže jsem držák odpáčil.

![ohM1 prasklý držák, protočené vložky](ohm1/oprava/ohm1_praskly_drzak.jpg)

Do budoucna by to chtělo něco s pantem na jeden šroub, nejlépe křídlovku. Taky materiál by to chtělo jiný. PETG na sluníčku přece jen dost křehne. No, příště. Teď jsem jen vytisknul novou sponu držáku.

![ohM1 nová spona držáku](ohm1/oprava/ohm1_novy_drzak.jpg)

Závitové vložky jsem vytavil ven a nahradil většími M4, které tam snad budou lépe držet.

![ohM1 nové vložky](ohm1/oprava/ohm1_nove_vlozky.jpg)

Také jsem chtěl dát kratší šrouby, aby tolik netrčely a nerezivěly. V dané délce měli "jen" nerez - no paráda, to by mohlo být řešení.

Uvnitř krabice bylo čisto a sucho, až na spodní napájecí konektor. Nenapadlo mě, že bude vlhkost procházet konektorem. Na druhou stranu není vodotěsný - dal jsem tam co jsem měl. Konektor jsem tedy očistil, zadělal silikonem a při montáži zpět na střechu jsem protikus, který také vykazoval známky koroze, prostříknul kontaktním konzervačním sprejem.

## Oprava snímače

Deska snímače prostředí BME280 je, pochopitelně vystavená vlivům prostředí. Nechtěl jsem řešit co přesně se stalo, tak jsem ji rovnou nahradil novou. Tu jsem tentokrát přelakoval základovkou na plasty. U toho se nesmí zapomenou zalepit něčím samotný snímač, aby jej nezalepil lak. Na to jsem použil kousek kaptonové, kterou jsem po zaschnutí laku odstranil.

Krátce po zapnutí stanice se snímač přihlásil a měří .. opraveno.

Starý snímač byl trochu zašlý (snad oxidace pájky) kolem těch pár součástek. Opláchnul jsem ho isopropanolem a nechal uschnout. A funguje taky. Nevím co s tím mohlo být. Nějaký svod na I2C by to asi nezastavil.

## Update FW

Update FW popisuju [u nodu ohm2](https://github.com/ondrejh/ohMesh/tree/master/ohm2#aktualizace-fw). V tomto případě jsem nezpanikařil a po prvním neúspěchu jsem nedal full erase. A jelo to na druhou dobrou. Nebylo nutné obnovovat zálohu klíčů ani nic podobného.

## Hotovo

![ohM1 po servisu](ohm1/oprava/ohm1_hotovo.jpg)

Stanice má aktuální FW, je zkontrolovaná, zatěsněná a snímač prostředí je snad lépe zabezpečený... tak uvidíme.

# ToDo

- [ ] popsat nastavení statického nodu
- [ ] schema připojení snímače
