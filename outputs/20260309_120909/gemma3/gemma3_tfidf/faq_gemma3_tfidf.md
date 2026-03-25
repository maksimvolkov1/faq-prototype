# FAQ (gemma3:4b, automatisch generiert)

## Warum druckt mein PDF langsam oder gar nicht?

**Topic/Label:** Drucker: druck / druckt / pdf

**Antwort:**
**Kurzlösung:** Langsame Druckzeiten von PDFs können auf Probleme mit der Bilddruckfunktion, dem Druckertreiber oder blockierten Jobs zurückzuführen sein. Schlechte Druckqualität kann durch Tonerprobleme oder verschmutzte Rollen verursacht werden.

**Schritte:**
1. Teste eine kleine Testseite.
2. Probiere einen anderen Druckertreiber (z.B. PCL6/Universal-Treiber).
3. Starte die Reinigungs-/Kalibrierungsfunktion des Druckers (Menü -> Wartung).
4. Drucke eine interne Testseite.

**Hinweise:**
- Probleme mit PDFs können durch "Als Bild drucken" verursacht werden.
- Schwarze Streifen können auf Toner/Drum oder verschmutzte Rollen hindeuten.

**Support:**
- Überprüfe die Wartungsfunktionen des Druckers.
- Überprüfe den Print-Log mit Dokumenttyp und Uhrzeit.

**Belege (Tickets):** TCK-0213, TCK-0202, TCK-0211

---

## Warum ist meine Festplatte C: nach einem Update voll?

**Topic/Label:** Performance: nach / update / voll

**Antwort:**
**Kurzlösung:** Nach größeren Updates wird oft ein Ordner namens Windows.old erstellt. Dieser kann über die Datenträgerbereinigung entfernt werden.

**Schritte:**
1. Öffne die Datenträgerbereinigung (Speicher -> Temporäre Dateien).
2. Wähle 'Vorherige Windows-Installation(en)' aus.
3. Starte den Computer neu.

**Hinweise:**
- Warte nach dem Update ein paar Tage, bis alles stabil läuft, bevor du den Ordner löschst.
- Wenn du unsicher bist, kann der Ordner automatisch entfernt werden.

**Support:**
- Die Datenträgerbereinigung löscht temporäre Dateien und vorherige Windows-Installationen.

**Belege (Tickets):** TCK-0606, TCK-0302, TCK-0313

---

## Ich habe keinen Zugriff auf ein neues Tool (z.B. Jira, Power BI Pro, Confluence). Was soll ich tun?

**Topic/Label:** Lizenz: lizenz / office / pro

**Antwort:**
**Kurzlösung:** Bitte senden Sie Informationen zum Projekt, benötigten Rollen/Dauer und holen Sie die notwendige Freigabe ein. Anschließend wird Ihnen die Lizenz zugewiesen.

**Schritte:**
1. Nennen Sie den Namen des Projekts, die benötigte Rolle (z.B. User/Admin) und die Begründung für den Lizenzbedarf.
2. Holen Sie die Freigabe von der Projektleitung oder Kostenstelle ein.

**Hinweise:**
- Nach der Zuweisung müssen Sie die Lizenz möglicherweise einmal ab- und wieder anmelden, um die Berechtigung zu aktivieren.

**Support:**
- Geben Sie den Space/Projekt und die verantwortliche Person bei Confluence an.

**Belege (Tickets):** TCK-0409, TCK-0608, TCK-0410

---

## Mein Standarddrucker wechselt immer wieder. Was kann ich tun?

**Topic/Label:** Drucker: drucker / immer / wieder

**Antwort:**
**Kurzlösung:** Deaktiviere Windows verwalteten Standarddrucker und setze den gewünschten Drucker als Standard.

**Schritte:**
1. Deaktiviere in Windows „Windows verwaltet Standarddrucker“ (Einstellungen -> Geräte -> Drucker & Scanner).

**Hinweise:**
- Wenn du oft mit dem Laptop dockst, kann es sonst automatisch umschalten.

**Belege (Tickets):** TCK-0207, TCK-0208, TCK-0210

---

## Scan-to-Mail funktioniert nicht oder sendet an die falsche Adresse.

**Topic/Label:** Scannen: mail / scan to / to mail

**Antwort:**
**Kurzlösung:** Überprüfen Sie die Empfängeradresse, die SMTP-Konfiguration und die Geräteinstellungen.  Überprüfen Sie auch das Adressbuch.

**Schritte:**
1. Überprüfen Sie die ausgewählte Empfängeradresse.
2. Prüfen Sie, ob die E-Mail im Spam-Ordner liegt.
3. Überprüfen Sie die Gerätekonfiguration (SMTP-Relay, Account, TLS).
4. Überprüfen Sie das Adressbuch auf Standardeinträge oder alte Adressen.

