"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


import os
import matplotlib.pyplot as plt
import pandas as pd


def pregunta_01():
    """
    Genera el archivo `files/plots/news.png` siguiendo las instrucciones del video.
    """
    # 1. Cargar el dataset
    df = pd.read_csv("files/input/news.csv", index_col=0)

    # Convertir los nombres de las columnas a minúsculas para evitar KeyErrors
    df.columns = df.columns.str.lower()

    # 2. Inicializar la figura vacía
    plt.figure()

    # 3. Definir los diccionarios de estilos (con nombres de grises estándar de Matplotlib)
    colors = {
        "television": "dimgray",
        "newspaper": "gray",
        "radio": "lightgray",
        "internet": "tab:blue",
    }

    z_order = {
        "television": 1,
        "newspaper": 1,
        "radio": 1,
        "internet": 2,
    }

    line_widths = {
        "television": 2,
        "newspaper": 2,
        "radio": 2,
        "internet": 4,
    }

    # 4. Graficar las líneas iterando sobre las columnas
    for col in df.columns:
        plt.plot(
            df.index,
            df[col],
            color=colors[col],
            zorder=z_order[col],
            linewidth=line_widths[col],
            label=col,
        )

    # 5. Configurar el Título
    plt.title("People get news", fontsize=16)

    # 6. Eliminar el ruido visual (Spines: superior, derecho e izquierdo)
    axes = plt.gca()
    axes.spines["top"].set_visible(False)
    axes.spines["right"].set_visible(False)
    axes.spines["left"].set_visible(False)

    # Hacer invisible por completo el eje Y
    axes.yaxis.set_visible(False)

    # 7. Obtener los años extremos
    first_year = df.index[0]
    last_year = df.index[-1]

    # 8. Agregar los marcadores (scatter) y etiquetas de texto al principio y al final
    for col in df.columns:
        first_val = df.loc[first_year, col]
        last_val = df.loc[last_year, col]

        # Puntos y texto del lado izquierdo
        plt.scatter(
            first_year, first_val, color=colors[col], zorder=z_order[col]
        )
        plt.text(
            first_year - 0.2,
            first_val,
            f"{col} {first_val}%",
            ha="right",
            va="center",
            color=colors[col],
        )

        # Puntos y texto del lado derecho
        plt.scatter(last_year, last_val, color=colors[col], zorder=z_order[col])
        plt.text(
            last_year + 0.2,
            last_val,
            f"{last_val}%",
            ha="left",
            va="center",
            color=colors[col],
        )

    # 9. Configurar las etiquetas completas del eje X (Años)
    plt.xticks(df.index, labels=df.index, ha="center")

    # 10. Guardar la gráfica en la ruta especificada de manera compacta
    os.makedirs("files/plots", exist_ok=True)
    plt.tight_layout()
    plt.savefig("files/plots/news.png")
    plt.close()


if __name__ == "__main__":
    pregunta_01()