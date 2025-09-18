//Controlador
function calcular() {
    const f1Input = document.getElementById("f1").value;
    const f2Input = document.getElementById("f2").value;
    const op = document.getElementById("op").value;
    const res = document.getElementById("res");

    try {
        const f1 = Fraction.fromString(f1Input);
        const f2 = Fraction.fromString(f2Input);

    let r;
    switch(op) {
        case "+": r = f1.add(f2); break;
        case "-": r = f1.subtract(f2); break;
        case "*": r = f1.multiply(f2); break;
        case "/": r = f1.divide(f2); break;
    }

    res.innerHTML = `
        <p><b>Resultado:</b> ${r.toString()}</p>
        <p><b>Decimal:</b> ${r.toDecimal()}</p>
    `;
    } catch(e) {
        res.innerHTML = `<p style="color:red;">Error: ${e.message}</p>`;
    }
}