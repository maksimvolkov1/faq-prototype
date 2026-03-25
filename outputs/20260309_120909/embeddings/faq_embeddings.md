# FAQ (automatisch generiert)

## Teams friert beim Start ein?

**Topic/Label:** Stabilität: friert / teams / beim

**Antwort:**
**Kurzlösung:** Stelle außerdem sicher, dass Teams aktualisiert ist.

**Schritte:**
1. Teams komplett beenden (Task-Manager) und den Cache löschen (Teams Cache/Local Storage).
2. Wenn es wieder passiert, prüfe Updates von Teams und Windows.
3. Alternativ kannst du testweise die Web-Version nutzen.
4. Schließe unnötige Programme und prüfe, ob du über WLAN mit schwachem Signal verbunden bist.
5. Teste wenn möglich LAN oder einen anderen Access Point.
6. Stelle außerdem sicher, dass Teams aktualisiert ist.

**Benötigte Angaben:**
- Sende dem IT-Support bitte deine Teams-Version, falls es bleibt.

**Hinweise:**
- Danach Teams neu starten.

**Belege (Tickets):** TCK-0303, TCK-0308, TCK-0311

---

## Office Aktivierung Fehlercode (0xC004F074)?

**Topic/Label:** Lizenz: aktivierung / office / aktiviert

**Antwort:**
**Kurzlösung:** Prüfe Datum/Uhrzeit und Netzwerkverbindung (im Firmennetz oder VPN).

**Ursache/Erklärung:**
- Das ist oft ein Aktivierungs-/KMS-Kommunikationsproblem.
- Das passiert meist, wenn ein falsches Konto verwendet wird (privat statt Firmenkonto) oder keine Lizenz zugewiesen ist.
- Das deutet auf ein Token-/Cache-Problem hin.

**Schritte:**
1. Prüfe Datum/Uhrzeit und Netzwerkverbindung (im Firmennetz oder VPN).
2. Melde dich komplett ab und nur mit dem Firmenkonto wieder an.

**Benötigte Angaben:**
- Wenn es bleibt, sende dem IT-Support den Screenshot; ich prüfe, ob KMS/Token oder die installierte Office-Edition nicht zur Lizenz passt.

**Hinweise:**
- Starte den PC neu und versuche es erneut.

**Support:**
- Der IT-Support prüft parallel, ob dir die passende Lizenz zugeordnet ist und weise sie ggf. zu.

**Belege (Tickets):** TCK-0412, TCK-0403, TCK-0607

---

## PC sehr langsam nach Windows-Update?

**Topic/Label:** Performance: nach / update / windows

**Antwort:**
**Kurzlösung:** Starte danach neu.

**Schritte:**
1. Nach Updates laufen oft Hintergrundprozesse (Indexierung/Defender/Optimierung).
2. Starte danach neu.
3. Prüfe im Task-Manager, ob „Windows Modules Installer“/„Antimalware Service Executable“ viel Last verursacht.
4. Wenn es morgen noch so ist, schicken mir bitte Screenshot vom Task-Manager (CPU/RAM/Datenträger).
5. Windows.old entsteht nach größeren Updates und kann nach erfolgreichem Betrieb entfernt werden.
6. Nutze „Datenträgerbereinigung“ bzw. „Speicher“ -> „Temporäre Dateien“ und wähle „Vorherige Windows-Installation(en)“.

**Hinweise:**
- Lass den PC 30–60 Minuten am Strom und im WLAN/LAN, damit alles fertig wird.
- Danach neu starten.

**Belege (Tickets):** TCK-0301, TCK-0606, TCK-0313

---

## Passwort-Reset Link kommt nicht an?

**Topic/Label:** Account: passwort / reset / bekomme

**Antwort:**
**Kurzlösung:** Prüfe Spam/Quarantäne und ob du die richtige Firmen-E-Mail-Adresse verwendet hast.

**Schritte:**
1. Prüfe Spam/Quarantäne und ob du die richtige Firmen-E-Mail-Adresse verwendet hast.
2. Wenn du ein privates Postfach eingetragen hast, funktioniert es nicht.
3. Teile mir bitte den Zeitpunkt des Versuchs mit.
4. Das Passwort muss die Mindestlänge erfüllen und eine Mischung aus Groß-/Kleinbuchstaben, Zahl und Sonderzeichen enthalten.
5. Vermeide Namen/leicht erratbare Wörter und nutze besser eine Passphrase (z.B. 4 Wörter + Zahl + Sonderzeichen).
6. Wenn du mir sagst, welche Fehlermeldung genau kommt, kann ich prüfen, ob zusätzliche Regeln greifen.
7. Nutze auf der Login-Seite die Funktion „Passwort vergessen“.

**Support:**
- Der IT-Support kann den Reset-Link erneut auslösen und das Postfach-Logging prüfen.

**Belege (Tickets):** TCK-0102, TCK-0114, TCK-0101

---

## WLAN verbindet mit Gastnetz statt Firmennetz?

**Topic/Label:** Netzwerk: wlan / verbindet / trennt

