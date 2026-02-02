class MyNumMatrix:
    def __init__(self, rows):
        """rows should look like [[a, b, c], [d, e, f], [g, h, i]]"""
        # TODO step 1 : verify rows has length 3
        if len(rows) != 3:
            raise ValueError("input must have exactly 3 rows.")

       # TODO step 2: verify each row has length 3
        for x in rows:
            if len(x) != 3:
                raise ValueError("matrix must have exactly 3 columns")
            # TODO step 3: verify each entry is int or float
            for val in x:
                    if not isinstance(val, (int, float)):
                        raise TypeError("values must be int or float")
            
        # TODO step 4: assign self.values and self.shape
        self.values = rows
        self.shape = (3, 3)

    def __str__(self):
        return str(self.values)

    def  multiply(self, other):
        if self.shape != other.shape:
             raise ValueError("matrices must be 3x3")

        other_cols = list(zip(*other.values))
        product = [
            [sum(a * b for a, b in zip(row_a, col_b)) for col_b in other_cols]
            for row_a in self.values
        ]
        
        return MyNumMatrix(product)

# Minimal test harness
if __name__ == "__main__":
    m1 = MyNumMatrix([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])
    m2 = MyNumMatrix([[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]])
    print("Product:", m1.multiply(m2))  # expected [[30, 24, 18], [84, 69, 54], [138, 114, 90]]
