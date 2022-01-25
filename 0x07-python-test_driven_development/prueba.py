
	>>> add_integer(-5,3)# si -a es mas grande que b
	-2
	>>> add_integer(5,-3)# si -b es mas pequeño q a
	2
	>>> add_integer(-3,-3)# si -a y -b son iguales
	-6
	>>> add_integer(3,-5)
	-2
	>>> add_integer('a')
    TypeError: a must be an integer

	>>> add_integer(1,'b')

	TypeError: b must be an integer

	>>> add_integer('a', 2)

	TypeError: a must be an integer

	>>> add_integer('a', 'b')

	>>> add_integer()

	TypeError: a must be an integer