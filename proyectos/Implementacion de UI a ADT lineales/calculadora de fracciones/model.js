// ======== Fracciones ========
function parseFrac(str) {
    let [num, den] = str.split("/").map(Number);
    return { num, den };
}

function operarFracciones(f1, f2, op) {
    let n1 = f1.num, d1 = f1.den;
    let n2 = f2.num, d2 = f2.den;
    let num, den;

    switch (op) {
        case "+": num = n1*d2 + n2*d1; den = d1*d2; break;
        case "-": num = n1*d2 - n2*d1; den = d1*d2; break;
        case "*": num = n1*n2; den = d1*d2; break;
        case "/": num = n1*d2; den = d1*n2; break;
    }
    return `${num}/${den}`;
}

// ======== Conjuntos ========
function strToSet(str) {
    return new Set(str.split(",").map(Number));
}

function operarConjuntos(c1, c2, op) {
    let res = new Set();

    if (op === "union") {
    c1.forEach(x => res.add(x));
    c2.forEach(x => res.add(x));
    } else if (op === "inter") {
    c1.forEach(x => { if (c2.has(x)) res.add(x); });
    } else if (op === "dif") {
    c1.forEach(x => { if (!c2.has(x)) res.add(x); });
    }

    return Array.from(res).join(", ");
}

// ======== Polinomios ========
function strToPoly(str) {
    return str.split(",").map(Number);
}

function sumarPolinomios(p1, p2) {
    let n = Math.max(p1.length, p2.length);
    let res = Array(n).fill(0);
    for (let i = 0; i < n; i++) {
    res[i] = (p1[i] || 0) + (p2[i] || 0);
    }
    return res;
}

function multiplicarPolinomios(p1, p2) {
    let res = Array(p1.length + p2.length - 1).fill(0);
    for (let i = 0; i < p1.length; i++) {
        for (let j = 0; j < p2.length; j++) {
        res[i+j] += p1[i]*p2[j];
        }
    }
    return res;
}

function polyToStr(p) {
    return p.map((coef, i) => `${coef}x^${p.length-1-i}`).join(" + ");
}
