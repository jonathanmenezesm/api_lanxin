Primeira dificuldade enfrentada:
    Rodar o servidor.
    Estava utilzando o comando "python app.py", porém, ele estava fora da pasta raiz isso impedindo que o servidor fosse iniciado.

Soluções:
    - coloquei dentro da src.
    - ajeitei os imports em app.py
        de: 
            from controller.home import home_route
            rom controller.user_controller import user_route
        para:
            from src.controller.home import home_route
            from src.controller.user_controller import user_route
    - criei um arquivo run.py na pasta raiz, recebendo somente para iniciar o app.