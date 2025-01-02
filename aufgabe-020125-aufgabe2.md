# Aufgabe 2 Pseudocode

Begin
    imput a
    imput b
    defenition count_ungerade = 0
    defenition sum_ungerade = 0

    if a > b then
        Swap a, b
    endif

    for i from a to b do
        if i mod 2 != 0 then
            count_ungerade = count_ungerade + 1
            sum_ungerade = sum_ungerade + i
        endif
    endfor

    output "Anzahl der ungeraden Zahlen: ", count_ungerade
    output "Summe der ungeraden Zahlen: ", sum_ungerade
End