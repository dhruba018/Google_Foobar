{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## Challenge 1.0. Repeatation\n",
    "\n",
    "## Filter by frequncy count...\n",
    "def solution(data, n):\n",
    "    freq, data_new = { }, [ ]\n",
    "    for k in data:\n",
    "        freq[k] = freq[k] + 1 if k in freq else 1\n",
    "    data_new = [kk for kk in data if freq[kk] <= n]\n",
    "    return data_new\n",
    "\n",
    "## Run...\n",
    "print(\"Filtered list = \", solution([5, 10, 15, 10, 7], n = 1))\n",
    "print(\"Filtered list = \", solution([1, 2, 3], n = 0))\n",
    "print(\"Filtered list = \", solution([1, 2, 2, 3, 3, 3, 4, 5, 5], n = 1))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}