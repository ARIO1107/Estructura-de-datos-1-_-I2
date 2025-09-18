// Modelo
class Fraction {
    constructor(n, d) {
        if (d === 0) throw new Error("El denominador no puede ser 0");
        this.n = n;
        this.d = d;
        this.simplify();
    }

    static fromString(str) {
        let [n, d] = str.split('/').map(Number);
        if (isNaN(n) || isNaN(d)) throw new Error("Formato inválido (usa a/b)");
        return new Fraction(n, d);
    }

    static gcd(a, b) {
        return b ? Fraction.gcd(b, a % b) : a;
    }

    simplify() {
        let g = Fraction.gcd(Math.abs(this.n), Math.abs(this.d));
        this.n /= g;
        this.d /= g;
        if (this.d < 0) { this.n *= -1; this.d *= -1; }
    }

    add(other) {
        return new Fraction(this.n * other.d + other.n * this.d, this.d * other.d);
    }
    subtract(other) {
        return new Fraction(this.n * other.d - other.n * this.d, this.d * other.d);
    }
    multiply(other) {
        return new Fraction(this.n * other.n, this.d * other.d);
    }
    divide(other) {
        if (other.n === 0) throw new Error("División por cero");
        return new Fraction(this.n * other.d, this.d * other.n);
    }
        toString() {
        return `${this.n}/${this.d}`;
    }
        toDecimal() {
        return (this.n / this.d).toFixed(4); // 4 decimales
    }
}
