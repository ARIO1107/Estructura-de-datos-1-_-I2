// ======== Fracciones ========
function calcularFraccion() {
    let f1 = parseFrac(document.getElementById("f1").value);
    let f2 = parseFrac(document.getElementById("f2").value);
    let op = document.getElementById("opFrac").value;
    let res = operarFracciones(f1, f2, op);
    document.getElementById("resFrac").innerText = "Resultado: " + res;
}

// ======== Conjuntos ========
function calcularConjunto() {
    let c1 = strToSet(document.getElementById("c1").value);
    let c2 = strToSet(document.getElementById("c2").value);
    let op = document.getElementById("opConj").value;
    let res = operarConjuntos(c1, c2, op);
    document.getElementById("resConj").innerText = "Resultado: {" + res + "}";
}

// ======== Polinomios ========
function calcularPolinomio() {
    let p1 = strToPoly(document.getElementById("p1").value);
    let p2 = strToPoly(document.getElementById("p2").value);
    let op = document.getElementById("opPol").value;
    let res;

    if (op === "suma") {
        res = sumarPolinomios(p1, p2);
    } else if (op === "multi") {
        res = multiplicarPolinomios(p1, p2);
    }

    document.getElementById("resPol").innerText = "Resultado: " + polyToStr(res);
}