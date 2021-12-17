Usage
=====

.. _installation:

Installation
------------

Чтобы использовать Lumache, сначала установите его с помощью командды в консоле:

.. code-block:: console

   pip install lumache

Creating recipes
----------------

Чтобы получить список случайных ингредиентов,
вы можете использовать функцию ``lumache.get_random_ingredients()``:

.. autofunction:: lumache.get_random_ingredients

Параметр ``kind`` должен иметь значения ``"meat"``, ``"fish"``,
или ``"veggies"``. В противном случае, :py:func:`lumache.get_random_ingredients`
вызовет исключение.

.. autoexception:: lumache.InvalidKindError

   Возникает если kind не действительный.

import lumache
lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']