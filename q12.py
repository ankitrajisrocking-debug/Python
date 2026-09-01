def eigen_2x2(a, b, c, d):
    """Compute eigenvalues and eigenvectors of [[a, b], [c, d]]."""
    tr = a + d
    det = a * d - b * c
    disc = tr**2 - 4 * det

    if disc >= 0:
        sq = disc**0.5
        l1 = (tr + sq) / 2
        l2 = (tr - sq) / 2
    else:
        sq = (-disc)**0.5
        l1 = complex(tr / 2, sq / 2)
        l2 = complex(tr / 2, -sq / 2)

    def eigenvector(l):
        if b != 0:
            v = (b, l - a)
        elif c != 0:
            v = (l - d, c)
        else:
            v = (1, 0) if a == l else (0, 1)
        norm = (v[0] * (v[0].conjugate() if isinstance(v[0], complex) else v[0])
                + v[1] * (v[1].conjugate() if isinstance(v[1], complex) else v[1])) ** 0.5
        return (v[0] / norm, v[1] / norm)

    return (l1, eigenvector(l1)), (l2, eigenvector(l2))



a, b, c, d = 2, 1, 1, 2
for val, vec in eigen_2x2(a, b, c, d):
    print(f"eigenvalue: {val}, eigenvector: {vec}")
