## Aufgabe 1 - VPNs 

**a) Erkläre in eigenen Worten, wie ein VPN funktioniert.**

Ein VPN (Virtuelles Privates Netzwerk) ermöglicht es, eine sichere und verschlüsselte Verbindung über ein weniger sicheres Netzwerk, wie das Internet, herzustellen. Es erstellt einen „Tunnel“, durch den die Daten sicher übertragen werden. Dabei wird der Datenverkehr verschlüsselt, sodass er vor Dritten, wie Hackern oder Internetdienstanbietern, geschützt ist.

**b) Nenne drei Vorteile und zwei potenzielle Nachteile eines VPNs.**

**Vorteile:**
1. **Sicherheit und Datenschutz:** VPNs verschlüsseln den Datenverkehr, wodurch vertrauliche Informationen geschützt werden.
2. **Anonymität:** Durch die Nutzung eines VPNs bleibt die tatsächliche IP-Adresse des Benutzers verborgen, was zu mehr Anonymität im Internet führt.
3. **Zugriff auf gesperrte Inhalte:** VPNs ermöglichen den Zugriff auf Inhalte, die in bestimmten Regionen gesperrt oder eingeschränkt sind.

**Nachteile:**
1. **Geschwindigkeitseinbußen:** Die zusätzliche Verschlüsselung und der Umweg über VPN-Server können zu einer langsameren Internetverbindung führen.
2. **Kosten:** Hochwertige VPN-Dienste sind oft kostenpflichtig, was zusätzliche Ausgaben bedeuten kann.

## Aufgabe 2 - OSI Modell 

**1. Ordne folgende Begriffe den richtigen OSI-Schichten zu:**

- **HTTP:** Anwendungsschicht (Layer 7)
- **TCP:** Transportschicht (Layer 4)
- **MAC-Adresse:** Sicherungsschicht (Layer 2)
- **Router:** Netzwerkschicht (Layer 3)
- **DNS:** Anwendungsschicht (Layer 7)

**2. Skizziere den Datenfluss durch die OSI-Schichten bei einer HTTP-Anfrage.**

In einem lokalen Netzwerk sendet Rechner A (192.168.0.2) von einem Browser aus eine Anfrage für eine Website (HTTP Get Request) an einen Server, der auf Rechner B (192.168.0.3) gehostet ist.

1. **Anwendungsschicht (Layer 7):** Der Browser auf Rechner A erstellt eine HTTP-GET-Anfrage.
2. **Darstellungsschicht (Layer 6):** Die Daten werden in ein Standardformat (z.B. ASCII) konvertiert.
3. **Sitzungsschicht (Layer 5):** Eine Sitzung wird aufgebaut, um die Kommunikation zu steuern.
4. **Transportschicht (Layer 4):** Die Anfrage wird in TCP-Segmente aufgeteilt und mit Quell- und Zielportnummern versehen.
5. **Netzwerkschicht (Layer 3):** Die TCP-Segmente werden in IP-Pakete verpackt und mit den IP-Adressen von Rechner A und Rechner B versehen.
6. **Sicherungsschicht (Layer 2):** Die IP-Pakete werden in Frames konvertiert und mit MAC-Adressen versehen.
7. **Bitübertragungsschicht (Layer 1):** Die Frames werden als elektrische oder optische Signale über das Netzwerkmedium gesendet.

Auf Rechner B durchläuft der Datenfluss die OSI-Schichten in umgekehrter Reihenfolge, um die HTTP-Anfrage zu empfangen und zu verarbeiten.

## Aufgabe 3 - Authentifizierung und Autorisierung 

**Erkläre die Begriffe Authentifizierung und Autorisierung und nenne je zwei Beispiele.**

**Authentifizierung:**
Die Authentifizierung ist der Prozess der Überprüfung der Identität eines Benutzers oder Systems. Es geht darum sicherzustellen, dass jemand tatsächlich derjenige ist, der er vorgibt zu sein.
- **Beispiel 1:** Benutzername und Passwort-Eingabe bei der Anmeldung auf einer Website.
- **Beispiel 2:** Zwei-Faktor-Authentifizierung (2FA) mit einem zusätzlichen Code, der an das Mobiltelefon des Benutzers gesendet wird.

**Autorisierung:**
Die Autorisierung ist der Prozess der Festlegung, welche Ressourcen oder Dienste ein authentifizierter Benutzer oder Systemzugriff hat. Es geht darum sicherzustellen, dass jemand nur auf die Ressourcen zugreift, zu denen er berechtigt ist.
- **Beispiel 1:** Ein Administrator hat Zugriff auf die Einstellungen einer Website, während ein normaler Benutzer nur auf den Inhalt zugreifen kann.
- **Beispiel 2:** Ein Mitarbeiter hat Zugriff auf bestimmte Dateien im Unternehmensnetzwerk basierend auf seiner Rolle und Abteilung.