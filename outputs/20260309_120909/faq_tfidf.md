# FAQ (automatisch generiert)

## Druck dauert extrem lange?

**Topic/Label:** Drucker: druck / druckt / pdf

**Antwort:**
**Kurzlösung:** Stelle im Treiber testweise auf PCL6/Universal-Treiber um (falls vorhanden).

**Ursache/Erklärung:**
- Das deutet oft auf Toner/Drum oder verschmutzte Rollen hin.

**Schritte:**
1. Teste einmal eine kleine Testseite.
2. Wenn nur PDFs langsam sind, kann es an „Als Bild drucken“ oder am Treibermodus liegen.
3. Stelle im Treiber testweise auf PCL6/Universal-Treiber um (falls vorhanden).
4. Starte die Reinigungs-/Kalibrierungsfunktion am Drucker (Menü -> Wartung).
5. Wenn möglich, drucke eine interne Testseite.

**Hinweise:**
- Falls die Streifen bleiben, tauschen wir Toner/Drum bzw. erstellen eine Störung für den Service.

**Support:**
- Der IT-Support kann außerdem die Queue auf große Jobs prüfen, die alles blockieren.

**Belege (Tickets):** TCK-0213, TCK-0202, TCK-0211

---

## C: voll wegen Windows.old nach Update?

**Topic/Label:** Performance: nach / update / voll

**Antwort:**
**Kurzlösung:** Nutze „Datenträgerbereinigung“ bzw. „Speicher“ -> „Temporäre Dateien“ und wähle „Vorherige Windows-Installation(en)“.

**Ursache/Erklärung:**
- Das kann an Autostart-Programmen oder Profil-Skripten liegen.

**Schritte:**
1. Windows.old entsteht nach größeren Updates und kann nach erfolgreichem Betrieb entfernt werden.
2. Nutze „Datenträgerbereinigung“ bzw. „Speicher“ -> „Temporäre Dateien“ und wähle „Vorherige Windows-Installation(en)“.
3. Öffne Task-Manager -> Autostart und deaktiviere nicht benötigte Einträge.

**Hinweise:**
- Teste einmal mit Neustart und ohne VPN.
- Danach neu starten.
- Wenn du unsicher bist, warte ein paar Tage, bis alles stabil läuft, bevor du löschst.

**Support:**
- Der IT-Support prüft parallel, ob das Profil/Netzlaufwerke beim Login hängen.

**Belege (Tickets):** TCK-0606, TCK-0302, TCK-0313

---

## Lizenz für neues Tool anfragen (Jira)?

**Topic/Label:** Lizenz: lizenz / office / pro

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

## Standarddrucker verstellt sich ständig?

**Topic/Label:** Drucker: drucker / immer / wieder

**Antwort:**
**Kurzlösung:** Deaktiviere in Windows „Windows verwaltet Standarddrucker“ (Einstellungen -> Geräte -> Drucker & Scanner).

**Ursache/Erklärung:**
- Oft ist in der Vorlage A3 gespeichert.

**Schritte:**
1. Deaktiviere in Windows „Windows verwaltet Standarddrucker“ (Einstellungen -> Geräte -> Drucker & Scanner).
2. Setze anschließend den gewünschten Drucker als Standard.
3. Wenn du oft mit dem Laptop dockst, kann es sonst automatisch umschalten.
4. Prüfe im Druckdialog das Papierformat (A4) und im Druckertreiber die „Standardpapiergröße“.
5. Stelle außerdem sicher, dass im Druckerfach tatsächlich A4 eingelegt ist und das Fach korrekt eingestellt ist.
6. Wenn du willst, schick mir einen Screenshot der Druckeinstellungen.
7. Prüfe, ob der Drucker eingeschaltet ist und am Display eine IP-Adresse angezeigt wird.

**Belege (Tickets):** TCK-0207, TCK-0208, TCK-0210

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

