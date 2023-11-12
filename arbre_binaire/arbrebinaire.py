from arbre import Arbre
from racine import Racine

racine = Racine(5, 0)
racine.insert(11)
racine.insert(6)
racine.insert(3)
racine.insert(4)
racine.insert(8)
racine.insert(7)
racine.insert(3.5)
racine.insert(4.6)
racine.insert(2)
racine.insert(1)
racine.insert(0.0005)
racine.insert(2.5)
racine.insert(10)

racine = racine.delete(11)
maximum = racine.getMax()
minimum = racine.getMinIterative()
# print(maximum.value , minimum.value)
# # value = racine.search( 0.0005 );
# # print( "Found at depth " , value.getDepth() )


if __name__ == '__main__':
    racine.print()
