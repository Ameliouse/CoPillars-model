# import sys
# import bkt

# if __name__ == '__main__':
#     model = bkt.fit_model()
#     if len(sys.argv) != 3:
#         print("Utilisation: python script.py <paramètre1> <paramètre2>")
#         sys.exit(1)

#     # Récupérer les arguments de la ligne de commande
#     user_id = sys.argv[1]
#     skill_id = sys.argv[2]
    
#     bkt.update_player(model, user_id, skill_id)

from cx_Freeze import setup, Executable

# setup(
#     name="bkt",
#     version="1.0",
#     description="Description",
#     executables=[Executable("bkt.py")]
# )

setup(
    name="runbkt",
    version="1.0",
    description="Description",
    executables=[Executable("bkt.py")]
)
