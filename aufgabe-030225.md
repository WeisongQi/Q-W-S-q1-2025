# Grundlagen des Datenschutzes

## Aufgabe 1: Datenschutz-Glossar

1. **Datenschutz**
   - **Definition**: Maßnahmen zum Schutz personenbezogener Daten vor unbefugtem Zugriff oder Missbrauch.
   - **Beispiel**: Beim Online-Shopping verwendet der Händler SSL-Verschlüsselung, um die Zahlungsinformationen der Benutzer zu schützen.

2. **Personenbezogene Daten**
   - **Definition**: Jede Information, die sich auf eine identifizierte oder identifizierbare Person bezieht.
   - **Beispiel**: Name, Adresse, E-Mail-Adresse usw.

3. **Sensible Daten**
   - **Definition**: Informationen, die die Privatsphäre einer Person betreffen, wie Gesundheitsdaten, Rasse, religiöse Überzeugungen usw.
   - **Beispiel**: Medizinische Aufzeichnungen, biometrische Daten.

4. **Anonymisierung**
   - **Definition**: Entfernung persönlicher Identifikationsmerkmale aus Daten, sodass die Daten nicht mehr auf eine spezifische Person zurückgeführt werden können.
   - **Beispiel**: Bei statistischen Erhebungen werden Namen und Adressen entfernt, wobei nur Alter, Geschlecht usw. erhalten bleiben.

5. **Pseudonymisierung**
   - **Definition**: Ersetzung echter Informationen durch Codes oder virtuelle Identitäten zum Schutz der Privatsphäre.
   - **Beispiel**: In Studien wird eine Benutzer-ID anstelle des echten Namens verwendet, um Daten zu analysieren.

6. **Datenschutzbeauftragter**
   - **Definition**: Eine Person, die für die Überwachung und Verwaltung von Datenschutzangelegenheiten in einer Organisation verantwortlich ist und sicherstellt, dass die geltenden Vorschriften eingehalten werden.
   - **Beispiel**: Ein Unternehmen stellt einen Datenschutzbeauftragten ein, um Datenschutzrichtlinien zu erstellen und umzusetzen.

7. **Datenleck**
   - **Definition**: Unbefugte Offenlegung von Daten, die zu einem Verlust persönlicher Informationen führt.
   - **Beispiel**: Ein Hackerangriff auf die Datenbank eines Unternehmens, bei dem Kreditkarteninformationen der Benutzer gestohlen werden.

8. **Datensicherheit**
   - **Definition**: Maßnahmen zum Schutz von Daten vor unbefugtem Zugriff, Offenlegung, Zerstörung oder Verlust.
   - **Beispiel**: Verwendung von Firewalls, Verschlüsselungstechniken und Zugangskontrollen zum Schutz des Firmennetzwerks.

9. **Datensparsamkeit**
   - **Definition**: Das Prinzip, nur die minimal erforderlichen personenbezogenen Daten zu erheben und zu verarbeiten.
   - **Beispiel**: Bei der Registrierung eines neuen Dienstes werden nur notwendige Informationen wie E-Mail-Adresse und Passwort erfasst.

10. **DatenSpeicherung**
    - **Definition**: Die sichere Speicherung von Daten in einer Umgebung, die vor Datenverlust oder unbefugtem Zugriff schützt.
    - **Beispiel**: Verwendung von verschlüsselten Cloud-Speicherdiensten zur Speicherung von Benutzerdaten-Backups.

---

## Aufgabe 2: Fallstudie zum Datenschutz - Gesundheits-App "FitTrack Pro"

### 1. Identifizierung persönlicher und sensibler Daten

In der "FitTrack Pro"-App werden folgende Daten gesammelt:

- **Name**: Direkt mit der Identität einer Person verbunden und gilt als personenbezogene Daten.
- **Alter**: Zwar keine direkten Identifikationsinformationen, aber in Kombination mit anderen Daten kann die Identität einer Person ermittelt werden, daher ebenfalls personenbezogene Daten.
- **Gesundheitsdaten (Herzfrequenz, Schlafdauer)**: Betreffen die Gesundheitszustände einer Person und gelten als sensible Daten.
- **Positionsdaten**: Zur Verfolgung von Aktivitäten genutzt, können sie die täglichen Gewohnheiten und Bewegungsmuster einer Person offenlegen und sind somit personenbezogene Daten.

### 2. Anwendbarkeit von Anonymisierung und Pseudonymisierung

- **Anonymisierung**: In "FitTrack Pro" könnte eine vollständige Anonymisierung nicht realistisch sein, da die App personalisierte Gesundheitsberichte generieren muss, die normalerweise mit der Benutzeridentität verknüpft sind. Es kann jedoch durch Entfernen direkter Identifikationsinformationen (wie Name) teilweise anonymisiert werden.

- **Pseudonymisierung**: Besser geeignet, indem Benutzer-ID oder virtuelle Identitäten anstelle der echten Namen und anderer direkter Identifikationsinformationen verwendet werden. Zum Beispiel werden die Gesundheitsdaten eines Benutzers mit einer zufällig generierten Benutzer-ID verknüpft, um die Datenverwendbarkeit zu gewährleisten und gleichzeitig die Privatsphäre zu schützen.

### 3. Implementierungsmethoden

- **Datenverschlüsselung**: Während der Datenübertragung und -speicherung SSL/TLS-Verschlüsselungstechniken verwenden, um zu verhindern, dass Daten während der Übertragung abgefangen werden.

- **Verwendung von Benutzer-IDs**: Anstelle von echten Namen, um sicherzustellen, dass Datenanalysen und -verarbeitungen nicht direkt mit der Identität einer Person verknüpft sind.

- **Zugangskontrollen für Daten**: Beschränken Sie den Zugriff auf sensible Daten nur auf autorisierte App-Komponenten und -Personen, um das Risiko von Datenlecks zu verringern.

- **Anonymisierte Verarbeitung**: Entfernen oder Verschleiern direkter persönlicher Identifikationsinformationen bei der Datenfreigabe oder -analyse, um sicherzustellen, dass Datensätze nicht auf spezifische Personen zurückgeführt werden können.

### 4. Gesetzeskonformität

Gemäß der Datenschutz-Grundverordnung (DSGVO) müssen bei der Verarbeitung personenbezogener und sensibler Daten folgende Punkte beachtet werden:

- **Rechtmäßigkeit**: Daten dürfen nur auf gesetzlicher Grundlage, wie Einwilligung des Benutzers oder Vertragserfüllung, erhoben und verarbeitet werden.
- **Transparenz**: Benutzer müssen klar darüber informiert werden, welche Daten gesammelt werden, wie sie verwendet und wie sie geschützt werden.
- **Datenminimierung**: Es dürfen nur die minimal erforderlichen Daten für die App-Funktionalität erhoben und verarbeitet werden.
- **Sicherheit**: Angemessene technische und organisatorische Maßnahmen müssen ergriffen werden, um die Datensicherheit zu gewährleisten und unbefugten Zugriff oder Datenlecks zu verhindern.

Durch die Implementierung von Anonymisierungs- und Pseudonymisierungstechniken kann "FitTrack Pro" personalisierte Dienste anbieten und gleichzeitig die Privatsphäre und Datensicherheit der Benutzer gewährleisten, um den Anforderungen der DSGVO zu entsprechen.

---

## Fazit

In der "FitTrack Pro"-Gesundheits-App kann durch die sinnvolle Anwendung von Anonymisierungs- und Pseudonymisierungstechniken ein Gleichgewicht zwischen dem Schutz der Privatsphäre der Benutzer und der Bereitstellung personalisierter Dienste gefunden werden. Durch die Sicherstellung der sicheren Speicherung und Übertragung von Daten sowie die Einhaltung von Datenschutzvorschriften wird nicht nur das Vertrauen der Benutzer gestärkt, sondern auch die Compliance und soziale Verantwortung des Unternehmens gewährleistet.

---