**Hinweise:**
- Bitte geben Sie den Gerätenamen, Standort und die Uhrzeit des Scans an.

**Support:**
- Bei Problemen mit SMTP/Authentifizierung kontaktieren Sie den Support.

**Belege (Tickets):** TCK-0205, TCK-0604, TCK-0212

---

## Warum kann ich bestimmte Websites nicht laden, und was bedeutet das mit dem Proxy?

**Topic/Label:** Netzwerk: proxy / laden / seiten

**Antwort:**
**Kurzlösung:** Überprüfe die Proxy-Einstellungen in deinem Browser und teste, ob ein manueller Proxy aktiv ist oder ob eine Erweiterung die Seiten blockiert.

**Schritte:**
1. Prüfe die Proxy-Einstellungen in Windows (Einstellungen -> Netzwerk & Internet -> Proxy).
2. Stelle sicher, dass der Proxy auf 'Automatisch' steht oder das Unternehmens-Skript genutzt wird.
3. Deaktiviere testweise manuelle Proxy-Einträge und starte den Browser neu.
4. Teste im Inkognito-Fenster.
5. Überprüfe, ob Browser-Erweiterungen (z.B. Adblocker) die Seiten blockieren.

**Hinweise:**
- Bei Problemen kann eine Deaktivierung der automatischen Proxy-Konfiguration helfen.
- Prüfe die Erreichbarkeit des PAC-Servers, falls verwendet.

**Support:**
- Bitte gib bei Problemen die Umgebung (Büro/Homeoffice/VPN) und die betroffenen Domains sowie Fehlermeldungen an.

**Belege (Tickets):** TCK-0609, TCK-0507, TCK-0512

---

## Mein LAN funktioniert nicht, nur WLAN. Was kann ich tun?

**Topic/Label:** Netzwerk: lan / funktioniert / lan wlan

**Antwort:**
**Kurzlösung:** Bitte trenne die Dockingstation komplett, warte 10 Sekunden und schließe sie neu an. Prüfe Treiber/Firmware und teste einen anderen USB-C Port.

**Schritte:**
1. Trenne die Dockingstation (Strom + USB-C).
2. Warte 10 Sekunden.
3. Schließe die Dockingstation neu an.
4. Prüfe Treiber/Firmware der Dockingstation.
5. Teste einen anderen USB-C Port.

**Hinweise:**
- Wenn das LAN am gleichen Kabel ohne Dock funktioniert, liegt das Problem wahrscheinlich am Dock oder den Treibern.
- Überprüfe die LAN-Kabelverbindung und die LEDs am Port/Adapter.

**Support:**
- Kontaktiere den Support, wenn das Problem weiterhin besteht. Bitte gib Raum/Portnummer und PC-Name an.

**Belege (Tickets):** TCK-0505, TCK-0504, TCK-0510

---

## Teams friert beim Start oder bei der Nutzung ein.

**Topic/Label:** Stabilität: friert / beim / teams

**Antwort:**
**Kurzlösung:** Versuchen Sie, Teams zu beenden, den Cache zu löschen und Teams neu zu starten. Überprüfen Sie Updates, Add-ins und die Netzwerkverbindung.

**Schritte:**
1. Teams komplett beenden (Task-Manager)
2. Teams Cache/Local Storage löschen
3. Teams neu starten
4. Updates von Teams und Windows prüfen
5. Testweise die Web-Version nutzen

**Hinweise:**
- Überprüfen Sie die Größe von E-Mails und Anhängen (Outlook).
- Testen Sie den abgesicherten Modus von Outlook.
- Überprüfen Sie Windows-Updates.
- Testen Sie ohne VPN (falls verwendet).
- Schließen Sie unnötige Programme.
- Überprüfen Sie die WLAN-Verbindung oder testen Sie LAN/anderen Access Point.
- Stellen Sie sicher, dass Teams aktualisiert ist.
- Testen Sie mit nur einem Monitor (bei Verwendung mehrerer Monitore).

**Support:**
- Bitte senden Sie Ihre Teams-Version, falls das Problem weiterhin besteht.

**Belege (Tickets):** TCK-0303, TCK-0311, TCK-0308

---

## Warum ist mein WLAN manchmal extrem langsam oder verbindet sich nicht?

**Topic/Label:** Netzwerk: wlan / langsam / verbindet

**Antwort:**
**Kurzlösung:** Versuchen Sie, sich neu zu verbinden, die IP-Adresse zu aktualisieren oder ein anderes WLAN-Kanal zu verwenden. Überprüfen Sie die Netzwerkeinstellungen und entfernen/ändern Sie Gast-WLAN-Profile.

