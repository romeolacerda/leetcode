1671 Minimum Number of Removals to Make Montain Array

You may recall that an array arr is a mountain array if and only if:

- arr.length >= 3
- There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
  - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
  - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Given an integer array nums​​​, return the minimum number of elements to remove to make nums​​​ a mountain array.

Example 1:

Input: nums = [1,3,1]
Output: 0
Explanation: The array itself is a mountain array so we do not need to remove any elements.

Example 2:

Input: nums = [2,1,1,5,6,2,3,1]
Output: 3
Explanation: One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].

Constraints:

3 <= nums.length <= 1000
1 <= nums[i] <= 109
It is guaranteed that you can make a mountain array out of nums.
########################################################

Explicaçãp em Português :
Mountain Array
Um mountain array é um array que:

1. Tem pelo menos três elementos.
2. Existe um índice i tal que:
   -Os elementos à esquerda de i são estritamente crescentes até i.
   -Os elementos à direita de i são estritamente decrescentes a partir de i.

Objetivo do Algoritmo
O objetivo é descobrir quantos elementos precisamos remover de um array dado para que ele se torne um mountain array.

Algoritmo Passo a Passo
1.Função LIS (Longest Increasing Subsequence):

    - Esta função calcula o comprimento da subsequência crescente mais longa para um array.
    -Usamos uma lista chamada lis para armazenar os elementos da subsequência crescente e um array lis_len para armazenar o comprimento da LIS até cada índice do array original.

Como funciona:
Para cada elemento do array, encontramos a posição em que ele pode ser inserido na lista lis usando a função bisect_left, que mantém lis ordenada.
Se o elemento for maior que todos os elementos em lis, ele é adicionado ao final. Se não, ele substitui o menor elemento que é maior ou igual a ele.
O comprimento da subsequência crescente é atualizado em lis_len.

2.Função Principal minimumMountainRemovals:

- Calcula a lis_lr, que é a LIS do array original.
- Calcula a lis_rl, que é a LIS do array revertido (para encontrar a subsequência decrescente) e a inverte novamente para corresponder aos índices do array original.
- Comparação:

  - Para cada índice do array, verificamos se lis_lr[i] > 1 e lis_rl[i] > 1. Isso significa que, em i, podemos formar uma montanha.
  - A soma dos tamanhos de lis_lr[i] e lis_rl[i] (subtraindo 1 para não contar o pico duas vezes) nos dá o tamanho da montanha naquele índice.

    3.Cálculo do Resultado:
    O tamanho máximo da montanha encontrada é subtraído do tamanho original do array para determinar quantos elementos precisam ser removidos.
    Exemplo Detalhado
    Vamos considerar o exemplo nums = [2, 1, 1, 5, 6, 2, 3, 1]:

1. Calcular lis_lr
   Array original: [2, 1, 1, 5, 6, 2, 3, 1]

Cálculo:
Para 2, lis = [2], lis_len[0] = 1.
Para 1, não é maior que 2, então substitui 2 por 1: lis = [1], lis_len[1] = 1.
Para 1 (novamente): lis = [1], lis_len[2] = 1.
Para 5, lis = [1, 5], lis_len[3] = 2.
Para 6, lis = [1, 5, 6], lis_len[4] = 3.
Para 2, lis = [1, 2, 6], lis_len[5] = 2.
Para 3, lis = [1, 2, 3], lis_len[6] = 3.
Para 1, lis = [1], lis_len[7] = 1.
Resultado: lis_lr = [1, 1, 1, 2, 3, 2, 3, 1]

2. Calcular lis_rl
   Array revertido: [1, 3, 2, 6, 5, 1, 1, 2]

Cálculo:
Para 1, lis = [1].
Para 3, lis = [1, 3].
Para 2, substitui 3 por 2: lis = [1, 2].
Para 6, lis = [1, 2, 6].
Para 5, substitui 6 por 5: lis = [1, 2, 5].
Para 1, lis = [1].
Para 1 (novamente): lis = [1].
Para 2, lis = [1, 2].
Resultado (revertendo de novo): lis_rl = [2, 2, 3, 2, 1, 1, 1, 1]

3. Encontrar a Montanha Máxima
   Agora, verificamos onde podemos ter uma montanha:

