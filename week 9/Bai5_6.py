class Polynomial:
    def __init__(self, coeffs: list):
        self.coeffs = list(coeffs)

    def __str__(self):
        n = len(self.coeffs)
        terms = []

        for i, coef in enumerate(self.coeffs):
            if coef == 0:
                continue

            power = n - i - 1
            abs_coef = abs(coef)

            # Tạo phần biến
            if power == 0:
                term = f"{abs_coef}"
            elif power == 1:
                if abs_coef == 1:
                    term = "x"
                else:
                    term = f"{abs_coef}x"
            else:
                if abs_coef == 1:
                    term = f"x^{power}"
                else:
                    term = f"{abs_coef}x^{power}"

            # Thêm dấu
            if not terms:
                if coef < 0:
                    terms.append(f"-{term}")
                else:
                    terms.append(term)
            else:
                if coef < 0:
                    terms.append(f"- {term}")
                else:
                    terms.append(f"+ {term}")

        return " ".join(terms) if terms else "0"

    def __call__(self, x):
        result = 0
        for coef in self.coeffs:
            result = result * x + coef
        return result

    def __add__(self, other):
        a = self.coeffs[:]
        b = other.coeffs[:]

        if len(a) < len(b):
            a = [0] * (len(b) - len(a)) + a
        elif len(b) < len(a):
            b = [0] * (len(a) - len(b)) + b

        result = [a[i] + b[i] for i in range(len(a))]
        return Polynomial(result)
