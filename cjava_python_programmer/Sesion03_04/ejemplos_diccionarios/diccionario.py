datastore = { "office": {
    "medical": [
      { "room-number": 100,
        "use": "reception",
        "sq-ft": 50,
        "price": 75
      },
      { "room-number": 101,
        "use": "waiting",
        "sq-ft": 250,
        "price": 75
      },
      { "room-number": 102,
        "use": "examination",
        "sq-ft": 125,
        "price": 153.5
      },
      { "room-number": 103,
        "use": "examination",
        "sq-ft": 125,
        "price": 159
      },
      { "room-number": 104,
        "use": "office",
        "sq-ft": 150,
        "price": 100
      }
    ],
    "parking": {
      "location": "premium",
      "style": "covered",
      "price": 750
    }
  }
}

# accediendo a parking
print(datastore["office"]["parking"])

#almacenando store
spaces = datastore["office"]["medical"]

print("Oficinas de atencion médica")
for item in spaces:
    if item.get("use") == "examination":
        print("La oficina médica %d tiene un costo de %8.2f." % (item.get("room-number") , item.get("price")) ) 


