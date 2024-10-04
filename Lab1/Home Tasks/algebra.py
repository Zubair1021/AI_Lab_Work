class Expression:
    pass

class Sum(list, Expression):
    def _repr_(self):
        return "Sum(%s)" % list._repr_(self)

    def simplify(self):
        # Flatten nested sums to handle the associative law
        terms = self.flatten()
        # Recursively simplify each term
        simplified_terms = [simplify_if_possible(term) for term in terms]
        return Sum(simplified_terms)

    def flatten(self):
        # Flatten nested sums
        terms = []
        for term in self:
            if isinstance(term, Sum):
                terms += term.flatten()
            else:
                terms.append(term)
        return terms


class Product(list, Expression):
    def _repr_(self):
        return "Product(%s)" % list._repr_(self)

    def simplify(self):
        # Flatten nested products to handle the associative law
        factors = self.flatten()
        # Recursively simplify each factor
        simplified_factors = [simplify_if_possible(factor) for factor in factors]
        return Product(simplified_factors)

    def flatten(self):
        # Flatten nested products
        factors = []
        for factor in self:
            if isinstance(factor, Product):
                factors += factor.flatten()
            else:
                factors.append(factor)
        return factors


def simplify_if_possible(expr):
    if isinstance(expr, Expression):
        return expr.simplify()
    else:
        return expr


def multiply(expr1, expr2):
    if not isinstance(expr1, Expression):
        expr1 = Product([expr1])
    if not isinstance(expr2, Expression):
        expr2 = Product([expr2])
    return do_multiply(expr1, expr2)


def do_multiply(expr1, expr2):
    expr1 = simplify_if_possible(expr1)
    expr2 = simplify_if_possible(expr2)

    # Case 1: Both expr1 and expr2 are Sums (Distributive law)
    if isinstance(expr1, Sum) and isinstance(expr2, Sum):
        result_terms = []
        for term1 in expr1:
            for term2 in expr2:
                result_terms.append(Product([term1, term2]))
        return Sum(result_terms).simplify()

    # Case 2: expr1 is a Sum and expr2 is a Product (Distributive law)
    elif isinstance(expr1, Sum) and isinstance(expr2, Product):
        result_terms = []
        for term in expr1:
            result_terms.append(Product([term, expr2]))
        return Sum(result_terms).simplify()

    # Case 3: expr1 is a Product and expr2 is a Sum (Distributive law)
    elif isinstance(expr1, Product) and isinstance(expr2, Sum):
        result_terms = []
        for term in expr2:
            result_terms.append(Product([expr1, term]))
        return Sum(result_terms).simplify()

    # Case 4: Both expr1 and expr2 are Products (Combine factors)
    elif isinstance(expr1, Product) and isinstance(expr2, Product):
        combined_product = Product(expr1 + expr2)
        return combined_product.simplify()

    else:
        raise TypeError("Unexpected types in do_multiply")


if __name__ == '__main__':
    expr1 = Sum([1, 2])
    expr2 = Sum([3, 4])
    result = multiply(expr1, expr2)
    print("The Result is \n\t",result) 