# Cluster Report (TF-IDF + KMeans)

- Tickets: 85
- Cluster (k): 12
- Silhouette (cosine): 0.121

## Cluster 0 (5 Tickets)
**Keywords:** druck, druckt, pdf, schlechte, ausdrucke, seiten

**Beispiele:**
- `TCK-0213` – Druck dauert extrem lange
  - Druck dauert extrem lange Einfaches PDF braucht mehrere Minuten,
    bis es druckt.
- `TCK-0202` – Druck mit Streifen / schlechte Qualität
  - Druck mit Streifen / schlechte Qualität Ausdrucke haben seit gestern
    schwarze Streifen über die Seite.
- `TCK-0211` – Druckauftrag verschwindet einfach
  - Druckauftrag verschwindet einfach Ich sende einen Druck, kurz danach 
    ist er weg und es kommt nichts raus.

## Cluster 1 (13 Tickets)
**Keywords:** nach, update, voll, anmelden, fast voll, fast

**Beispiele:**
- `TCK-0606` – C: voll wegen Windows.old nach Update
  - C: voll wegen Windows.old nach Update Nach dem letzten Update ist C: fast voll. Ich sehe einen Ordner Windows.old mit vielen GB.
- `TCK-0302` – PC hängt nach Login / schwarzer Bildschirm kurz
  - PC hängt nach Login / schwarzer Bildschirm kurz Nach dem Anmelden bleibt der Bildschirm lange schwarz und der Desktop lädt sehr spät.
- `TCK-0313` – Hohe RAM-Auslastung – PC wird träge
  - Hohe RAM-Auslastung – PC wird träge Nach ein paar Stunden Arbeit ist der PC träge und RAM ist fast voll.

## Cluster 2 (12 Tickets)
**Keywords:** lizenz, office, pro, lizenz abgelaufen, keinen, abgelaufen

**Beispiele:**
- `TCK-0409` – Lizenz für neues Tool anfragen (Jira)
  - Lizenz für neues Tool anfragen (Jira) Ich brauche eine Jira-Lizenz für das Projekt, aktuell habe ich keinen Zugriff.
- `TCK-0608` – Lizenz für neues Tool anfragen (Power BI Pro)
  - Lizenz für neues Tool anfragen (Power BI Pro) Für das Reporting benötige ich eine Power BI Pro Lizenz. Aktuell habe ich nur Zugriff auf die Free-Version.
- `TCK-0410` – Lizenz für neues Tool anfragen (Confluence)
  - Lizenz für neues Tool anfragen (Confluence) Ich soll Dokumentation in Confluence pflegen, aber ich habe keinen Zugang.

## Cluster 3 (8 Tickets)
**Keywords:** drucker, immer, wieder, immer wieder, drucke, drucken

**Beispiele:**
- `TCK-0207` – Standarddrucker verstellt sich ständig
  - Standarddrucker verstellt sich ständig Mein Standarddrucker springt immer wieder auf einen anderen Drucker.
- `TCK-0208` – Falsches Papierformat (A4/A3)
  - Falsches Papierformat (A4/A3) Der Drucker will A3, obwohl ich A4 drucke. Dadurch kommt immer eine Fehlermeldung.
- `TCK-0210` – Drucker offline / nicht erreichbar
  - Drucker offline / nicht erreichbar Windows zeigt den Drucker als „Offline“ an. Drucken geht gar nicht.

## Cluster 4 (4 Tickets)
**Keywords:** mail, to mail, to, scan to, scan, sendet

**Beispiele:**
- `TCK-0205` – Scanner sendet nicht an E-Mail
  - Scanner sendet nicht an E-Mail Scan-to-Mail funktioniert nicht. Es kommt keine Mail an.
- `TCK-0604` – Scan-to-Mail: Zustellung schlägt fehl (Bounce)
  - Scan-to-Mail: Zustellung schlägt fehl (Bounce) Scan-to-Mail sendet scheinbar, aber ich bekomme danach eine Unzustellbarkeitsmeldung (Bounce).
- `TCK-0212` – Scanner sendet an falsche Adresse
  - Scanner sendet an falsche Adresse Scan-to-Mail geht, aber die Scans landen bei einer falschen Mailadresse.

## Cluster 5 (5 Tickets)
**Keywords:** proxy, laden, seiten, websites, externe, dns

**Beispiele:**
- `TCK-0609` – Proxy/PAC: automatische Konfiguration nicht erreichbar
  - Proxy/PAC: automatische Konfiguration nicht erreichbar Seit heute 
    laden Websites nicht. In den Netzwerkeinstellungen steht etwas von 
    automatischer Proxy-Konfiguration, aber es klappt nicht.
- `TCK-0507` – Websites laden nicht wegen Proxy
  - Websites laden nicht wegen Proxy Viele Websites laden nicht, im 
    Browser steht etwas von Proxy.
- `TCK-0512` – DNS/Proxy: nur bestimmte Seiten gehen
  - DNS/Proxy: nur bestimmte Seiten gehen Google geht, aber mehrere 
    andere Seiten (auch externe) laden nicht.

