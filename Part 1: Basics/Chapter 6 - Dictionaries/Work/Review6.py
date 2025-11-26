{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": { 
      "provenance": [],
      "authorship_tag": "ABX9TyNaPW8mUN3GNjgRY3aD1mGT",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/BKnightHD/Python-CC/blob/main/Part%201%3A%20Basics/Chapter%206%20-%20Dictionaries/Work/Learning6.1.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Nesting"
      ],
      "metadata": {
        "id": "6q-C4Zaz5P6n"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "id": "k3F5XmQE4W3w",
        "outputId": "0f341b0f-576a-49f0-96cf-2d88e07acb96",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'color': 'green', 'points': 5}\n",
            "{'color': 'yellow', 'points': 10}\n",
            "{'color': 'red', 'points': 15}\n",
            "...\n",
            "{'name': 'giuseppe', 'age': 29}\n",
            "{'name': 'zach', 'age': 30}\n",
            "{'name': 'david', 'age': 31}\n"
          ]
        }
      ],
      "source": [
        "# reviewing nesting with dictionaries\n",
        "\n",
        "alien_0 = {'color': 'green', 'points': 5}\n",
        "alien_1 = {'color': 'yellow', 'points': 10}\n",
        "alien_2 = {'color': 'red', 'points': 15}\n",
        "\n",
        "aliens = [alien_0, alien_1, alien_2]\n",
        "\n",
        "for alien in aliens:\n",
        "  print(alien)\n",
        "\n",
        "print(\"...\")\n",
        "# try on my own\n",
        "\n",
        "freind_0 = {'name': 'giuseppe', 'age': 29}\n",
        "freind_1 = {'name': 'zach', 'age': 30}\n",
        "freind_2 = {'name': 'david', 'age': 31}\n",
        "\n",
        "freinds = [freind_0, freind_1, freind_2]\n",
        "for freind in freinds:\n",
        "  print(freind)"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Key program using multiple methods and functions"
      ],
      "metadata": {
        "id": "id2snizf8T_5"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Make an empty list for storing aliens\n",
        "\n",
        "aliens = []\n",
        "\n",
        "# Make 30 green aliens\n",
        "for alien_number in range(30): # this line tells python how many times we want the loop to repeat\n",
        "  new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}\n",
        "  aliens.append(new_alien)\n",
        "\n",
        "# Show the first 5 aliens:\n",
        "for alien in aliens[:5]:\n",
        "  print(alien)\n",
        "print(\"...\")\n",
        "\n",
        "# Show how many aliens have been created.\n",
        "print(f\"Total number of aliens: {str(len(aliens))}\")"
      ],
      "metadata": {
        "id": "U_s5OVyA6BKi",
        "outputId": "f232de23-9819-4cfb-eaf0-8f8b5cefe024",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'color': 'green', 'points': 5, 'speed': 'slow'}\n",
            "{'color': 'green', 'points': 5, 'speed': 'slow'}\n",
            "{'color': 'green', 'points': 5, 'speed': 'slow'}\n",
            "{'color': 'green', 'points': 5, 'speed': 'slow'}\n",
            "{'color': 'green', 'points': 5, 'speed': 'slow'}\n",
            "...\n",
            "Total number of aliens: 30\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Recreating loop for better understanding\n",
        "\n",
        "objects = []\n",
        "\n",
        "for items in range(20):\n",
        "  more_objects = {'item': 'chair', 'animal': 'dog', 'car': 'honda'}\n",
        "  objects.append(more_objects)\n",
        "\n",
        "for something in objects[:10]:\n",
        "  print(something)\n",
        "\n",
        "print(f\"{str(len(something))}\")"
      ],
      "metadata": {
        "id": "dwYCooX88CFA",
        "outputId": "2862cb8d-4a42-4066-b33b-9911c332b06d",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'item': 'chair', 'animal': 'dog', 'car': 'honda'}\n",
            "{'item': 'chair', 'animal': 'dog', 'car': 'honda'}\n",
            "{'item': 'chair', 'animal': 'dog', 'car': 'honda'}\n",
            "{'item': 'chair', 'animal': 'dog', 'car': 'honda'}\n",
            "{'item': 'chair', 'animal': 'dog', 'car': 'honda'}\n",
            "{'item': 'chair', 'animal': 'dog', 'car': 'honda'}\n",
            "{'item': 'chair', 'animal': 'dog', 'car': 'honda'}\n",
            "{'item': 'chair', 'animal': 'dog', 'car': 'honda'}\n",
            "{'item': 'chair', 'animal': 'dog', 'car': 'honda'}\n",
            "{'item': 'chair', 'animal': 'dog', 'car': 'honda'}\n",
            "3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "aliens = []\n",
        "\n",
        "for alien_number in range(20):\n",
        "  new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}\n",
        "  aliens.append(new_alien)\n",
        "for alien_number in range(10):\n",
        "  new_alien_0 = {'color': 'blue', 'points': 0, 'speed': 'slow'}\n",
        "  aliens.append(new_alien_0)\n",
        "\n",
        "# Changing the first 5 aliens to yellow\n",
        "for alien in aliens[6:10]:\n",
        "  if alien['color'] == 'green':\n",
        "     alien['color'] = 'red'\n",
        "     alien['points'] = 15\n",
        "     alien['speed'] = 'fast'\n",
        "\n",
        "for alien in aliens[:5]:\n",
        "  if alien['color'] == 'green':\n",
        "     alien['color'] = 'yellow'\n",
        "     alien['points'] = 10\n",
        "     alien['speed'] = 'medium'\n",
        "\n",
        "for alien in aliens[:30]:\n",
        "  print(alien)\n",
        "print(\"...\")"
      ],
      "metadata": {
        "id": "z4a0_iXM9Ina",
        "outputId": "af79c22d-5ca9-4268-fc15-c8c62e39196a",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'color': 'yellow', 'points': 10, 'speed': 'medium'}\n",
            "{'color': 'yellow', 'points': 10, 'speed': 'medium'}\n",
            "{'color': 'yellow', 'points': 10, 'speed': 'medium'}\n",
            "{'color': 'yellow', 'points': 10, 'speed': 'medium'}\n",
            "{'color': 'yellow', 'points': 10, 'speed': 'medium'}\n",
            "{'color': 'green', 'points': 5, 'speed': 'slow'}\n",
            "{'color': 'red', 'points': 15, 'speed': 'fast'}\n",
            "{'color': 'red', 'points': 15, 'speed': 'fast'}\n",
            "{'color': 'red', 'points': 15, 'speed': 'fast'}\n",
            "{'color': 'red', 'points': 15, 'speed': 'fast'}\n",
            "{'color': 'green', 'points': 5, 'speed': 'slow'}\n",
            "{'color': 'green', 'points': 5, 'speed': 'slow'}\n",
            "{'color': 'green', 'points': 5, 'speed': 'slow'}\n",
            "{'color': 'green', 'points': 5, 'speed': 'slow'}\n",
            "{'color': 'green', 'points': 5, 'speed': 'slow'}\n",
            "{'color': 'green', 'points': 5, 'speed': 'slow'}\n",
            "{'color': 'green', 'points': 5, 'speed': 'slow'}\n",
            "{'color': 'green', 'points': 5, 'speed': 'slow'}\n",
            "{'color': 'green', 'points': 5, 'speed': 'slow'}\n",
            "{'color': 'green', 'points': 5, 'speed': 'slow'}\n",
            "{'color': 'blue', 'points': 0, 'speed': 'slow'}\n",
            "{'color': 'blue', 'points': 0, 'speed': 'slow'}\n",
            "{'color': 'blue', 'points': 0, 'speed': 'slow'}\n",
            "{'color': 'blue', 'points': 0, 'speed': 'slow'}\n",
            "{'color': 'blue', 'points': 0, 'speed': 'slow'}\n",
            "{'color': 'blue', 'points': 0, 'speed': 'slow'}\n",
            "{'color': 'blue', 'points': 0, 'speed': 'slow'}\n",
            "{'color': 'blue', 'points': 0, 'speed': 'slow'}\n",
            "{'color': 'blue', 'points': 0, 'speed': 'slow'}\n",
            "{'color': 'blue', 'points': 0, 'speed': 'slow'}\n",
            "...\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "|"
      ],
      "metadata": {
        "id": "OzZHNib7_SK7"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}