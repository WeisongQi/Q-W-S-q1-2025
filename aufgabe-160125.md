Wenn ihr euch in einem Heimnetzwerk befindet und die Webseite https://example.com aufrufen möchtet, könnt ihr diesen Vorgang wie folgt beschreiben:

DNS-Abfrage: Euer Computer sendet eine DNS-Abfrage (Domain Name System) an den DNS-Server, um die IP-Adresse für example.com zu ermitteln. Der DNS-Server antwortet mit der IP-Adresse der Webseite.

Verbindungsaufbau: Euer Computer initiiert eine TCP-Verbindung (Transmission Control Protocol) mit dem Webserver unter der ermittelten IP-Adresse. Dies geschieht über den Port 443, da HTTPS (HyperText Transfer Protocol Secure) verwendet wird.

TLS-Handshake: Euer Computer und der Webserver führen einen TLS-Handshake (Transport Layer Security) durch, um eine sichere Verbindung aufzubauen. Dabei werden Zertifikate und Schlüssel ausgetauscht, um die Kommunikation zu verschlüsseln.

HTTP-Anfrage: Nach erfolgreichem TLS-Handshake sendet euer Computer eine HTTP GET-Anfrage an den Webserver, um die Webseite example.com anzufordern.

Antwort des Webservers: Der Webserver verarbeitet die Anfrage und sendet die HTML-Daten der Webseite an euren Computer zurück.

Darstellung im Browser: Euer Webbrowser erhält die HTML-Daten und rendert die Webseite, so dass ihr die Inhalte von example.com sehen könnt.

Dieser Prozess umfasst mehrere Schritte und Protokolle, die gemeinsam dafür sorgen, dass ihr sicher und effizient auf die gewünschte Webseite zugreifen könnt.

Natürlich, hier ist eine grafische Darstellung des Datenverkehrs, wenn ihr die Webseite https://example.com aus einem Heimnetzwerk aufruft und dabei die Netzwerkbegriffe verwendet, die wir kennengelernt haben:

```plaintext
Euer Computer (Client)
      |
      |--- DNS-Abfrage an DNS-Server
      |                 (Domain Name System)
      |<-- DNS-Antwort (IP-Adresse von example.com)
      |
      |--- Verbindungsaufbau über TCP
      |                 (Transmission Control Protocol)
      |
      |--- TLS-Handshake mit Webserver
      |                 (Transport Layer Security)
      |
      |--- HTTP GET-Anfrage an Webserver
      |                 (HyperText Transfer Protocol)
      |
      |<-- HTTP-Antwort mit HTML-Daten der Webseite
      |
      |--- Darstellung der Webseite im Browser
      |
Euer Heimnetzwerk (Router)
      |
      |--- NAT (Network Address Translation)
      |
      |--- Weiterleitung zum WAN (Wide Area Network)
      |
Internet
      |
      |--- Weiterleitung zum Zielnetzwerk
      |
Zielnetzwerk (Webserver von example.com)
      |
      |<-- Antwort an euren Computer
```

### Erklärung der Netzwerkbegriffe:
1. **DNS（Domain Name System）**: Wandelt den Domainnamen `example.com` in eine IP-Adresse um.
2. **TCP（Transmission Control Protocol）**: Aufbau der Verbindung mit dem Webserver über eine sichere Verbindung.
3. **TLS（Transport Layer Security）**: Verschlüsselung der Verbindung, um die Sicherheit der übertragenen Daten zu gewährleisten.
4. **HTTP（HyperText Transfer Protocol）**: Protokoll zum Senden von Anfragen und Empfangen von Webseiten-Daten.
5. **NAT（Network Address Translation）**: Übersetzung der privaten IP-Adresse eures Heimnetzwerks in eine öffentliche IP-Adresse.
6. **WAN（Wide Area Network）**: Netzwerk, das große geographische Bereiche abdeckt und das Internet umfasst.

