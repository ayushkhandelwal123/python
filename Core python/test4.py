{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "def mult(x,y):\n",
    "    pro=x*y\n",
    "    return pro"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "50"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mult(10,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [],
   "source": [
    "def add(x=5):\n",
    "    sum=x+7\n",
    "    return sum"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "12"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "add()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "square=lambda x:x*x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "36"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "square(6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "function"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(add)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "function"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(square)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [],
   "source": [
    "x=lambda a:a+10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "16"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x(6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "48\n",
      "75\n"
     ]
    }
   ],
   "source": [
    "def mult(n):\n",
    "    return lambda a:a*n\n",
    "x=mult(2)\n",
    "y=mult(3)\n",
    "print(x(24))\n",
    "print(y(25))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "array=['apple','banana','cherry']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "apple\n",
      "banana\n",
      "cherry\n"
     ]
    }
   ],
   "source": [
    "for i in array:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'cherry'"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "array[2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['apple', 'banana', 'cherry', 'renault', 'honda', 'volvo']\n"
     ]
    }
   ],
   "source": [
    "cars=['renault','honda','volvo']\n",
    "array.extend(cars)\n",
    "print(array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "class Test:\n",
    "    x=4\n",
    "a=Test()\n",
    "print(a.x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Person:\n",
    "  def __init__(self, name, age):\n",
    "    self.name = name\n",
    "    self.age = age\n",
    "\n",
    "p1 = Person(\"John\", 36)\n",
    "\n",
    "del p1\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ayush\n",
      "IT\n",
      "A\n",
      "19\n",
      "9521057735\n"
     ]
    }
   ],
   "source": [
    "class Student:\n",
    " def __init__(self,name,branch,section,age,phonenumber):\n",
    "        self.name=name\n",
    "        self.branch=branch\n",
    "        self.section=section\n",
    "        self.age=age\n",
    "        self.phonenumber=phonenumber\n",
    "s1=Student(\"Ayush\",\"IT\",\"A\",19,9521057735)\n",
    "\n",
    "print(s1.name)\n",
    "print(s1.branch)\n",
    "print(s1.section)\n",
    "print(s1.age)\n",
    "print(s1.phonenumber)\n",
    "        \n",
    "        \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My name is : \tJohn\n"
     ]
    }
   ],
   "source": [
    "class Person:\n",
    "    def __init__(self, name, age):\n",
    "        self.name = name\n",
    "        self.age = age\n",
    "    \n",
    "    def myfunc(self):\n",
    "        print(\"My name is : \\t\"+self.name)\n",
    "\n",
    "p1 = Person(\"John\", 36)\n",
    "p1.myfunc()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "apple\n",
      "banana\n",
      "cherry\n"
     ]
    }
   ],
   "source": [
    "mytuple = (\"apple\", \"banana\", \"cherry\")\n",
    "myit = iter(mytuple)\n",
    "\n",
    "print(next(myit))\n",
    "print(next(myit))\n",
    "print(next(myit))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A\n",
      "y\n",
      "u\n",
      "s\n",
      "h\n"
     ]
    }
   ],
   "source": [
    "str=\"Ayush\"\n",
    "it=iter(str)\n",
    "print(next(it))\n",
    "print(next(it))\n",
    "print(next(it))\n",
    "print(next(it))\n",
    "print(next(it))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "l\n",
      "a\n",
      "p\n",
      "t\n",
      "o\n",
      "p\n"
     ]
    }
   ],
   "source": [
    "s=\"laptop\"\n",
    "for i in s:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n",
      "11\n",
      "12\n",
      "13\n",
      "14\n",
      "15\n",
      "16\n",
      "17\n",
      "18\n",
      "19\n",
      "20\n"
     ]
    }
   ],
   "source": [
    "class Numbers:\n",
    "  def __iter__(self):\n",
    "    self.a = 1\n",
    "    return self\n",
    "\n",
    "  def __next__(self):\n",
    "    if self.a<=20:\n",
    "        x=self.a\n",
    "        self.a += 1\n",
    "        return x\n",
    "    else:\n",
    "        raise StopIteration\n",
    "\n",
    "z = Numbers()\n",
    "y = iter(z)\n",
    "\n",
    "for i in y:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'module'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-74-51d975b95349>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mmodule\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mmodule\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mgreeting\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Ayush\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'module'"
     ]
    }
   ],
   "source": [
    "import module\n",
    "\n",
    "module.greeting(\"Ayush\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
