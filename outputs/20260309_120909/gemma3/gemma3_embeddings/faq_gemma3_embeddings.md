# FAQ (gemma3:4b, automatisch generiert)

## Teams friert oder reagiert nicht mehr (weißes Fenster). Was kann ich tun?

**Topic/Label:** Stabilität: friert / teams / beim

**Antwort:**
**Kurzlösung:** Teams komplett beenden, Cache löschen und neu starten. Überprüfe Updates und teste die Web-Version.

**Schritte:**
1. Teams komplett über den Task-Manager beenden.
2. Teams Cache und Local Storage löschen.
3. Teams neu starten.
4. Falls das Problem weiterhin besteht, die Teams-Version mitteilen.

**Hinweise:**
- Teste die Web-Version von Teams als Alternative.

**Support:**
- Überprüfe Updates von Teams und Windows.
- Prüfe die WLAN-Verbindung und teste mit LAN oder einem anderen Access Point.
- Teste mit nur einem Monitor, falls mehrere Monitore verwendet werden.

**Belege (Tickets):** TCK-0303, TCK-0308, TCK-0311

---

## Ich erhalte beim Aktivieren von Office den Fehlercode 0xC004F074 oder die Meldung "Account not eligible". Was kann ich tun?

**Topic/Label:** Lizenz: aktivierung / office / aktiviert

**Antwort:**
**Kurzlösung:** Überprüfe dein Konto, die Netzwerkverbindung und starte den PC neu.

**Schritte:**
1. Überprüfe Datum/Uhrzeit und Netzwerkverbindung (im Firmennetz oder VPN).
2. Starte den PC neu.
3. Melde dich mit deinem Firmenkonto ab und wieder an.
4. Lösche gespeicherte Anmeldedaten im Windows-Anmeldeinformationsmanager (Office/Microsoft Einträge).

**Hinweise:**
- Das Problem kann durch eine fehlerhafte KMS-Kommunikation oder ein falsches Konto verursacht werden.

**Support:**
- Sende mir einen Screenshot, wenn das Problem weiterhin besteht.
- Ich prüfe, ob KMS/Token oder die installierte Office-Edition nicht zur Lizenz passt.
- Prüfen wir, ob mehrere Konten (privat/geschäftlich) parallel hinterlegt sind.

**Belege (Tickets):** TCK-0412, TCK-0403, TCK-0607

---

## Mein PC ist nach einem Windows-Update sehr langsam. Was kann ich tun?

**Topic/Label:** Performance: nach / update / windows

**Antwort:**
**Kurzlösung:** Lasse den PC nach dem Update 30-60 Minuten am Strom und im WLAN/LAN laufen. Überprüfe den Task-Manager auf ressourcenintensive Prozesse.

**Schritte:**
1. Lasse den PC 30-60 Minuten am Strom und im WLAN/LAN laufen.
2. Starte den PC neu.
3. Überprüfe im Task-Manager, ob "Windows Modules Installer" oder "Antimalware Service Executable" viel Last verursachen.
4. Schließe testweise große Programme und starte Teams/Browser neu.

**Hinweise:**
- Hintergrundprozesse wie Indexierung oder Defender können die Performance beeinträchtigen.
- Der Ordner Windows.old kann nach größeren Updates entstehen und sollte über die Datenträgerbereinigung entfernt werden.

**Support:**
- Bitte sende einen Screenshot vom Task-Manager (CPU/RAM/Datenträger), wenn das Problem weiterhin besteht.

**Belege (Tickets):** TCK-0301, TCK-0606, TCK-0313

---

## Ich habe mein Passwort vergessen und komme nicht mehr an meinen Reset-Link oder meine neue Zugangsdaten.

**Topic/Label:** Account: passwort / reset / bekomme

**Antwort:**
**Kurzlösung:** Bitte prüfe deinen Spam-Ordner und die E-Mail-Adresse, die du für den Passwort-Reset verwendet hast. Bei Problemen kann das Passwort manuell zurückgesetzt werden.

**Schritte:**
1. Nutze die Funktion 'Passwort vergessen' auf der Login-Seite.
2. Überprüfe deinen Spam-Ordner und die Quarantäne-Ordner deines E-Mail-Postfachs.
3. Stelle sicher, dass du die korrekte Firmen-E-Mail-Adresse verwendest (kein privates Postfach).