**Antwort:**
**Kurzlösung:** Entferne das Gast-WLAN-Profil („Bekannte Netzwerke verwalten“ -> Entfernen) oder setze die Priorität so, dass das Firmennetz bevorzugt wird.

**Schritte:**
1. Entferne das Gast-WLAN-Profil („Bekannte Netzwerke verwalten“ -> Entfernen) oder setze die Priorität so, dass das Firmennetz bevorzugt wird.
2. Verbinde dich anschließend manuell mit dem Firmennetz und speichere die Zugangsdaten.
3. Wenn ihr 802.1X nutzt, kann auch ein Zertifikat fehlen – dann richte ich das Profil neu ein.
4. Entferne das WLAN-Profil komplett und verbinde neu.
5. Prüfe, ob du das richtige Netz (z.B. Mitarbeiter vs. Gast) nutzt.
6. Wenn ihr 802.1X verwendet, kann ein Zertifikat/Passwort-Problem vorliegen.
7. Entferne das WLAN-Profil („Bekannte Netzwerke verwalten“ -> Entfernen) und verbinde dich neu.

**Benötigte Angaben:**
- Sende dem IT-Support bitte die genaue Meldung in Windows und ob es an anderen Geräten klappt.

**Belege (Tickets):** TCK-0610, TCK-0513, TCK-0501

---

## Falsches Papierformat (A4/A3)?

**Topic/Label:** Drucker: drucker / drucke / immer

**Antwort:**
**Kurzlösung:** Deaktiviere in Windows „Windows verwaltet Standarddrucker“ (Einstellungen -> Geräte -> Drucker & Scanner).

**Ursache/Erklärung:**
- Oft ist in der Vorlage A3 gespeichert.

**Schritte:**
1. Prüfe im Druckdialog das Papierformat (A4) und im Druckertreiber die „Standardpapiergröße“.
2. Stelle außerdem sicher, dass im Druckerfach tatsächlich A4 eingelegt ist und das Fach korrekt eingestellt ist.
3. Wenn du willst, schick mir einen Screenshot der Druckeinstellungen.
4. Deaktiviere in Windows „Windows verwaltet Standarddrucker“ (Einstellungen -> Geräte -> Drucker & Scanner).
5. Setze anschließend den gewünschten Drucker als Standard.
6. Wenn du oft mit dem Laptop dockst, kann es sonst automatisch umschalten.
7. Prüfe, ob du den richtigen Drucker ausgewählt hast und ob es ggf. mehrere ähnlich benannte Geräte gibt.

**Belege (Tickets):** TCK-0208, TCK-0207, TCK-0209

---

## Lizenz für neues Tool anfragen (Jira)?

**Topic/Label:** Lizenz: lizenz / pro / keinen

**Antwort:**
**Kurzlösung:** Nach der Zuweisung bitte einmal ab- und wieder anmelden, damit die Berechtigung aktiv wird.

**Schritte:**
1. Nach der Zuweisung bitte einmal ab- und wieder anmelden, damit die Berechtigung aktiv wird.

**Benötigte Angaben:**
- Sende dem IT-Support: Projektname, benötigte Rolle (z.B. User/Admin), Begründung und idealerweise eine kurze Freigabe durch Projektleitung.
- Sende dem IT-Support kurz Zweck/Projekt, benötigte Dauer (temporär/ dauerhaft) und eine Freigabe durch Teamleitung/Kostenstelle.
- Nenne Space/Projekt und die verantwortliche Person.

**Hinweise:**
- Danach kann ich die Lizenz zuweisen bzw. den Antrag im Lizenzsystem stellen.
- Du erhältst eine Bestätigung, sobald die Zuweisung aktiv ist.
- Danach kann ich die Pro-Lizenz zuweisen.

**Support:**
- Der IT-Support kann dir eine Confluence-Lizenz zuweisen, sobald die Projektverantwortlichen bestätigt haben, dass du Zugriff benötigst.

**Belege (Tickets):** TCK-0409, TCK-0608, TCK-0410

---

## WLAN verbunden, aber kein Internet?

**Topic/Label:** Netzwerk: lan / laden / kein

**Antwort:**
**Kurzlösung:** Trenne die WLAN-Verbindung und verbinde dich neu.

**Schritte:**
1. Trenne die WLAN-Verbindung und verbinde dich neu.
2. Prüfe, ob eine Proxy-Einstellung aktiv ist.
3. Prüfe, ob das LAN-Kabel richtig eingerastet ist und ob am Port/Adapter LEDs leuchten.
4. Teste wenn möglich ein anderes Kabel oder einen anderen Netzwerkport.
5. Trenne Dockingstation komplett (Strom + USB-C), warte 10 Sekunden und schließe alles neu an.

**Benötigte Angaben:**
- Wenn es weiter besteht, sende dem IT-Support einen Screenshot der WLAN-Details (IP-Adresse/Gateway).

**Hinweise:**
- Danach: `ipconfig /release` und `ipconfig /renew` (falls erlaubt) bzw. Netzwerkproblembehandlung starten.

**Support:**
- Der IT-Support kann den Switch-Port prüfen (VLAN/Port deaktiviert) – dafür brauche ich Raum/Portnummer (falls am Anschluss steht) und deine MAC-Adresse.