## Proxy/PAC: automatische Konfiguration nicht erreichbar?

**Topic/Label:** Netzwerk: proxy / laden / seiten

**Antwort:**
**Kurzlösung:** Prüfe unter Windows -> Proxy, ob „Setupscript verwenden“ aktiv ist und ob die PAC-URL erreichbar ist.

**Schritte:**
1. Prüfe unter Windows -> Proxy, ob „Setupscript verwenden“ aktiv ist und ob die PAC-URL erreichbar ist.
2. Teste einmal, die automatische Erkennung kurz zu deaktivieren und den Browser neu zu starten.
3. Prüfe unter Windows „Proxy“ (Einstellungen -> Netzwerk & Internet -> Proxy), ob ein manueller Proxy gesetzt ist.
4. In der Regel muss das auf „Automatisch“ stehen bzw. das Unternehmens-Skript nutzen.
5. Deaktiviere testweise manuelle Einträge und starte den Browser neu.
6. Wenn ihr einen Pflicht-Proxy habt, prüfe ich die korrekte Konfiguration/URL.

**Benötigte Angaben:**
- Nenne dem IT-Support bitte Standort (Büro/Homeoffice/VPN).

**Hinweise:**
- Wenn es danach funktioniert, liegt vermutlich ein Problem mit dem PAC-Server vor – ich prüfe die Erreichbarkeit/Logs.

**Belege (Tickets):** TCK-0609, TCK-0507, TCK-0512

---

## Dockingstation: LAN wird nicht erkannt?

**Topic/Label:** Netzwerk: lan / funktioniert / lan wlan

**Antwort:**
**Kurzlösung:** Prüfe Treiber/Firmware der Dockingstation (falls eure IT das verteilt).

**Schritte:**
1. Trenne Dockingstation komplett (Strom + USB-C), warte 10 Sekunden und schließe alles neu an.
2. Prüfe Treiber/Firmware der Dockingstation (falls eure IT das verteilt).
3. Teste außerdem einen anderen USB-C Port.
4. Wenn LAN am gleichen Kabel ohne Dock geht, liegt es sehr wahrscheinlich an Dock/Treiber.
5. Prüfe, ob das LAN-Kabel richtig eingerastet ist und ob am Port/Adapter LEDs leuchten.
6. Teste wenn möglich ein anderes Kabel oder einen anderen Netzwerkport.
7. Prüfe zuerst, ob du im richtigen Netzwerk/VLAN bist (nach Umzug kann Port falsch gepatcht sein).

**Support:**
- Der IT-Support kann den Switch-Port prüfen (VLAN/Port deaktiviert) – dafür brauche ich Raum/Portnummer (falls am Anschluss steht) und deine MAC-Adresse.

**Belege (Tickets):** TCK-0505, TCK-0504, TCK-0510

---

## Teams friert beim Start ein?

**Topic/Label:** Stabilität: friert / beim / teams

**Antwort:**
**Kurzlösung:** Starte Outlook im abgesicherten Modus und teste ohne Add-ins.

**Schritte:**
1. Teams komplett beenden (Task-Manager) und den Cache löschen (Teams Cache/Local Storage).
2. Wenn es wieder passiert, prüfe Updates von Teams und Windows.
3. Alternativ kannst du testweise die Web-Version nutzen.
4. Prüfe zuerst die Größe der Mail/Anhänge.
5. Starte Outlook im abgesicherten Modus und teste ohne Add-ins.
6. Wenn es weiter passiert: OST-Datei neu erstellen (Konto entfernen/neu hinzufügen) und Windows-Updates prüfen.

**Benötigte Angaben:**
- Sende dem IT-Support bitte deine Teams-Version, falls es bleibt.

**Hinweise:**
- Danach Teams neu starten.

**Belege (Tickets):** TCK-0303, TCK-0311, TCK-0308

---

## WLAN langsam zu Stoßzeiten?

