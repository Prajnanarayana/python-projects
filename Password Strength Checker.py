{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "5d4be8d7-989f-4ffd-9da0-f1c095d22ce1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a password:  Roobi@2001\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Password strength: Very Strong\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "\n",
    "def check_password_strength(password):\n",
    "  strength = 0 \n",
    "\n",
    "  if len(password) >= 8:\n",
    "    strength += 1\n",
    "  if re.search('[a-z]', password):\n",
    "    strength += 1\n",
    "  if re.search('[A-Z]', password):\n",
    "    strength += 1\n",
    "  if re.search('[0-9]', password):\n",
    "    strength += 1\n",
    "  if re.search('[@#$%+=!]', password):\n",
    "    strength += 1\n",
    "\n",
    "  return strength\n",
    "  \n",
    "\n",
    "def main():\n",
    "  password = input('Enter a password: ')\n",
    "  strength = check_password_strength(password)\n",
    "\n",
    "  if strength == 5:\n",
    "    print('Password strength: Very Strong')\n",
    "  elif strength == 4:\n",
    "    print('Password strength: Strong')\n",
    "  elif strength == 3:\n",
    "    print('Password strength: Medium')\n",
    "  elif strength == 2:\n",
    "    print('Password strength: Weak')\n",
    "  else:\n",
    "    print('Password strength: Very Weak')\n",
    "\n",
    "\n",
    "\n",
    "\n",
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