Para i = 0: lis_lr[0] = 1, lis_rl[0] = 2 → Não é uma montanha.
Para i = 1: lis_lr[1] = 1, lis_rl[1] = 2 → Não é uma montanha.
Para i = 2: lis_lr[2] = 1, lis_rl[2] = 3 → Não é uma montanha.
Para i = 3: lis_lr[3] = 2, lis_rl[3] = 2 → É uma montanha. Tamanho = 2 + 2 - 1 = 3.
Para i = 4: lis_lr[4] = 3, lis_rl[4] = 2 → É uma montanha. Tamanho = 3 + 2 - 1 = 4.
Para i = 5: lis_lr[5] = 2, lis_rl[5] = 1 → Não é uma montanha.
Para i = 6: lis_lr[6] = 3, lis_rl[6] = 1 → Não é uma montanha.
Para i = 7: lis_lr[7] = 1, lis_rl[7] = 1 → Não é uma montanha.
Montanha Máxima: O tamanho máximo da montanha é 4.

Resultado Final
Tamanho original do array: 8
Tamanho da maior montanha: 4
Elementos a remover: 8 - 4 = 4

#############################################################
Explanation in English
Mountain Array
A mountain array is an array that:

Has at least three elements.
There exists an index i such that:
The elements to the left of i are strictly increasing up to i.
The elements to the right of i are strictly decreasing from i.
Algorithm Objective
The goal is to determine how many elements need to be removed from a given array for it to become a mountain array.

Step-by-Step Algorithm

LIS Function (Longest Increasing Subsequence):

This function calculates the length of the longest increasing subsequence for an array.
We use a list called lis to store the elements of the increasing subsequence and an array lis_len to store the length of the LIS up to each index of the original array.
How it works:
For each element in the array, we find the position where it can be inserted in the list lis using the bisect_left function, which keeps lis sorted.
If the element is greater than all elements in lis, it is added to the end. If not, it replaces the smallest element that is greater than or equal to it.
The length of the increasing subsequence is updated in lis_len.

Main Function minimumMountainRemovals:
Calculates lis_lr, which is the LIS of the original array.

Calculates lis_rl, which is the LIS of the reversed array (to find the decreasing subsequence) and reverses it back to match the indices of the original array.

Comparison:

For each index of the array, we check if lis_lr[i] > 1 and lis_rl[i] > 1. This means that at i, we can form a mountain.
The sum of the sizes of lis_lr[i] and lis_rl[i] (subtracting 1 to not count the peak twice) gives us the size of the mountain at that index.
Calculating the Result:
The maximum size of the mountain found is subtracted from the original size of the array to determine how many elements need to be removed.
Detailed Example
Let's consider the example nums = [2, 1, 1, 5, 6, 2, 3, 1]:

Calculating lis_lr
Original array: [2, 1, 1, 5, 6, 2, 3, 1]
Calculation:
For 2, lis = [2], lis_len[0] = 1.
For 1, not greater than 2, so replaces 2 with 1: lis = [1], lis_len[1] = 1.
For 1 (again): lis = [1], lis_len[2] = 1.
For 5, lis = [1, 5], lis_len[3] = 2.
For 6, lis = [1, 5, 6], lis_len[4] = 3.
For 2, lis = [1, 2, 6], lis_len[5] = 2.
For 3, lis = [1, 2, 3], lis_len[6] = 3.
For 1, lis = [1], lis_len[7] = 1. Result: lis_lr = [1, 1, 1, 2, 3, 2, 3, 1]`

Calculating lis_rl
Reversed array: [1, 3, 2, 6, 5, 1, 1, 2]
Calculation:
For 1, lis = [1].
For 3, lis = [1, 3].
For 2, replaces 3 with 2: lis = [1, 2].
For 6, lis = [1, 2, 6].
For 5, replaces 6 with 5: lis = [1, 2, 5].
For 1, lis = [1].
For 1 (again): lis = [1].
For 2, lis = [1, 2].
Result (reversing back): lis_rl = [2, 2, 3, 2, 1, 1, 1, 1]

Finding the Maximum Mountain
Now, we check where we can have a mountain:
For i = 0: lis_lr[0] = 1, lis_rl[0] = 2 → Not a mountain.
For i = 1: lis_lr[1] = 1, lis_rl[1] = 2 → Not a mountain.
For i = 2: lis_lr[2] = 1, lis_rl[2] = 3 → Not a mountain.
For i = 3: lis_lr[3] = 2, lis_rl[3] = 2 → Is a mountain. Size = 2 + 2 - 1 = 3.
For i = 4: lis_lr[4] = 3, lis_rl[4] = 2 → Is a mountain. Size = 3 + 2 - 1 = 4.
For i = 5: lis_lr[5] = 2, lis_rl[5] = 1 → Not a mountain.
For i = 6: lis_lr[6] = 3, lis_rl[6] = 1 → Not a mountain.
For i = 7: lis_lr[7] = 1, lis_rl[7] = 1 → Not a mountain.
Maximum Mountain: The maximum size of the mountain is 4.

Final Result
Original size of the array: 8
Size of the largest mountain: 4
Elements to remove: 8 - 4 = 4