**Belege (Tickets):** TCK-0503, TCK-0504, TCK-0505

---

## Hohe CPU: Prozess 'Antimalware Service Executable'?

**Topic/Label:** Performance: cpu / voll / task

**Antwort:**
**Kurzlösung:** Prüfe, ob gerade ein großes Laufwerk/Ordner neu synchronisiert wird.

**Ursache/Erklärung:**
- Das ist Windows Defender beim Scannen.
- Das deutet meist auf eine laufende Synchronisation oder einen Sync-Fehler hin.

**Schritte:**
1. Lasse den Scan einmal fertig laufen (am besten am Strom).
2. Prüfe, ob gerade ein großes Laufwerk/Ordner neu synchronisiert wird.
3. Wenn es dauerhaft hoch bleibt, kann ich eine gezielte Ausschlussprüfung für bekannte Unternehmensordner prüfen (nach Policy) oder einen vollständigen Malware-Scan anstoßen.
4. Prüfe das OneDrive-Symbol (Sync-Status) und pausiere testweise die Synchronisation für 10 Minuten.
5. Wenn es hilft, prüfen wir, ob sehr große Dateien/Ordner oder viele kleine Dateien gesynct werden.

**Hinweise:**
- Ein Neustart von OneDrive (Beenden/Starten) behebt es oft ebenfalls.

**Belege (Tickets):** TCK-0305, TCK-0605, TCK-0306

---

## Scanner sendet nicht an E-Mail?

**Topic/Label:** Scannen: mail / scan to / to mail

**Antwort:**
**Kurzlösung:** Prüfe, ob du die richtige Empfängeradresse auswählst und ob die Mail im Spam landet.

**Ursache/Erklärung:**
- Häufig liegt es an SMTP/Authentifizierung.
- Häufig sind Absenderkonto/SMTP-Auth oder eine blockierte Empfängeradresse der Grund.

**Schritte:**
1. Prüfe, ob du die richtige Empfängeradresse auswählst und ob die Mail im Spam landet.
2. Leite mir die Bounce-Mail (Fehlertext) weiter, damit wir Ursache/SMTP-Fehlercode sehen.

**Benötigte Angaben:**
- Nenne dem IT-Support bitte Gerätename/Standort und ungefähre Uhrzeit des Scanversuchs.
- Nenne dem IT-Support bitte Gerätename/Standort und Uhrzeit des Scans.

**Support:**
- Der IT-Support prüft die Scan-to-Mail Konfiguration am Gerät (Relay/Account) und die Server-Logs.
- Der IT-Support prüft die Gerätekonfiguration (SMTP-Relay, Account, TLS) und passe sie an.

**Belege (Tickets):** TCK-0205, TCK-0604, TCK-0212

---

## Konto gesperrt nach VPN-Login?

**Topic/Label:** Account: gesperrt / login / nach

**Antwort:**
**Kurzlösung:** Lösche im VPN-Client gespeicherte Zugangsdaten und melde dich neu mit dem aktuellen Passwort an.

**Ursache/Erklärung:**
- Wahrscheinlich nutzt der VPN-Client noch ein altes gespeichertes Passwort.
- Das passiert häufig durch ein Gerät mit altem gespeicherten Passwort (z.B. Smartphone-Mail, Outlook, VPN).

**Schritte:**
1. Das Konto wurde entsperrt.
2. Lösche im VPN-Client gespeicherte Zugangsdaten und melde dich neu mit dem aktuellen Passwort an.
3. Wenn du weitere Geräte nutzt (Handy/Outlook), aktualisiere dort ebenfalls die Anmeldedaten, um erneute Sperren zu vermeiden.
4. Ändere das Passwort einmal und aktualisiere es anschließend auf allen Geräten.

**Support:**
- Der IT-Support prüft parallel die Sperr-Quelle in den Logs und gebe dir Bescheid, welches Gerät die Fehlversuche verursacht.

**Belege (Tickets):** TCK-0115, TCK-0104, TCK-0103

---

## Drucker druckt sehr blass / kaum lesbar?

**Topic/Label:** Drucker: druck / druckt / drucker

**Antwort:**
**Kurzlösung:** Stelle im Treiber testweise auf PCL6/Universal-Treiber um (falls vorhanden).

**Schritte:**
1. Prüfe den Tonerstand am Gerät und rüttle die Tonerkassette einmal vorsichtig (falls vom Hersteller vorgesehen).
2. Starte anschließend eine Kalibrierung/Reinigung (Menü -> Wartung).
3. Drucke eine interne Testseite.
4. Wenn die Testseite ebenfalls blass ist, tauschen wir Toner/Drum bzw. melden Service.
5. Teste einmal eine kleine Testseite.
6. Wenn nur PDFs langsam sind, kann es an „Als Bild drucken“ oder am Treibermodus liegen.
7. Stelle im Treiber testweise auf PCL6/Universal-Treiber um (falls vorhanden).

**Support:**
- Der IT-Support kann außerdem die Queue auf große Jobs prüfen, die alles blockieren.

**Belege (Tickets):** TCK-0603, TCK-0213, TCK-0201

---

