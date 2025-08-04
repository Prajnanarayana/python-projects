{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "47acba8b-f6cf-47f7-88a0-a0f9a2817e31",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "\n",
    "def generate_secret():\n",
    "  digits = list(range(10))\n",
    "  random.shuffle(digits)\n",
    "  return ''.join([str(digit) for digit in digits[:4]])\n",
    "\n",
    "\n",
    "def calculate_cows_and_bulls(secret, guess):\n",
    "  bulls = sum([1 for i in range(4) if guess[i] == secret[i]])\n",
    "  cows = sum([1 for i in range(4) if guess[i] in secret]) - bulls\n",
    "\n",
    "  return cows, bulls\n",
    "# comment\n",
    "\n",
    "def main():\n",
    "  secret = generate_secret()\n",
    "  print('I have generated a 4-digit number with unique digits. Try to guess it!')\n",
    "\n",
    "  while True:\n",
    "    guess = input('Guess: ')\n",
    "    if len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4:\n",
    "      cows, bulls = calculate_cows_and_bulls(secret, guess)\n",
    "      print(f'{cows} cows, {bulls} bulls')\n",
    "\n",
    "      if bulls == 4:\n",
    "        print('Congratulations! You guessed the correct number')\n",
    "        break\n",
    "    else:\n",
    "      print('Invalid guess. Please enter a 4-digit number with unique digits.')\n",
    "      \n",
    "\n",
    "if __name__ == '__main__':\n",
    "  main()\n",
    "\n",
    "  # comment"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1daf1015-4e67-4fc9-9a5d-fbb705ed090f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "27462672-ad54-48d3-861d-2289386f98e3",
   "metadata": {},
   "outputs": [],
   "source": []
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
