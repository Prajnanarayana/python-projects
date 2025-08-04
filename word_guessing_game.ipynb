{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5eb2987d-ea44-4b1d-bcda-39bfd808a866",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random \n",
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c10b3e61-c9a4-417c-afd5-8014247271b9",
   "metadata": {},
   "outputs": [],
   "source": [
    "def read_words():\n",
    "  try:\n",
    "    with open('words.txt', 'r') as file:\n",
    "      words = file.read().splitlines()\n",
    "      return words\n",
    "  except FileNotFoundError:\n",
    "    print('words.txt does not exist.')\n",
    "    return []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "460b7078-701a-4f24-9ab4-6db344dd9702",
   "metadata": {},
   "outputs": [],
   "source": [
    "def display_word(secret_word, guessed_letters):\n",
    "  word_to_display = ''\n",
    "\n",
    "  for letter in secret_word:\n",
    "    if letter in guessed_letters:\n",
    "      word_to_display += letter\n",
    "    else:\n",
    "      word_to_display += '_'\n",
    "\n",
    "  print(word_to_display)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6ecd4fb5-9796-44b3-b30c-4bd0bd17141e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_guess(guessed_letters):\n",
    "  while True:\n",
    "    guess = input('Enter a letter: ').lower()\n",
    "    if len(guess) != 1:\n",
    "      print('Enter only one letter.')\n",
    "    elif not re.search('[a-z]', guess):\n",
    "      print('Enter only letters from a to z.')\n",
    "    elif guess in guessed_letters:\n",
    "      print('You already guessed that letter.')\n",
    "    else:\n",
    "      return guess\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "44a9a8f7-5ab1-4300-bd5a-a788afdf78eb",
   "metadata": {},
   "outputs": [],
   "source": [
    "def is_word_guessed(secret_word, guessed_letters):\n",
    "  for letter in secret_word:\n",
    "    if letter not in guessed_letters:\n",
    "      return False\n",
    "  return True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "8c0ed660-08c8-4d2f-b383-6946f9e93474",
   "metadata": {},
   "outputs": [],
   "source": [
    "def main():\n",
    "  words = read_words()\n",
    "  if not words:\n",
    "    print('No words loaded.')\n",
    "    return \n",
    "  secret_word = random.choice(words)\n",
    "  print(secret_word)\n",
    "\n",
    "  attempts = 6\n",
    "  guessed_letters = []\n",
    "  while attempts > 0:\n",
    "    display_word(secret_word, guessed_letters)\n",
    "\n",
    "    guess = get_guess(guessed_letters)\n",
    "    guessed_letters.append(guess)\n",
    "    \n",
    "\n",
    "    if guess in secret_word:\n",
    "      print('Good guess')\n",
    "      \n",
    "      if is_word_guessed(secret_word, guessed_letters):\n",
    "        print(f'Congratulations! You guessed the word! The final word is {secret_word}' )\n",
    "        break\n",
    "          \n",
    "    else:\n",
    "      print('Wrong guess')\n",
    "      attempts -= 1\n",
    "      if attempts == 0:\n",
    "        print(f'Game over! The word was {secret_word}')\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c7b7a64b-5087-4fd2-bbda-5d4c8a35fdaf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "watermelon\n",
      "__________\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a letter:  w\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Good guess\n",
      "w_________\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a letter:  t\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Good guess\n",
      "w_t_______\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a letter:  a\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Good guess\n",
      "wat_______\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a letter:  e\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Good guess\n",
      "wate__e___\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a letter:  r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Good guess\n",
      "water_e___\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a letter:  m\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Good guess\n",
      "waterme___\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a letter:  l\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Good guess\n",
      "watermel__\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a letter:  o\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Good guess\n",
      "watermelo_\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a letter:  n\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Good guess\n",
      "Congratulations! You guessed the word! The final word is watermelon\n"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "  main()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