**Topic/Label:** Netzwerk: wlan / langsam / verbindet

**Antwort:**
**Kurzlösung:** Trenne die WLAN-Verbindung und verbinde dich neu.

**Schritte:**
1. Das klingt nach Überlast.
2. Als Workaround: wenn möglich 5GHz nutzen oder kurz auf LAN wechseln.
3. Trenne die WLAN-Verbindung und verbinde dich neu.
4. Prüfe, ob eine Proxy-Einstellung aktiv ist.

**Benötigte Angaben:**
- Nenne Standort (Etage/Raum) und die Zeiten.
- Wenn es weiter besteht, sende dem IT-Support einen Screenshot der WLAN-Details (IP-Adresse/Gateway).

**Hinweise:**
- Danach: `ipconfig /release` und `ipconfig /renew` (falls erlaubt) bzw. Netzwerkproblembehandlung starten.

**Support:**
- Der IT-Support prüft Auslastung des Access Points und ob ein Kanalwechsel/Load-Balancing nötig ist.

**Belege (Tickets):** TCK-0511, TCK-0503, TCK-0610

---

## Passwort-Reset Link kommt nicht an?

**Topic/Label:** Account: passwort / link / reset

**Antwort:**
**Kurzlösung:** Prüfe Spam/Quarantäne und ob du die richtige Firmen-E-Mail-Adresse verwendet hast.

**Schritte:**
1. Prüfe Spam/Quarantäne und ob du die richtige Firmen-E-Mail-Adresse verwendet hast.
2. Wenn du ein privates Postfach eingetragen hast, funktioniert es nicht.
3. Teile mir bitte den Zeitpunkt des Versuchs mit.
4. Reset-Links sind zeitlich begrenzt.
5. Starte den Prozess „Passwort vergessen“ erneut und nutze den neuesten Link.
6. Wenn du mehrere Mails bekommen hast, ist nur die letzte gültig.

**Support:**
- Der IT-Support kann den Reset-Link erneut auslösen und das Postfach-Logging prüfen.
- Falls es weiterhin fehlschlägt, prüfe bitte die Systemzeit deines PCs und gib dem IT-Support den Zeitpunkt des Versuchs durch.

**Belege (Tickets):** TCK-0102, TCK-0601, TCK-0101

---

## MFA Nummer geändert – Login blockiert?

**Topic/Label:** Security: mfa / code / login

**Antwort:**
**Kurzlösung:** Aktiviere „Datum/Uhrzeit automatisch“ und öffne in der Authenticator-App (falls vorhanden) die Option „Zeitkorrektur/Synchronisieren“.

**Ursache/Erklärung:**
- Das passiert häufig bei abweichender Uhrzeit am Smartphone.

**Schritte:**
1. Aktiviere „Datum/Uhrzeit automatisch“ und öffne in der Authenticator-App (falls vorhanden) die Option „Zeitkorrektur/Synchronisieren“.
2. Wenn es weiterhin nicht klappt, kann ich die MFA-Registrierung zurücksetzen, damit du sie neu einrichten kannst (nach Identitätsprüfung).
3. Prüfe Netzempfang/Flugmodus und ob die Nummer korrekt hinterlegt ist.

**Benötigte Angaben:**
- Sende dem IT-Support die neue Nummer über den sicheren Kanal (nicht im Tickettext, falls euer Prozess das so vorsieht) und bestätige kurz deine Identität.

**Hinweise:**
- Danach richtest du MFA neu ein.
- Danach erneut versuchen.

**Support:**
- Der IT-Support kann die hinterlegte MFA-Telefonnummer nach Identitätsprüfung aktualisieren oder die MFA-Registrierung zurücksetzen.

**Belege (Tickets):** TCK-0113, TCK-0602, TCK-0108

---

## Hohe CPU: Prozess 'Antimalware Service Executable'?

**Topic/Label:** Performance: cpu / prozess / hohe cpu

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

