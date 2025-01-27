# Aufgabe

## Frage 1
>   ○ Mit dem Befehl iptables kannst du auf Ubuntu Firewall Regeln konfigurieren.
>   Lasse dir einmal mit ``sudo iptables -S`` die im Moment aufgestellten firewall Regeln für dein WSL anzeigen.
## Antworte 1
    -P INPUT ACCEPT
    -P FORWARD ACCEPT
    -P OUTPUT ACCEPT

## Frage 2
> ○ Es sollten durch den vorherigen Befehl drei Zeilen angezeigt werden: Was bedeutet jede davon?
## Antworte 2
    -P INPUT ACCEPT：Setzt die Standardrichtlinie der INPUT-Kette auf ACCEPT, d.h. standardmäßig werden alle eingehenden Datenpakete akzeptiert.

    -P FORWARD ACCEPT：Setzt die Standardrichtlinie der FORWARD-Kette auf ACCEPT, d.h. standardmäßig werden alle weitergeleiteten Datenpakete akzeptiert. Dies wird normalerweise für Gateways oder Router verwendet, um Datenpakete weiterzuleiten.

    -P OUTPUT ACCEPT：Setzt die Standardrichtlinie der OUTPUT-Kette auf ACCEPT, d.h. standardmäßig werden alle ausgehenden Datenpakete akzeptiert.

    Diese Befehle zeigen, dass das System standardmäßig alle eingehenden, ausgehenden und weitergeleiteten Datenpakete akzeptiert. Diese Konfiguration ist in Bezug auf die Sicherheit relativ locker und wird häufig vor der Festlegung spezifischer Regeln verwendet.

## Frage 3
> ○ Mit dem Befehl curl kannst du HTTP anfragen direkt von der Konsole aus senden. Gib einmal ``curl example.com`` ein und sehe, wie der HTML code der website example.com auf der Konsole ausgegeben wird (du kannst sie auch mal im Browser ansehen und vergleichen, ob du etwas wiedererkennst)
## Antworte 3
    Wir können voll html-code example.com sehen. mit <hard> <body> css...

## Frage 4
> ○ Nun blockieren wir den ausgehenden Verkehr auf port 80 (port 80 wird für HTTP verkehr genutzt):
``sudo iptables -A OUTPUT -p tcp --dport 80 -j DROP``

## Antworte 4
    Chain OUTPUT (policy ACCEPT)
    target     prot opt source         destination
    DROP       tcp  --  anywhere       anywhere          tcp dpt:http

## Frage 5
> ○ Analysiere diesen Befehl, recherchiere was die Optionen machen und gib im Detail an was welche Funktion übernimmt

## Antworte 5
    Dieser Befehl blockiert den ausgehenden Verkehr auf port 80. Und port 80 reserviert für HTTP, deshalb ist http betroffen.

## Frage 6
> ○ Benutze nun erneut ``curl example.com``. Was ist deine Beobachtung?

## Antworte 6
    Wird in der Befehlszeile nicht angezeigt.

## Frage 7
> ○ Kannst du mit deinem unter Windows installierten Browser noch auf das example.com zugreifen? Warum/Warum nicht?

## Antworte 7
    Wenn du den Port 80 in WSL blockierst, wird dies nur die Netzwerkverbindung in der WSL-Umgebung beeinflussen und nicht direkt die Netzwerkverbindung von Windows 11. Daher kannst du auch dann, wenn der Port 80 in WSL blockiert ist, weiterhin auf Websites in Windows 11 zugreifen.

    Konkret gesagt, sind die Netzwerkstacks von WSL und Windows 11 relativ unabhängig voneinander. Das Blockieren des Ports 80 in WSL verhindert nur das Senden oder Empfangen von HTTP-Anfragen aus WSL heraus, hat jedoch keine Auswirkungen auf den Zugriff auf das Internet über den Browser oder andere Anwendungen in Windows 11.

## Frage 8
    ○ Nun blockieren wir port 5000 für eingehende Anfragen: ``sudo iptables -A INPUT -p tcp --dport 5000 -j DROP``

## Antworte 8
    Chain INPUT (policy ACCEPT)
    target     prot opt source         destination
    DROP       tcp  --  anywhere       anywhere          tcp dpt:5000

## Frage 9
○ Gib auch für diesen Befehl im Detail an, was passiert. Allerdings nicht so genau, falls du parallelen/unterschiede zum ersten Befehl ziehen kannst.

## Antworte 9
    Dieser Befehl blockiert den eingehenden Verkehr auf port 5000.

## Frage 10
> ○ Starte nun einen beliebigen Flask Server der letzten Woche und versuche ihn über den Browser zu erreichen (localhost:5000). Was ist deine Beobachtung?

## Amtworte 10
    Die Netzwerkstacks sind von WSL und Windows 11 relativ unabhängig voneinander. Ich kann über den Browser `` Flask Server`` erreichen.

## Frage 11
> ○ Benutze nun ``sudo iptables -L --line-numbers`` um dir die Regeln mitsamt ihrer Regelnummern anzeigen zu lassen

## Antwort 11
    weisong@Key:~$ sudo iptables -L --line-numbers
    Chain INPUT (policy ACCEPT)
    num  target     prot opt source         destination
    1    DROP       tcp  --  anywhere       anywhere     tcp dpt:5000

    Chain FORWARD (policy ACCEPT)
    num  target     prot opt source         destination

    Chain OUTPUT (policy ACCEPT)
    num  target     prot opt source         destination
    1    DROP       tcp  --  anywhere       anywhere     tcp dpt:http
    2    DROP       tcp  --  anywhere       anywhere     tcp dpt:5000
## Frage 12
> ○ Lösche die Regeln wieder mit ``sudo iptables -D INPUT <Nummer>`` bzw ``sudo iptables -D OUTPUT <Nummer>``. Ersetze <Nummer> mit der tatsächlichen Regelnummer

## Antworte 12

    weisong@Key:~$ sudo iptables -D OUTPUT 2
    weisong@Key:~$ sudo iptables -L --line-numbers
    Chain INPUT (policy ACCEPT)
    num  target     prot opt source          destination
    1    DROP       tcp  --  anywhere        anywhere    tcp dpt:5000

    Chain FORWARD (policy ACCEPT)
    num  target     prot opt source          destination

    Chain OUTPUT (policy ACCEPT)
    num  target     prot opt source          destination
    1    DROP       tcp  --  anywhere        anywhere    tcp dpt:http

## Frage 13
> ○ Vergewissere dich mit ``sudo iptables -S``, dass alles so eingestellt ist wie vorher

## Antworte 13
    -P INPUT ACCEPT
    -P FORWARD ACCEPT
    -P OUTPUT ACCEPT