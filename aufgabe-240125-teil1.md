# Aufgabe 1

> Ich bin ein nutzer der eBay.de.

- Anfrage   „Als Nutzer möchte ich mit meine ``Username`` und ``Password`` anmelden.“
    Flow:
        1. Nutzer wählt ``Anmeldung`` im Interface aus.
        2. Frontend sender API-Reguest: POST /user/singin
        3. Server verarbeitet die Anfrage:
            - Überprüft die Userliste und das Passwort.
            - Wenn richtig:
                - Server sendet eine Erfolgsmeldung und einen Authentifizierungstoken zurück.
                - Nutzer wird zum Dashboard weitergeleitet.
            - Wenn falsch:
                - Server sendet eine Fehlermeldung zurück.
                - Nutzer bleibt auf der Anmeldeseite und sieht eine Fehlermeldung.

- Anfrage  „Als Nutzer möchte ich nach Produkten mit einem bestimmten Keyword suchen (z. B. ‘Handy’).“
    Flow:
            1. Nutzer gibt ein Keyword in das Suchfeld ein.
            2. Frontend sendet API-Request: GET /products/search?keyword=Handy
            3. Server verarbeitet die Anfrage:
                - Durchsucht die Produktdatenbank nach dem Keyword.
                - Sendet die Suchergebnisse zurück.
            4. Frontend zeigt die Suchergebnisse an.

- Anfrage  „Als Nutzer möchte ich Produkte in einer bestimmten Preisspanne angezeigt bekommen (z. B. zwischen 10 und 50 Euro).“
    Flow:
        1. Nutzer gibt die Preisspanne in das Suchfeld ein.
        2. Frontend sendet API-Request: GET /products/search?min_price=10&max_price=50
        3. Server verarbeitet die Anfrage:
            - Durchsucht die Produktdatenbank nach Produkten in der angegebenen Preisspanne.
            - Sendet die Suchergebnisse zurück.
        4. Frontend zeigt die Suchergebnisse an.

- Anfrage  „Als Nutzer möchte ich meine gespeicherten Artikel im Warenkorb anzeigen lassen.“
     Flow:
        1. Nutzer wählt `Warenkorb` im Interface aus.
        2. Frontend sendet API-Request: GET /user/cart
        3. Server verarbeitet die Anfrage:
            - Überprüft die gespeicherten Artikel im Warenkorb des Nutzers.
            - Sendet die Artikelinformationen zurück.
        4. Frontend zeigt die Artikel im Warenkorb an.

- Anfrage  „Als Nutzer möchte ich meine gespeicherten Artikel vom Warenkorb löschen lassen.“
    Flow:
        1. Nutzer wählt `Warenkorb` im Interface aus.
        2. Nutzer wählt die zu löschenden Artikel aus und klickt auf `Löschen`.
        3. Frontend sendet API-Request: DELETE /user/cart
        4. Server verarbeitet die Anfrage:
            - Entfernt die ausgewählten Artikel aus dem Warenkorb des Nutzers.
            - Sendet eine Erfolgsmeldung zurück.
        5. Frontend aktualisiert die Warenkorbanzeige und zeigt die verbleibenden Artikel an.