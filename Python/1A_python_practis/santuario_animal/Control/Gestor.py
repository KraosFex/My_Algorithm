import pickle

class UserManagement:
  def __init__(self):
    try:
      with open("Registro/Registro.pkl", "rb") as f: # es necesario que la extencion sea .pkl, para que sea legible con pickle
        self.data = pickle.load(f) # Luego se carga con pickle
    except FileNotFoundError as f:
      self.data = []

  def register_in_data(self):
    with open("Registro/Registro.pkl", "wb") as f:
      pickle.dump(self.data, f)

  def create_new_user(self, data_new_user:tuple) -> bool:
      if len(self.datos) <= 3:
        new_user = {"usuario": data_new_user[0],
                    "clave": dare_new_user[1],
                    "santuarios":[],
                    }
        self.data.append(new_user)
        self.register_in_data()
        return True
      else:
        return False

  def login_user(self, credentials:tuple):
      for user in self.datos:
          if user["usuario"] == credentials[0] and user["clave"] == credentials[1]:
              return {"status": True, 
                      "User": user,
                      }
          else:
              return {"status": False,
                      "User": {},
                      }

  def __str__(self) -> str:
    registration = ""
    for line in self.data:
      registration += f"{line}\n"
    return registration
