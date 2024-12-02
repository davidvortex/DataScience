dicccionario={}
type (dicccionario)

edad = {"eloit":30,"luis":25,"fernando":24}
len(edad)

print(edad["eloit"])
edad["fernando"] = 25

# me llamara los id del arreglo ejemplo "eloit","luis","fernando" 
edad.keys()

# me llamara los valores de cada uno de los id ejemplo: 30,35,24
edad.values()

# presentara los imtems que teine el arrelgo completo ya que  me dira tanto los id como valores
edad.items()

# nos dara nadamas el puro valor
edad.get("luis")

edad.update({"Luis":27})
print(edad)

