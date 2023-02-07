{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ce96e717-8d67-4043-b6a3-98eb914b0f60",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('Virat Kohli', 24936), ('Jack Kallis', 25534), ('Ricky Ponting', 27483), ('Sachin Tendulkar', 34357)]\n"
     ]
    }
   ],
   "source": [
    "# day-4\n",
    "# Q,1\n",
    "l = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]\n",
    "A = sorted(l,key = lambda x :x[1] )\n",
    "print(A)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a0e54dd8-7e53-4b2e-b717-9b4324610328",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]\n"
     ]
    }
   ],
   "source": [
    "# Q,2\n",
    "l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
    "B = list(map(lambda x : x**2,l1))\n",
    "print(B)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "dc9480ea-76b4-412e-9b51-92251584c100",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')\n"
     ]
    }
   ],
   "source": [
    "# Q,3\n",
    "L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
    "C = tuple(map(lambda x : str(x),L))\n",
    "print(C)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f5bb9f3d-3da6-4402-b938-8159aa881186",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15511210043330985984000000\n"
     ]
    }
   ],
   "source": [
    "# Q,4\n",
    "from functools import reduce\n",
    "\n",
    "numbers = [i  for i in range(1,26)]\n",
    "product = reduce(lambda x,y: x*y , numbers)\n",
    "print(product)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "56c36b79-f0c1-4f25-b342-ee54c075f5fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[6, 60, 90, 120]\n"
     ]
    }
   ],
   "source": [
    "# Q,5\n",
    "l = [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]\n",
    "v = list(filter(lambda x : x %2 ==0 and x % 3 == 0,l))\n",
    "print(v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2ad42c5a-0bcd-4500-b40c-860f3327385d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Q,6\n"
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
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
