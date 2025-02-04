# Datensicherheit

## Aufgabe 1 DSGVO

Die Datenschutz-Grundverordnung (DSGVO) ist ein umfassendes Datenschutzgesetz der Europäischen Union, das im Mai 2018 in Kraft getreten ist. Es wurde entwickelt, um die personenbezogenen Daten von EU-Bürgern zu schützen und gilt für alle Organisationen, die solche Daten verarbeiten, unabhängig von ihrem Standort. Die DSGVO basiert auf sieben Grundsätzen, die sicherstellen, dass personenbezogene Daten rechtmäßig, fair und transparent verarbeitet werden. Hier ist eine Erklärung der einzelnen Prinzipien in einfachen Worten, zusammen mit Beispielen, die ihre Anwendung veranschaulichen:

1. **Rechtmäßigkeit, Verarbeitung nach Treu und Glauben, Transparenz**
   - **Rechtmäßigkeit**: Organisationen müssen einen gültigen rechtlichen Grund für die Erhebung und Verarbeitung personenbezogener Daten haben. Dies könnte die Einwilligung der betroffenen Person, eine vertragliche Notwendigkeit oder die Erfüllung einer gesetzlichen Verpflichtung sein.
   - **Fairness**: Daten sollten auf ehrliche und offene Weise erhoben werden. Die betroffenen Personen sollten nicht darüber in die Irre geführt werden, wie ihre Daten verwendet werden.
   - **Transparenz**: Organisationen müssen klar und transparent über ihre Datenverarbeitungsaktivitäten informieren. Sie sollten leicht zugängliche Informationen darüber bereitstellen, welche Daten gesammelt werden, wie sie verwendet werden und mit wem sie geteilt werden.

   *Beispiel*: Ein Unternehmen muss die Benutzer über die auf seiner Website verwendeten Cookies informieren und ihre Zustimmung einholen, bevor persönliche Daten über diese Cookies erhoben werden.

2. **Zweckbindung**
   - Personenbezogene Daten müssen für spezifische, legitime Zwecke erhoben und dürfen ohne die Einwilligung der betroffenen Person nicht für andere Zwecke verwendet werden. Dies stellt sicher, dass Daten nicht missbraucht oder unangemessen weitergegeben werden.

   *Beispiel*: Wenn Sie einem Einzelhändler Ihre E-Mail-Adresse geben, um einen Newsletter zu erhalten, darf der Einzelhändler diese E-Mail-Adresse nicht ohne Ihre ausdrückliche Zustimmung für Marketingkampagnen anderer Unternehmen verwenden.

3. **Datenminimierung**
   - Es sollten nur die notwendigen personenbezogenen Daten für den beabsichtigten Zweck erhoben werden. Dies verringert das Risiko einer übermäßigen Datenerhebung und eines Missbrauchs.

   *Beispiel*: Bei der Erstellung eines Kontos auf einer sozialen Medienplattform sollten nur wesentliche Informationen wie Ihr Name und Ihre E-Mail-Adresse abgefragt werden. Zusätzliche Informationen wie Ihre Telefonnummer oder Adresse sollten nur angefordert werden, wenn dies für den Dienst erforderlich ist.

4. **Richtigkeit**
   - Personenbezogene Daten müssen genau und auf dem neuesten Stand sein. Organisationen sind dafür verantwortlich, sicherzustellen, dass die von ihnen gespeicherten Daten korrekt sind, und bei Feststellung von Ungenauigkeiten Korrekturen vorzunehmen.

   *Beispiel*: Wenn Sie Ihre Adresse ändern, sollte eine Online-Shopping-Plattform Ihre Adresse in ihren Unterlagen aktualisieren, um eine genaue Zustellung Ihrer Bestellungen zu gewährleisten.

5. **Speicherbegrenzung**
   - Personenbezogene Daten sollten nicht länger als nötig aufbewahrt werden. Sobald der Zweck, für den die Daten erhoben wurden, erfüllt ist, sollten die Daten sicher gelöscht oder anonymisiert werden.

   *Beispiel*: Wenn Sie Ihr Abonnement für einen Dienst kündigen, sollte der Anbieter Ihre personenbezogenen Daten löschen, es sei denn, er ist gesetzlich verpflichtet, diese für einen bestimmten Zeitraum aufzubewahren.

6. **Integrität und Vertraulichkeit**
   - Personenbezogene Daten müssen vor unbefugtem Zugriff, versehentlichem Verlust, Zerstörung oder Beschädigung geschützt werden. Dies umfasst die Implementierung geeigneter technischer und organisatorischer Maßnahmen zur Gewährleistung der Datensicherheit.

   *Beispiel*: Ein Unternehmen sollte Verschlüsselung verwenden, um sensible Kundendaten während der Übertragung und Speicherung zu schützen und sicherzustellen, dass nur autorisiertes Personal Zugriff darauf hat.