## Cluster 6 (5 Tickets)
**Keywords:** lan, funktioniert, lan wlan, verbunden, wlan, ungültig

**Beispiele:**
- `TCK-0505` – Dockingstation: LAN wird nicht erkannt
  - Dockingstation: LAN wird nicht erkannt An der Dockingstation funktioniert LAN nicht, nur WLAN.
- `TCK-0504` – LAN funktioniert nicht nach Umzug
  - LAN funktioniert nicht nach Umzug Ich bin umgezogen und seitdem geht mein LAN nicht mehr. WLAN geht.
- `TCK-0510` – LAN: verbunden, aber keine Netzlaufwerke
  - LAN: verbunden, aber keine Netzlaufwerke LAN ist verbunden, aber ich komme nicht auf Netzlaufwerke/Server.

## Cluster 7 (8 Tickets)
**Keywords:** friert, beim, teams, hängen, outlook, sich

**Beispiele:**
- `TCK-0303` – Teams friert beim Start ein
  - Teams friert beim Start ein Teams öffnet sich, aber reagiert nicht mehr (weißes Fenster).
- `TCK-0311` – Outlook friert beim Senden ein
  - Outlook friert beim Senden ein Beim Senden bleibt Outlook hängen und reagiert nicht mehr.
- `TCK-0308` – Teams hängt beim Bildschirmteilen
  - Teams hängt beim Bildschirmteilen Beim Bildschirmteilen friert Teams kurz ein und ruckelt stark.

## Cluster 8 (10 Tickets)
**Keywords:** wlan, langsam, verbindet, extrem langsam, extrem, pc

**Beispiele:**
- `TCK-0511` – WLAN langsam zu Stoßzeiten
  - WLAN langsam zu Stoßzeiten Nachmittags ist WLAN extrem langsam, morgens geht es.
- `TCK-0503` – WLAN verbunden, aber kein Internet
  - WLAN verbunden, aber kein Internet Ich bin mit dem WLAN verbunden, aber Internetseiten laden nicht.
- `TCK-0610` – WLAN verbindet mit Gastnetz statt Firmennetz
  - WLAN verbindet mit Gastnetz statt Firmennetz Mein Laptop verbindet sich automatisch mit dem Gast-WLAN. Im Firmennetz kann ich dann keine internen Seiten öffnen.

## Cluster 9 (5 Tickets)
**Keywords:** passwort, link, reset, vergessen, passwort vergessen, reset link

**Beispiele:**
- `TCK-0102` – Passwort-Reset Link kommt nicht an
  - Passwort-Reset Link kommt nicht an Ich habe „Passwort vergessen“ genutzt, aber es kommt keine Mail mit dem Link an.
- `TCK-0601` – Passwort-Reset: Link abgelaufen
  - Passwort-Reset: Link abgelaufen Ich habe den Reset-Link aus der E-Mail geöffnet, aber es steht „Link ungültig oder abgelaufen“. Ich komme nicht rein.
- `TCK-0101` – Passwort vergessen – Login ins Intranet nicht möglich
  - Passwort vergessen – Login ins Intranet nicht möglich Ich habe mein Passwort vergessen und komme nicht mehr ins Intranet. Können Sie mir helfen?

## Cluster 10 (7 Tickets)
**Keywords:** mfa, code, login, authenticator, habe, geändert

**Beispiele:**
- `TCK-0113` – MFA Nummer geändert – Login blockiert
  - MFA Nummer geändert – Login blockiert Ich habe eine neue Telefonnummer. Jetzt kann ich keinen Code empfangen und komme nicht rein.
- `TCK-0602` – MFA: Einmalcodes funktionieren nicht
  - MFA: Einmalcodes funktionieren nicht Ich gebe den Code aus der Authenticator-App ein, aber er wird immer abgelehnt.
- `TCK-0108` – MFA Code kommt nicht an (SMS)
  - MFA Code kommt nicht an (SMS) Beim Login wird ein SMS-Code verlangt, aber ich bekomme keine SMS.

## Cluster 11 (3 Tickets)
**Keywords:** cpu, prozess, hohe cpu, task, manager, hohe

**Beispiele:**
- `TCK-0305` – Hohe CPU: Prozess 'Antimalware Service Executable'
  - Hohe CPU: Prozess 'Antimalware Service Executable' Mein Laptop ist laut und langsam. Im Task-Manager zieht 'Antimalware Service Executable' sehr viel CPU.
- `TCK-0605` – Hohe CPU durch OneDrive.exe
  - Hohe CPU durch OneDrive.exe Mein PC ist langsam und der Lüfter läuft. Im Task-Manager zieht OneDrive.exe dauerhaft viel CPU.
- `TCK-0306` – Hohe CPU durch Prozess X (Unbekannt)
  - Hohe CPU durch Prozess X (Unbekannt) Im Task-Manager sehe ich einen Prozess, der ständig 80–90% CPU nutzt. Ich weiß nicht, was das ist.

