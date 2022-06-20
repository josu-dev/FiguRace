<h1> Grupo <img src="https://media.giphy.com/media/lkTunMhUitIEITABuS/giphy.gif" height="40"/></h1>


<br>


## Integrantes

Fabian Martinez Rincon | Josue Suarez | Lucas Gallardo | Iñaki Agustin Lapeyre
--- | --- | --- | ---
![@Fabian-Martinez1](https://avatars.githubusercontent.com/Fabian-Martinez1?s=150&v=0) | ![@J-Josu](https://avatars.githubusercontent.com/J-Josu?s=150&v=1) | ![@Lucas-Andres-GF](https://avatars.githubusercontent.com/Lucas-Andres-GF?s=150&v=1) | ![@KinnaGt](https://avatars.githubusercontent.com/KinnaGt?s=150&v=1)
[@Fabian-Martinez1](https://github.com/Fabian-Martinez1) | [@J-Josu](https://github.com/J-Josu) | [@Lucas-Andres-GF](https://github.com/Lucas-Andres-GF) | [@KinnaGt](https://github.com/KinnaGt)


<br>


## Guia primer uso:

1. #### Requerimientos de sistema

    Se necesita tener python version mayor o igual a 3.10

    > En caso de que no, una de estas guias puede ser de ayuda:
    > - [Windows](https://docs.python.org/es/3.10/using/windows.html)
    > - [Linux](https://docs.python.org/es/3.10/using/unix.html)
    > - [Mac](https://docs.python.org/es/3.10/using/mac.html)

1. #### Obtener el repositorio

    Existen dos maneras:

    - Clonar el repositorio por medio de SSH o HTTPS

    - Descargar el .zip (luego realizar la descompresion)

1. #### Instalacion de dependencias

    Las dependencias son:

    - Juego: PySimpleGui

    - Datasets: Pandas

    - Analysis: Pandas, MatPlotLib

    Para su instalacion:

    1. Primero abrir una terminal/consola en la ubicacion donde descargo el contenido del repositorio

    2. Luego ejecutar el siguiente comando
        ```bash
        pip install -r requirements.txt
        ```

1. #### Ejecución

    Ejecucion de los diferentes apartados:

    > Se asume que se encuentra en una terminal/consola en la ubicacion donde descargo el contenido del repositorio y realizo los pasos previos de la guia

    - **Juego**

        ```bash
        py figurace.py
        ```

    - **Procesamiento Datasets**

        Esta seccion se encuentra en la carpeta dataset_section

        El procesamiento de los datasets se encuentra como un script de python o un cuaderno interactivo de [JupyterNotebook](https://jupyter.org/) en la carpeta second_assignment

        Los datasets a procesar en la carpeta base_datasets

    - **Analizis de eventos**

        Esta seccion se encuentra en la carpeta analysis_section

        El analisis de los eventos generados al jugar partidas se encuentra como un script de python o un cuaderno interactivo de [JupyterNotebook](https://jupyter.org/)


<br>


## Fuentes

- Datasets:

    [Spotify](https://www.kaggle.com/datasets/muhmores/spotify-top-100-songs-of-20152019) | [Lagos](https://www.ign.gob.ar/NuestrasActividades/Geografia/DatosArgentina/Lagos) | [FIFA 2021](https://www.kaggle.com/datasets/aayushmishra1512/fifa-2021-complete-player-data?resource=download)
    --- | --- | --- 
    <img src = "https://user-images.githubusercontent.com/55964635/170844079-de18c35d-138a-4c24-af09-c74086ffcab8.jpg" width = "150" height = "150" alt = "ejemplo" align = "center" /> | <img src = "https://user-images.githubusercontent.com/55964635/170844002-7aa0ba0d-7b8b-4c2c-adfa-2adec352e59c.jpg" width = "150" height = "150" alt = "ejemplo" align = "center" /> | <img src = "https://user-images.githubusercontent.com/55964635/170844054-57c7460d-62d0-4cc1-988e-32232ef88e15.jpg" width = "150" height = "150" alt = "ejemplo" align = "center" />

- Imagenes:

    - [README](https://pixabay.com/es/)

    - [Menu del juego](https://romannurik.github.io/AndroidAssetStudio/icons-notification.html)

    - Otras, creación propia


<br>
<br>


## Comentarios adicionales

La carpeta .vscode contiene configuraciones particulares de este proyecyo para el editor VisualStudioCode

La carpeta typings los tipados necesarios de la libreria PySimpleGUI para que el LanguageServer pueda funcionar adecuadamente al hacer el static type checking

La carpeta documents contiene enunciados y otros archivos relaciones a que se tenia que realizar con el proyecto
