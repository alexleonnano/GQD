# Tight Binding Calculations for Electronic properties of graphene quantum dots

### Repo for the tight binding calculations I did for my thesis 

Includes 3 folders that correspond for the geometries used for each quantum dot and the calculations of eigenstates and local density of states.

- GQD_C Corresponds to the zigzag-edged circular geometries.
- GQD_H Corresponds to the armchair-edged circular geometries.
- GQD_T Corresponds to the triangular geometries:
    - 0 is the angle of rotation for the generation of the basis vectors and the geometry, leading to a zigzag-edged triangular geometry.
    - On a similar fashion for $\pi \over 6$ corresponds to an armchair-edged triangular geometry.

The LDOS scripts calculate the local density of states at specific points in the lattice structure and associates the corresponding energy states eigenvalues calculated via KPM Method.

Everything is done using the [pybinding package](https://docs.pybinding.site/en/stable/index.html) and some validation via green synthesis using This [article's](https://www.sciencedirect.com/science/article/abs/pii/S0008622312005088#:~:text=GQDs%20are%20graphene%20sheets%20smaller,activity%20when%20compared%20with%20GO.) method on the interrupted nucleation of graphene oxide formation using citric acid.