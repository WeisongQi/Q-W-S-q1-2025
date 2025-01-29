## Aufgabe 1 Wie mache ich eine Anwendung sicher

Datenbank schützen:

    Zugriffsrechte beschränken: Stelle sicher, dass nur autorisierte Benutzer Zugriff auf die Datenbank haben. Verwende starke Passwörter und Mehr-Faktor-Authentifizierung.

    Datenverschlüsselung: Verschlüssele die gespeicherten Daten, um sicherzustellen, dass selbst bei einem Zugriff durch Unbefugte die Daten unlesbar sind.

    Firewalls: Implementiere Firewalls, um unautorisierte Zugriffe zu verhindern. Konfiguriere Firewalls so, dass sie nur spezifische IP-Adressen oder Netzwerke zulassen.

Ports schützen:

    Unnötige Ports schließen: Deaktiviere alle nicht benötigten Ports auf der Anwendung und dem Server, um die Angriffsfläche zu minimieren.

    Firewalls und Zugangskontrolllisten: Verwende Firewalls und Access Control Lists (ACLs), um den Zugriff auf bestimmte Ports zu beschränken. Nur vertrauenswürdige IP-Adressen sollten Zugriff haben.

    Intrusion Detection Systems (IDS): Implementiere IDS, um ungewöhnliche oder verdächtige Aktivitäten auf überwachten Ports zu erkennen.

Code-Sicherheit:

    Eingabeverifizierung: Stelle sicher, dass alle Benutzereingaben verifiziert werden, um SQL-Injektionen, Cross-Site Scripting (XSS) und andere Angriffe zu verhindern.

    Regelmäßige Code-Überprüfung: Führe regelmäßige Code-Überprüfungen und Sicherheits-Tests durch, um potenzielle Schwachstellen frühzeitig zu erkennen und zu beheben.

    Verwendung sicherer Bibliotheken und Frameworks: Verwende gut gewartete und sichere Bibliotheken und Frameworks, um bekannte Sicherheitsprobleme zu vermeiden.

Authentifizierung und Autorisierung:

    Starke Passwortrichtlinien: Implementiere starke Passwortrichtlinien und setze die Benutzer zur regelmäßigen Passwortänderung an.

    Mehr-Faktor-Authentifizierung (MFA): Verwende MFA, um die Sicherheit der Benutzerkonten zu erhöhen.

    Rollenbasierte Zugriffskontrolle (RBAC): Setze RBAC ein, um sicherzustellen, dass Benutzer nur auf die Ressourcen zugreifen können, die für ihre Rolle notwendig sind.

Netzwerksicherheit:

    VPN (Virtual Private Network): Nutze VPNs, um eine sichere Verbindung zwischen entfernten Benutzern und der Anwendung herzustellen.

    Sicherheits-Patches: Halte alle Systeme und Anwendungen durch regelmäßige Sicherheits-Updates auf dem neuesten Stand.

    Netzwerksegmentierung: Segmentiere das Netzwerk, um kritische Ressourcen von weniger wichtigen zu trennen und den Zugriff zu kontrollieren.

Durch die Implementierung dieser Maßnahmen kann die Sicherheit einer Anwendung deutlich verbessert werden. Es ist wichtig, regelmäßig Sicherheitsbewertungen durchzuführen und die neuesten Best Practices zu berücksichtigen, um gegen neue Bedrohungen gewappnet zu sein.


## Aufgabe 2 VM - AWS (EC2)

Schritt 1: Starten einer Instance
    - Geben Sie einen Namen für Instance ein.
    - Wählen Sie Betriebssystem aus.
    - Wählen Sie Kontingent aus.
    - Erstellen Sie basierend auf SSH ein Schlüsselpaar und speichern Sie die Schlüsseldatei.
    - Erstellen Sie Netzwerkeinstellungen
    - Nutzen Sie die Regeln von Subnetzen, um voneinander getrennte Subnetze zu erstellen und so wichtige Daten zu schützen.
    - Erstellen Sie je nach Bedarf unterschiedliche Sicherheitsgruppen.

Schritt 2: Verbindung mit der Instance herstellen

Schritt 3: Bereinigen Ihrer Instance

- Begriffe:

    Ein Image – Eine Vorlage, die die Software enthält, die auf Ihrer Instance ausgeführt werden soll, z. B. das Betriebssystem.

    Ein Schlüsselpaar – Eine Reihe von Sicherheitsanmeldeinformationen, mit denen Sie Ihre Identität nachweisen, wenn Sie sich mit Ihrer Instance verbinden. Der private Schlüssel ist auf dem lokalen Computer gespeichert und der öffentliche Schlüssel ist in der Instance gespeichert.

    Ein Netzwerk — Eine virtuelle private Cloud (VPC) ist ein virtuelles Netzwerk, das Ihrem gewidmet ist AWS-Konto. Damit Sie schnell loslegen können, verfügt Ihr Konto über ein Standard-Subnetz VPC in jedem Konto AWS-Region, und jedes Standardsubnetz VPC hat in jeder Availability Zone ein Standardsubnetz.

    Eine Sicherheitsgruppe – Dient als virtuelle Firewall zur Steuerung von ein- und ausgehendem Datenverkehr.

    Ein EBS Volume — Wir benötigen ein Root-Volume für das Image. Sie können optional Daten-Volumes hinzufügen.