**Schritte:**
1. Trennen und wiederherstellen der WLAN-Verbindung.
2. Führen Sie `ipconfig /release` und `ipconfig /renew` aus (falls erlaubt).
3. Überprüfen Sie die Netzwerkeinstellungen und entfernen Sie Gast-WLAN-Profile (Bekannte Netzwerke verwalten -> Entfernen).
4. Verbinden Sie sich manuell mit dem Firmennetz und speichern Sie die Zugangsdaten.

**Hinweise:**
- Die Langsamkeit kann durch Überlastung verursacht werden.
- Der Wechsel zwischen Firmen- und Gastnetz kann die Ursache sein.

**Support:**
- Kontaktieren Sie den Support, wenn das Problem weiterhin besteht. Geben Sie Standort und Zeiten an.

**Belege (Tickets):** TCK-0511, TCK-0503, TCK-0610

---

## Ich habe den Link zum Zurücksetzen meines Passworts erhalten, aber er funktioniert nicht oder ist abgelaufen. Was soll ich tun?

**Topic/Label:** Account: passwort / link / reset

**Antwort:**
**Kurzlösung:** Bitte starte den Prozess "Passwort vergessen" erneut und verwende den neuesten generierten Link. Überprüfe auch deinen Spam-Ordner und die Systemzeit deines PCs.

**Schritte:**
1. Starte den Prozess "Passwort vergessen".
2. Überprüfe deinen Spam-Ordner.
3. Überprüfe die Systemzeit deines PCs.

**Hinweise:**
- Reset-Links sind zeitlich begrenzt.
- Verwende nur den letzten erhaltenen Link.

**Support:**
- Bei Problemen mit dem Empfang des Links, prüfe, ob du eine Firmen-E-Mail-Adresse verwendest. Private Postfächer funktionieren nicht.
- Bitte gib den Zeitpunkt des Versuchs an.

**Belege (Tickets):** TCK-0102, TCK-0601, TCK-0101

---

## Ich erhalte keinen MFA-Code oder der Code wird abgelehnt. Was kann ich tun?

**Topic/Label:** Security: mfa / code / login

**Antwort:**
**Kurzlösung:** Überprüfen Sie die Uhrzeit Ihres Smartphones, den Netzempfang und die hinterlegte Telefonnummer. Bei Problemen kann die MFA-Registrierung zurückgesetzt oder die Methode auf einen Authenticator umgestellt werden.

**Schritte:**
1. Überprüfen Sie den Netzempfang und stellen Sie sicher, dass der Flugmodus deaktiviert ist.
2. Stellen Sie sicher, dass die korrekte Telefonnummer hinterlegt ist.
3. Aktivieren Sie 'Datum/Uhrzeit automatisch' auf Ihrem Smartphone.
4. Synchronisieren Sie die Zeit in Ihrer Authenticator-App.
5. Starten Sie Ihr Smartphone neu und fordern Sie den Code erneut an.
6. Bei anhaltenden Problemen: Kontaktieren Sie den Support für die Rücksetzung der MFA-Registrierung (nach Identitätsprüfung) oder die Umstellung auf einen Authenticator.

**Hinweise:**
- Abweichende Uhrzeiten am Smartphone können zu Problemen mit den Codes führen.
- Stellen Sie sicher, dass die hinterlegte Telefonnummer korrekt ist.

**Support:**
- MFA-Telefonnummer aktualisieren
- MFA-Registrierung zurücksetzen
- Authenticator-App verwenden
- Temporären Backup-Code bereitstellen

**Belege (Tickets):** TCK-0113, TCK-0602, TCK-0108

---

## Warum verbraucht ein Prozess meine CPU-Ressourcen?

**Topic/Label:** Performance: cpu / prozess / hohe cpu

**Antwort:**
**Kurzlösung:** Hohe CPU-Auslastung kann durch verschiedene Prozesse verursacht werden, wie z.B. Windows Defender, OneDrive oder unbekannte Updater/Sync-Clients.

**Schritte:**
1. Überprüfe den Task-Manager auf CPU-intensive Prozesse.
2. Lasse Scans von Windows Defender oder andere Synchronisations-Clients (z.B. OneDrive) vollständig abschließen.
3. Pausiere testweise die Synchronisation von OneDrive für 10 Minuten.

**Hinweise:**
- Hohe CPU-Auslastung kann durch laufende Synchronisationen, Sync-Fehler oder Updates verursacht werden.
- Ein Neustart des PCs kann oft vorübergehende Probleme beheben.

**Support:**
- Sende den exakten Prozessnamen und einen Screenshot aus dem Task-Manager (Details-Tab) an den Support, falls der Prozess unbekannt ist.

**Belege (Tickets):** TCK-0305, TCK-0605, TCK-0306

---

