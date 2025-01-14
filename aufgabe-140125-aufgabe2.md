## 2.1 Was genau ist eine Subnetzmaske?

Eine Subnetzmaske ist eine 32-Bit-Zahl, die verwendet wird, um ein IP-Netzwerk in Subnetze zu unterteilen und den Bereich der IP-Adressen zu definieren, die einem bestimmten Netzwerk oder Subnetz zugeordnet sind. Sie besteht aus einer Sequenz von Einsen (1) gefolgt von Nullen (0). Die Einsen markieren den Netzwerkteil der Adresse, während die Nullen den Hostteil der Adresse markieren.

**Beispiel:**
- IP-Adresse: 192.168.1.10
- Subnetzmaske: 255.255.255.0

Diese Subnetzmaske (255.255.255.0) bedeutet, dass die ersten 24 Bits (255.255.255) für das Netzwerk verwendet werden und die letzten 8 Bits (0) für die Hostadressen im Netzwerk.

## 2.2 Wie funktioniert das Routing, wenn ich eine Adresse außerhalb meines Subnetzes erreichen möchte?

Wenn ein Gerät eine Adresse außerhalb seines Subnetzes erreichen möchte, verwendet es ein Gateway (meistens ein Router), um die Daten an das Zielnetzwerk weiterzuleiten. Das Gerät sendet die Datenpakete an das Standard-Gateway, das in den Netzwerkeinstellungen konfiguriert ist.

**Der Prozess läuft wie folgt ab:**
1. **Routing-Tabelle prüfen**: Das Gerät prüft seine eigene Routing-Tabelle, um zu sehen, ob es eine spezifische Route zum Zielnetzwerk hat. Wenn nicht, wird das Standard-Gateway verwendet.
2. **Paketweiterleitung**: Das Gerät sendet das Datenpaket an das Standard-Gateway.
3. **Gateway-Routing**: Das Gateway (Router) überprüft seine eigene Routing-Tabelle und leitet das Paket an das nächste Netzwerk weiter, das näher an das Zielnetzwerk liegt.
4. **Zwischenrouter**: Das Paket kann durch mehrere Router geleitet werden, wobei jeder Router seine Routing-Tabelle verwendet, um den besten nächsten Hop zu bestimmen.
5. **Zielnetzwerk erreichen**: Schließlich erreicht das Paket das Zielnetzwerk, und der letzte Router leitet das Paket an das endgültige Zielgerät weiter.

Dieser Prozess stellt sicher, dass Datenpakete effizient von einem Netzwerk zum anderen geleitet werden, bis sie ihr endgültiges Ziel erreichen.