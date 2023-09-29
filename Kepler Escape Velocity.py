# G is Gravitational constant
G = 6.67430 * (10**-11)
# M is mass of body
M_earth = 5.9722 * (10**24)
M_kepler = 5 * M_earth
# r is radus
r_earth = 3958.8
r_kepler = 1.5 * r_earth
v_earth = ((2*G*M_earth)/r_earth)**0.5
v_kepler = ((2*G*M_kepler)/r_kepler)**0.5
print(v_earth)
print(v_kepler)
print(v_kepler/v_earth)
print(f"v_earth:{v_earth}, v_kepler:{v_kepler}, ratio:{v_kepler/v_earth}")