7. **Rechenschaftspflicht**
   - Organisationen müssen in der Lage sein, die Einhaltung der DSGVO-Grundsätze nachzuweisen. Dies umfasst die Erstellung geeigneter Richtlinien, Verfahren und Dokumentationen, um zu zeigen, dass Daten rechtmäßig verarbeitet werden.

   *Beispiel*: Ein Unternehmen muss Aufzeichnungen über Datenverarbeitungsaktivitäten führen, einschließlich der gesammelten Daten, der Gründe für die Erhebung und der Art und Weise, wie sie weitergegeben werden. Diese Dokumentation kann von den Behörden überprüft werden, um die Einhaltung der DSGVO sicherzustellen.

Zusammenfassend lässt sich sagen, dass die sieben Prinzipien der DSGVO zusammenwirken, um sicherzustellen, dass personenbezogene Daten verantwortungsbewusst und ethisch verarbeitet werden. Durch die Einhaltung dieser Prinzipien können Organisationen das Vertrauen der Einzelpersonen gewinnen und potenzielle rechtliche Konsequenzen aufgrund von Nichtkonformität vermeiden.

---

## Aufgabe 2 Datensicherheit

---
   ![SSL](./images/Screenshot%202025-02-04%20171452.png)

   ![SSL](./images/Screenshot%202025-02-04%20171619.png)

---
   > warum diese Methode ``unsicherer`` ist als eine Verschlüsselung mit einem zufälligen SSL-Key.

      - Verwenden Sie eine zufällig generierte SSL-Verschlüsselung, da diese auf einem sicheren Zufallsprozess basiert, was die Wahrscheinlichkeit eines Bruchs erheblich verringert. Im Gegensatz dazu kann eine symmetrische Verschlüsselung mit einem nicht zufälligen Schlüssel anfälliger für Angriffe sein, da der Schlüssel voraussehbarer ist.

---
● Warum wird für die Verschlüsselung ein „Salt“ hinzugefügt?

      Bei der Verwendung von OpenSSL zur Verschlüsselung wird der Salt-Parameter hauptsächlich hinzugefügt, um die Sicherheit der Verschlüsselung zu erhöhen. Konkret ist Salt eine Art von Zufallsdaten, die zusammen mit dem Passwort verwendet werden, um den Verschlüsselungsschlüssel durch eine Key-Derivation-Funktion zu generieren. Diese Methode bietet mehrere wichtige Vorteile:

      1. **Verhindert die Generierung des gleichen Schlüssels mit demselben Passwort**: Selbst wenn dasselbe Passwort verwendet wird, wird durch die Salzzugabe jedes Mal ein anderer Schlüssel generiert, wodurch die Sicherheit der Verschlüsselung erhöht wird und verhindert wird, dass Angreifer denselben Schlüssel verwenden, um mehrere Dateien zu entschlüsseln.
         
      2. **Erhöht die Schwierigkeit des Brute-Force-Angriffs**: Aufgrund des Vorhandenseins von Salt muss ein Angreifer, selbst wenn er das Passwort kennt oder errät, auch den entsprechenden Salt-Wert kennen, um den richtigen Schlüssel zu generieren. Zufällige und einzigartige Salt-Werte erschweren Brute-Force-Angriffe erheblich.
         
      3. **Erhöht die Zufälligkeit und Komplexität des Schlüssels**: Durch die Kombination von Salt und Passwort wird der generierte Schlüssel zufälliger und komplexer, wodurch das Risiko eines erfolgreichen Angriffs verringert wird.
         
      4. **Unterstützt sicherere Key-Derivation-Methoden**: Moderne Key-Derivation-Funktionen wie PBKDF2 verwenden durch mehrfache Iterationen des Hash-Funktions und die Kombination mit Salt stärkere Schlüssel, was die Sicherheit der Verschlüsselung weiter erhöht.

   Zusammenfassend lässt sich sagen, dass die Verwendung des Salt-Parameters im OpenSSL-Verschlüsselungsprozess die Sicherheit der Verschlüsselung effektiv erhöht, Sicherheitslücken durch wiederholte Schlüssel oder einfache Passwörter verhindert und mit modernen Key-Derivation-Methoden einen sichereren Verschlüsselungsprozess gewährleistet, der den modernen Anforderungen der Informationssicherheit entspricht.

   ---

● Was passiert, wenn der symmetrische Schlüssel verloren geht?

   > Daten nicht zugänglich:

      Auswirkungen: Ein symmetrischer Schlüssel ist der einzige Schlüssel für die Verschlüsselung und Entschlüsselung. Wenn der Schlüssel verloren geht, kann auf die verschlüsselten Daten nicht zugegriffen werden, was zu Datenverlust führt.

      Lösung: Stellen Sie sicher, dass Sie Backups haben oder verwenden Sie ein Schlüsselverwaltungssystem wie Hardware-Sicherheitsmodule (HSM) oder Cloud-Schlüsselverwaltungsdienste, um Schlüssel zu speichern und zu verwalten.

---