**Hinweise:**
- Wenn du keinen Link erhältst, bestätige deine Identität (z.B. Personalnummer), damit das Passwort manuell zurückgesetzt werden kann.

**Support:**
- Bei Problemen mit dem Reset-Link kann der Reset-Link erneut ausgelöst werden.
- Achte bei der Passwortwahl auf eine Mindestlänge und eine Mischung aus Groß-/Kleinbuchstaben, Zahlen und Sonderzeichen. Vermeide leicht erratbare Wörter und verwende besser eine Passphrase.

**Belege (Tickets):** TCK-0102, TCK-0114, TCK-0101

---

## Ich verbinde mich mit dem WLAN, aber es trennt sich sofort wieder.

**Topic/Label:** Netzwerk: wlan / verbindet / trennt

**Antwort:**
**Kurzlösung:** Entferne das WLAN-Profil und verbinde dich neu. Überprüfe, ob du das richtige Netz verwendest.

**Schritte:**
1. Entferne das WLAN-Profil komplett.
2. Verbinde dich neu.
3. Prüfe, ob du das richtige Netz (z. B. Mitarbeiter vs. Gast) verwendest.

**Hinweise:**
- Überprüfe, ob ein Zertifikat/Passwort-Problem vorliegt, wenn 802.1X verwendet wird.

**Support:**
- Starte den PC einmal neu.
- Prüfe, ob der WLAN-Treiber aktuell ist (Windows Update).
- Teste kurz in einem anderen Raum/nahe am Access Point.
- Bitte nenne mir Raum/Etage und Uhrzeiten der Abbrüche für die AP-Logprüfung.

**Belege (Tickets):** TCK-0610, TCK-0513, TCK-0501

---

## Warum druckt mein Drucker manchmal ein falsches Papierformat (z.B. A3 statt A4)?

**Topic/Label:** Drucker: drucker / drucke / immer

**Antwort:**
**Kurzlösung:** Überprüfe die Druckeinstellungen im Druckdialog und im Druckertreiber. Stelle sicher, dass das Papierformat korrekt eingestellt ist und dass das Druckerfach A4 enthält.

**Schritte:**
1. Prüfe das Papierformat (A4) im Druckdialog.
2. Prüfe die Standardpapiergröße im Druckertreiber.
3. Stelle sicher, dass das Druckerfach A4 enthält.
4. Sende einen Screenshot der Druckeinstellungen, falls nötig.

**Hinweise:**
- Oft ist in der Vorlage A3 gespeichert.

**Support:**
- Keine zusätzlichen Support-Aktionen erforderlich.

**Belege (Tickets):** TCK-0208, TCK-0207, TCK-0209

---

## Wie beantworte ich eine Anfrage nach einer Lizenz für ein neues Tool?

**Topic/Label:** Lizenz: lizenz / pro / keinen

**Antwort:**
**Kurzlösung:** Bitte geben Sie Projektname, benötigte Rolle, Begründung und Freigabe durch die Projektleitung an.

**Schritte:**
1. Senden Sie Projektname, benötigte Rolle (z. B. User/Admin), Begründung und idealerweise eine kurze Freigabe durch Projektleitung.

**Hinweise:**
- Nach Erhalt der Informationen kann ich die Lizenz zuweisen bzw. den Antrag im Lizenzsystem stellen.

**Support:**
- Sie erhalten eine Bestätigung, sobald die Zuweisung aktiv ist.

**Belege (Tickets):** TCK-0409, TCK-0608, TCK-0410

---

## Frage: Ich bin mit dem WLAN verbunden, aber kann keine Internetseiten laden. Was kann ich tun?
**Kurzlösung:** Trenne die WLAN-Verbindung und verbinde dich neu. 
    Überprüfe Proxy-Einstellungen und führe die Netzwerkproblembehandlung durch.

**Schritte:**
    1. Trenne die WLAN-Verbindung.
    2. Verbinde dich neu.
    3. Führe `ipconfig /release` und `ipconfig /renew` aus (falls erlaubt).
    4. Starte die Netzwerkproblembehandlung.
    5. Überprüfe Proxy-Einstellungen.

**Hinweise:**
- Überprüfe die WLAN-Details (IP-Adresse/Gateway) und sende einen Screenshot bei Bedarf.

**Belege (Tickets):** TCK-0503, TCK-0504, TCK-0505

---

## Warum verbraucht ein Prozess im Task-Manager viel CPU?

**Topic/Label:** Performance: cpu / voll / task

**Antwort:**
**Kurzlösung:** Hohe CPU-Auslastung kann durch verschiedene Prozesse verursacht werden, wie z.B. Windows Defender, OneDrive oder unbekannte Updater.

**Schritte:**
1. Überprüfe den Task-Manager auf CPU-intensive Prozesse.

**Hinweise:**
- Die Ursache kann ein Scan, eine Synchronisation oder ein Update sein.

**Support:**
- Bitte sende den Prozessnamen und einen Screenshot aus dem Task-Manager (Details-Tab) weiter, falls der Prozess unbekannt ist.

**Belege (Tickets):** TCK-0305, TCK-0605, TCK-0306

---

## Scan-to-Mail funktioniert nicht oder sendet an die falsche Adresse.

**Topic/Label:** Scannen: mail / scan to / to mail

**Antwort:**
**Kurzlösung:** Überprüfen Sie die Empfängeradresse, den Spam-Ordner und die Gerätekonfiguration (SMTP-Relay, Account, TLS).

**Schritte:**
1. Überprüfen Sie die ausgewählte Empfängeradresse.
2. Prüfen Sie den Spam-Ordner auf empfangene E-Mails.
3. Überprüfen Sie die Gerätekonfiguration (SMTP-Relay, Account, TLS).

**Hinweise:**
- Häufige Ursachen sind falsche Adressen, SMTP/Authentifizierungsprobleme oder blockierte Empfängeradressen.

**Support:**
- Bitte geben Sie den Gerätenamen, Standort und die Uhrzeit des Scans an.

**Belege (Tickets):** TCK-0205, TCK-0604, TCK-0212

---

## Mein Konto wird nach dem Login (z.B. über VPN) oder nach mehreren fehlgeschlagenen Anmeldeversuchen gesperrt. Was kann ich tun?

**Topic/Label:** Account: gesperrt / login / nach

**Antwort:**
**Kurzlösung:** Überprüfe gespeicherte Passwörter auf Geräten wie Smartphone, Outlook oder VPN-Client und aktualisiere diese. Setze das Passwort bei Bedarf über "Passwort vergessen" zurück.

**Schritte:**
1. Ändere das Passwort auf allen Geräten, auf denen ein altes Passwort gespeichert ist.
2. Aktualisiere die Anmeldedaten auf allen Geräten (Handy, Outlook, VPN-Client).
3. Wenn du dir das Passwort nicht sicher bist, setze es über "Passwort vergessen" zurück.

**Hinweise:**
- Die Sperrung kann durch alte gespeicherte Passwörter verursacht werden.
- Warte nach der Entsperrung 5 Minuten, bevor du dich erneut anmeldest.

**Support:**
- Kontaktiere den Support, wenn das Problem weiterhin besteht.

**Belege (Tickets):** TCK-0115, TCK-0104, TCK-0103

---

## Mein Drucker druckt sehr blass oder kaum lesbar / Der Drucker druckt langsam.

**Topic/Label:** Drucker: druck / druckt / drucker

**Antwort:**
**Kurzlösung:** Überprüfen Sie Tonerstand, rütteln Sie die Tonerkassette und führen Sie eine Kalibrierung durch. Testen Sie eine Testseite.

**Schritte:**
1. Prüfen Sie den Tonerstand am Gerät.
2. Rütteln Sie die Tonerkassette vorsichtig (falls vorgesehen).
3. Starten Sie eine Kalibrierung/Reinigung (Menü -> Wartung).
4. Drucken Sie eine interne Testseite.

**Hinweise:**
- Bei langsamen Drucken kann es an 'Als Bild drucken' oder dem Treibermodus liegen.

**Support:**
- Kontaktieren Sie den Support, wenn die Testseite ebenfalls blass ist oder die Ursache nicht gefunden werden kann.

**Belege (Tickets):** TCK-0603, TCK-0213, TCK-0201

---

